# coding:utf-8
from flask import Flask,request,make_response,abort
from hashlib import sha1
import xmltodict
import time

app = Flask(__name__)

@app.route('/wechat8000',methods=['GET','POST'])
def wechat():

    #设置token
    token = 'python'
    if request.method=='GET':
        #获取参数
        data = request.args
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')

        #对参数进行字典排序，拼接字符串
        temp = [timestamp,nonce,token]
        temp.sort()
        temp = ''.join(temp)
        #加密
        s1 = sha1()
        s1.update(temp.encode("utf8"))
        sign = s1.hexdigest()
        if sign !=signature:
            abort(403)
        else:
            return echostr
    if request.method=='POST':
        xml = request.data
        print(xml)
        req = xmltodict.parse(xml)['xml']
        if 'text' == req.get('MsgType'):
            resp = {
                'ToUserName':req.get('FromUserName'),
                'FromUserName':req.get('ToUserName'),
                'CreateTime':int(time.time()),
                'MsgType':'text',
                'Content':req.get('Content')
            }
            xml = xmltodict.unparse({'xml': resp})
            print(req.get('Content'))
            return xml
        else:
            resp = {
                'ToUserName': req.get('FromUserName', ''),
                'FromUserName': req.get('ToUserName', ''),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': 'I LOVE ITCAST'
            }
            xml = xmltodict.unparse({'xml':resp})
            return xml
    
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)

