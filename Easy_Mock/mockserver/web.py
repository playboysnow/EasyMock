#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect
import urllib,requests,os,sys
import logging
import json,yaml
import time
import platform
from surgery import surgery

reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')
"""
参数解析，比如-h  -f 

支持json文件读取，根据固定格式py 自由添加逻辑判断

支持https、其他协议

支持添加逻辑判断——把控安全风险

根据不同端口启动，且可以启动N多个API

单独打包支持 即时启动即刻使用

前端界面、支持登陆 短信验证码

服务部署的话，支持mongodb json格式存储，且之前短信验证码登陆验证

远程机器调用，即host不再是0.0.0.0    先调研  不支持

"""

class web(object):
   
    def __init__(self):
        #self.sys_type=platform.system()   #"Windows,Linux"
        pass
    
    global req
    req={"url":"/123","response":{"code ":"ok "},"type":1,"method":["POST"],"sleeptime":0,"host":"0.0.0.0","port":5001}
    global type_1_file 
    type_1_file='runserver.py'
    global type_2_file 
    type_2_file='simpleserver.py'
    global port
    port=8080
    global host
    host='0.0.0.0'
    global app
    app=Flask(__name__)


    @app.route('/',methods=["GET,POST"])

    def index():

        return render_template("index.html")


    @app.route('/mockstart',methods=["POST"])
    
    def mockstart():
        data=request.get_data()
        #print data,eval(data)
        #js_data=json.loads(data)
        #js_data=yaml.safe_load(data)
        #print js_data
        mock_type=eval(data)['type']
        #根据不同类型执行不同类型文件
        if mock_type==1:
            #调用shell 执行常规方式
            #return json.dumps(eval(data)['response'])  启动后 如何响应状态
            print "start"
            surgery().system(type_1_file,eval(data))
            #server.play(eval(data))
            return  json.dumps(eval(data)['response'])
            
        elif mock_type==2:
            #调用
            surgery().system(type_2_file,eval(data))
            return  json.dumps(eval(data)['response'])
            pass
        elif mock_type==3:
            pass
        else:
            pass

       #return  json.dumps(eval(data)['response'])
    @app.route('/mockstop',methods=["POST"])
    
    def mockstop():
        data=request.get_data()
        mock_type=eval(data)['type']
        #根据不同类型执行不同类型文件
        if mock_type==1:
            #调用shell 执行常规方式
            surgery().clear(type_1_file,eval(data)['port'])
            return  json.dumps(eval(data)['response'])
            pass
        elif mock_type==2:
            #调用
            surgery().clear(type_2_file,eval(data)['port'])
            return  json.dumps(eval(data)['response'])
            pass
        elif mock_type==3:
            pass
        else:
            pass

        #return  json.dumps(response)
    def run(self,debug=False):
        app.run(host=host,port=port,debug=debug)
        pass
    
    
    
if __name__=='__main__':
    #web().system(file,req)
    web().run()
    









    