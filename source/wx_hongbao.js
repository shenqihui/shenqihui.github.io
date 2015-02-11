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
