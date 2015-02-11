from django.shortcuts import render
from django.http import HttpResponse

import urllib2
import base64
import urllib
import re
import sys
import json
import requests


# Create your views here.
def index(request):
    url = 'http://www.baidu.com'
    req = urllib2.urlopen(url)
    content = req.read()
    return HttpResponse(content)


def open(request, url):
    url = urllib.unquote(url).replace('amp;', '')
    print url
    cookie = "qlskey=v0ae5838c1254d9dd1d000054d3a084a; qq_logtype=16; qluin=onqOjjuMMTyDPcdHlbifOpdGefks; refresh_token=OezXcEiiBSKSxW0eoylIeDVpIfWQLaEk3KQhEkPa_90l2J-ndSMgC30kUWKvDG79wBK8Qxt3RYy6dAcmXe-klfsjEAlMvg3JyNgW_yEIlNcywMjakI6IWY8VLkpO4ATJ9cclrEVJG5rFJGTlgyGn8g; qlappid=wx6fa7e3bab7e15415"
    return HttpResponse(_money(url, cookie))


def _money(url, cookie):
    headers_fake = {'User-Agent': ("Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Galaxy Nexus - 4.2.2 - with Google Apps"
                                   "- API 17 - 720x1280 1 Build/JDQ39E) AppleWebKit/534.30 (KHTML, like Gecko)"
                                   "Version/4.0 Mobile Safari/534.30 MicroMessenger/5.3.0.80_r701542.440"),
                    'X-Requested-With': 'com.tencent.mm',
                    'Cookie': cookie,
                   }
    # print '[*] Get key value: %s\n' % url
    try:
        req_key_content = requests.get(url, headers=headers_fake).content
    except Exception,e:
        print e
    try:
        g_sendld = re.findall('g_sendId: "(.*?)",', req_key_content)
        g_sendnick = re.findall('g_sendNick: "(.*?)",', req_key_content)
        g_detailtoke = re.findall('g_detailToke: "(.*?)",', req_key_content)
        g_detailtoke = (g_detailtoke[0])
        # print '[+] Money key: \n\tSendNick:%s\n\tSendld:%s\n\tDetailToke:%s\n' % (g_sendnick[0], g_sendld[0], g_detailtoke)
    except Exception, e:
        print '[-] Error: %s' % str(e)
        return False

    sign_key = (str(url.split('&')[-1:]).split('=')[1])[:-2]
    receive_url = ("https://wxapp.tenpay.com/app/v1.0/wxhb_open.cgi?msg_type=&send_id=%s&channel_id=&detailToke=%s&scene="
                   "&us=&sign=%s&attention=0&hb_version=v2&ver=2&isappinstalled=0&clientversion=25030050&devicetype=android"
                   "-17")
    receive_url = receive_url % (g_sendld[0], g_detailtoke[:-4]+'%3D', sign_key)
    # print '[+] Request receive_url: %s\n' % receive_url
    receive_content = requests.get(receive_url, headers=headers_fake).content
    try:
        return_json_data = json.loads(receive_content)
        if return_json_data['retmsg'] == 'ok':
            money_count = return_json_data['amount'] * 0.01
            print '[+] Success: %s$' % money_count
            return money_count
        else:
            print '[-] Status: %s' % return_json_data['retmsg']
    except Exception, e:
        print str(e)