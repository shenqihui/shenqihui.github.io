#!/usr/bin/env python
# coding:utf-8


from flask import Flask, render_template
from flask_cache import Cache
import json
import urllib2
import base64
import urllib
import re
import sys
import requests

app = Flask(__name__)



@app.route('/cb/<data>/')
def cbdata(data):
    print data
    return '''
        console.log(%s); done();
    ''' % data

# Create your views here.
@app.route('/baidu/')
def index():
    url = 'http://www.baidu.com'
    req = urllib2.urlopen(url)
    content = req.read()
    print content
    return content


@app.route('/url/<url>/')
def open(url):
    url = urllib.unquote(url).replace('amp;', '')
    print url
    # cookie = "qlskey=v0ae5838c1254d9dd1d000054d3a084a; qq_logtype=16; qluin=onqOjjuMMTyDPcdHlbifOpdGefks; refresh_token=OezXcEiiBSKSxW0eoylIeDVpIfWQLaEk3KQhEkPa_90l2J-ndSMgC30kUWKvDG79wBK8Qxt3RYy6dAcmXe-klfsjEAlMvg3JyNgW_yEIlNcywMjakI6IWY8VLkpO4ATJ9cclrEVJG5rFJGTlgyGn8g; qlappid=wx6fa7e3bab7e15415"
    # cookie = "qlskey=011ce82b10a42c35n7e8cc50; qq_logtype=16; qluin=oE15ntw3NJ0zAiy2PDfq8TZlD0QM; refresh_token=OezXcEiiBSKSxW0eoylIeDNaWBTpzeMI77zjmJ9cuxOi_IE7zpENC6Z173AkxAuOAG9Ft4ka2YJjb2b0p7OGzsXFWYv2D2m7KNkqs2gd3-J3WJesanymdoA0iln0dq7cIA1iMe5HgzKE3oJkyDe8uA; qlappid=wx3749d0c504fe6d16"
    cookie = "ts_uid=6067479761; cft-aa_qlappid=wx3cc22b542de028d4; cft-aa_qlskey=011ce82b10a42c35n7e8cc50; cft-aa_qluin=oE15ntw3NJ0zAiy2PDfq8TZlD0QM; cft-aa_qq_logtype=16; cft-aa_refresh_token=OezXcEiiBSKSxW0eoylIeDNaWBTpzeMI77zjmJ9cuxOi_IE7zpENC6Z173AkxAuOAG9Ft4ka2YJjb2b0p7OGzsXFWYv2D2m7KNkqs2gd 3-J3WJesanymdoA0iln0dq7cIA1iMe5HgzKE3oJkyDe8uA; cft-aa_wx_session_time=1423134035421; refresh_token=OezXcEiiBSKSxW0eoylIeDVpIfWQLaEk3KQhEkPa_93hmlC LBFltYKwL-cppb8YbdzLqYdlXAULQ7Q4Vq594tOd3S5pAuG2RmLjYsBbAK9fQj3-NyZQS3o2-vz9V8kLmY5KoQNiNZUeYje0TNrqMOA; wcp_uid=1311181964; wcp_qlskey=0785f4b970f1de208a4e562b9f4f8f09; wcp_qluin=085e9858e99cdc0fc73c4d0fe@wx.tenpay.com; wcp_qlappid=wx3749d0c504fe6d16; wcp_qq_logtype=16; openid=oTTG3jlan5txwW6cpCTSYmdBf6FU; wcp_nickname=%25E7%25A5%259E%25E5%25A5%2587%25E8%25BE%2589; wcp_pictureUrl=http%3A//wx.qlogo.cn/mmopen/Eq1BXuU11YQ4ZOQ1hElK0xZmnTIVlEZibYxYKfCGsj1nVcP1EibcwydMZ0S39fKztjcXc1daOQQE3MQBEyQiaVQpIx60XDfx6qP/0; qlskey=0785f4b970f1de208a4e562b9f4f8f09; qluin=085e9858e99cdc0fc73c4d0fe@wx.tenpay.com; qlappid=wx3749d0c504fe6d16; qq_logtype=16; is_encode=1; wcp_newlogin=1; wcp_rcode=1; pgv_info=ssid=s1248825146; pgv_pvid=658744462"
    # return HttpResponse(_money(url, cookie))
    return _money(url, cookie)


def _money(url, cookie):
    headers_fake = {'User-Agent': ("Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Galaxy Nexus - 4.2.2 - with Google Apps"
                                   "- API 17 - 720x1280 1 Build/JDQ39E) AppleWebKit/534.30 (KHTML, like Gecko)"
                                   "Version/4.0 Mobile Safari/534.30 MicroMessenger/5.3.0.80_r701542.440"),
                    'X-Requested-With': 'com.tencent.mm',
                    'Cookie': cookie,
                   }
    print '[*] Get key value: %s\n' % url

    try:
        req_key_content = requests.get(url, headers=headers_fake).content
    except Exception,e:
        print e

    try:
        g_sendld = re.findall('g_sendId: "(.*?)",', req_key_content)
        g_sendld = re.findall('g_sendId: "(.*?)",', req_key_content)
        g_sendnick = re.findall('g_sendNick: "(.*?)",', req_key_content)
        g_detailtoke = re.findall('g_detailToke: "(.*?)",', req_key_content)
        print g_detailtoke
        g_detailtoke = (g_detailtoke[0])
        # return '1'
        # print '[+] Money key: \n\tSendNick:%s\n\tSendld:%s\n\tDetailToke:%s\n' % (g_sendnick[0], g_sendld[0], g_detailtoke)
    except Exception, e:
        return '[-] Error: %s' % str(e)
        # return '2' #False

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
        print '*'*60, str(e)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)