#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect
import urllib,requests,os,sys
import argparse,getopt
import logging
import json,yaml
import time
import platform
from surgery import surgery
#from runserver import runserver
#import server
reload(sys)
sys.setdefaultencoding('UTF-8')
surgery=surgery()
#sys.setdefaultencoding('gb2312')
"""
1、可以使用闭包解决 python 文件的形式：   done
比如
b.py:
from flask import Flask,render_template,request,redirect
def run_server(data):
        url=data['url']
        port=data['port']
        app=Flask(__name__)
        @app.route(url,methods=['POST'])
        def index():
                print "bb"
        def run():
                app.run(host="0.0.0.0",port=port,debug=False)
        run()

a.py:
from flask import Flask,render_template,request,redirect
import b
data={
        "url":"/123",
        "port":8080
        }
b.run_server(data)

参数解析，比如-h  -f 

支持json文件读取，根据固定格式py 自由添加逻辑判断

支持https、其他协议

支持添加逻辑判断——把控安全风险

根据不同端口启动，且可以启动N多个API；相同端口下启动多个URL

单独打包支持 即时启动即刻使用       Linux低内核可能coredump,6.4以上

前端界面、支持登陆 短信验证码       

服务部署的话，支持mongodb json格式存储，且之前短信验证码登陆验证

远程机器调用，即host不再是0.0.0.0    先调研  不支持

"""

class web(object):
   
    def __init__(self):
        #self.sys_type=platform.system()   #"Windows,Linux"
        #self.a="a"
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hf:vw")
        except:
            self.usage()
        try:
            for op,value in opts:
                if op == "-h":
                    self.usage()
                    sys.exit()
                elif op == "-f":
                    surgery.start(value)
                elif op == "-v":
                    print "version 1.1.0"
                else: 
                    pass
        except:
            pass
        try:
            if "-w" in sys.argv[1:]:
                run()
            else:
                #self.usage()
                pass
        except:
            run()
        else:pass
        pass
    
    def usage(self):
        print """
usage: [-h] [-f] [-v]
        
        -h     help information
        -f     file (json)
        -v     version
        -w     start webui at 127.0.0.1:8080

eg:
        ./bin  -f type1.json 
        ./bin  -h
        ./bin  -v
        ./bin
        ./bin  -w 
        """
        pass
    global req
    req={"url":"/123","response":{"code ":"ok "},"type":1,"method":["POST"],"sleeptime":0,"host":"0.0.0.0","port":5001}
   
    global port
    port=8080
    global host
    host='0.0.0.0'
    global run
    global app
    app=Flask(__name__)


    @app.route('/',methods=["GET,POST"])

    def index():

        return render_template("index.html")


    @app.route('/mockstart',methods=["POST"])
    
    def mockstart():
        #print self.a
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
            #surgery.system(type_1_file,eval(data))
            surgery.type_1_server(data)
            #print surgery.json_to_dict(data)
            #server.play(eval(data))
            return  json.dumps(eval(data)['response'])
            
        elif mock_type==2:
            #调用
            #surgery.system(type_2_file,eval(data))
            surgery.type_2_server(data)
            return  json.dumps(eval(data)['response'])
            pass
        elif mock_type==3:
            surgery.type_3_server(data)
            return  json.dumps(eval(data)['response_succ'])
            pass
        elif mock_type==4:
            surgery.type_4_server(data)
            return  json.dumps(eval(data)['response_succ'])
            pass

       #return  json.dumps(eval(data)['response'])
    @app.route('/mockstop',methods=["POST"])
    
    def mockstop():
        data=request.get_data()
        mock_type=eval(data)['type']
        surgery.clear(eval(data)['port'])
        return json.dumps(eval(data)['response'])
        '''#根据不同类型执行不同类型文件
        if mock_type==1:
            #调用shell 执行常规方式
            surgery.clear(eval(data)['port'])
            #surgery.json_to_dict(data)
            return  json.dumps(eval(data)['response'])
            pass
        elif mock_type==2:
            #调用
            surgery.clear(eval(data)['port'])
            return  json.dumps(eval(data)['response'])
            pass
        elif mock_type==3:
            surgery.clear(eval(data)['port'])
            return  json.dumps(eval(data)['response'])
            pass
        else:
            pass
        '''
        #return  json.dumps(response)
    @app.route('/sendsms',methods=['POST'])
    def send_sms():
        """发送验证码"""
        data=request.get_data()
        surgery.send(data)
        surgery.cron()
        pass
    @app.route('/login',methods=['POST'])
    def login():
        """验证登陆逻辑"""
        data=request.get_data()
        surgery.login(data)
        pass
    
    def run(debug=False):
        app.run(host=host,port=port,debug=debug)
        pass
    
    
    
if __name__=='__main__':
    #web().system(file,req)
    web()
    
    #runserver().run()
    
    
    









    