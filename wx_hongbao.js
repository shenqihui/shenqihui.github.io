$._ajax = $.ajax;
l = [];
dataArr = [];
var urlArr = [];
var imgBase = "http://127.0.0.1:8000/"

function check(c, that){
    var AddMsgList = c.AddMsgList;
    if (AddMsgList) {
        AddMsgList.forEach(function(elem, index){
            var str = '';
            str = elem.Url || '';
            var img ;
            var isHongBao = /https:\/\/wxapp.tenpay.com/.test(str);
            if(isHongBao) {
                img = new Image();
                document.body.appendChild(img);
                img.src = imgBase+encodeURIComponent(encodeURIComponent(str))+"/";
                img.onload = img.onerror = function(){
                    document.body.removeChild(img);
                }
                console.log(str);
                urlArr.push(str);
            }
        });
    }
}

function success(e, n){
    e._s = e.success;
    e.success = function(data) {
        try{
            check(data, this);
            dataArr.push(data);
        } catch(e) {}
        this._s.call(this, data);    
        // this._s.apply(this, arguments);
    }
    c = $._ajax(e, n);
    l.push(c);
    return c;
}
$.ajax = success;


// https://wxapp.tenpay.com/app/v1.0/receive.cgi?showwxpaytitle=1&amp;sendid=10000349012015021110214502105&amp;channelid=1&amp;msgtype=1&amp;ver=2&amp;sign=583fce1cc4d7f41f1778817cbd0994aa8b9f4cf84dbc92c913474564e3d73bab33ecd7afbed2e214c78da51fdb9aa771a0fe24ff6ddd9d5b17bab0d0e2600c597af4241641f455df5285c35bb7d03b7300c82bd05d9190c6819cc55afcb8c9ed