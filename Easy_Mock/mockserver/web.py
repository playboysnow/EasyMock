#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect
import urllib,requests,os,sys
import logging
import json
import time
import platform
reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')


class web(object):
   
    def __init__(self):
        self.res_succ={"code":0,"message":"server start succ"}
        self.res_fail={"code":1,"message":"server start fail"}
        #sys_type=platform.architecture()[1]
        self.sys_type=platform.system()   #"Windows,Linux"
        pass
    global req
    req={"url":"/123","response":{"code ":"ok "},"type":1,"method":["POST"],"sleeptime":0,"host":"0.0.0.0","port":5001}
    global port
    port=8080
    global host
    host='0.0.0.0'
    global app
    app=Flask(__name__)


    @app.route('/',methods=["GET,POST"])

    def index():

        return render_template("index.html")


    @app.route('/mockserver',methods=["POST"])
    
    def mock():
        data=request.get_data()
        js_data=json.loads(data)
        mock_type=js_data('type')
        #根据不同类型执行不同类型文件
        if mock_type==1:
            #调用shell 执行常规方式
            pass
        elif mock_type==2:
            #调用
            pass
        elif mock_type==3:
            pass
        else:
            pass

        return  json.dumps(response)
    def run(self,debug=False):
        app.run(host=host,port=port,debug=debug)
        pass

    def system(self,req):
        if self.sys_type=="Windows":
            print 'python2 runserver.py %s ' % req
            if os.system('python2 runserver.py "'"%s"'" ' % req) !=0:
                print self.res_fail
                return self.res_fail
        elif self.sys_type=="Linux":
            if os.system('python runserver.py "'"%s"'" ' % req) !=0:
                return self.res_fail


if __name__=='__main__':
    web().system(req)
    









    