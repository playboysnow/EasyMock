#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect
import os,sys,random,time
import logging
import json
import platform
from qcloudsms_py import SmsSingleSender
from qcloudsms_py import SmsMobileStatusPuller
from qcloudsms_py.httpclient import HTTPError
from concurrent.futures import ThreadPoolExecutor
import imp
import asyncio
imp.reload(sys)
#reload(sys)
#sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')


class surgery(object):
   
    def __init__(self):
        self.res_succ={"code":0,"message":"server start succ"}
        self.res_fail={"code":1,"message":"server start fail"}
        #sys_type=platform.architecture()[1]
        self.sys_type=platform.system()   #"Windows,Linux"
 
    def system(self,file,req):
        if self.sys_type=="Windows":
            #print 'python2 %s  %s ' % (file, req)

            code=os.system('start  /b   python2  %s  "'"%s"'"  ' % (file , req))
                #print self.res_fail
            if code==0:
                return self.res_succ
            else:
                return self.res_fail
        elif self.sys_type=="Linux":
            code=os.system('python %s  "'"%s"'"   &' % (file, req))
            if code==0:
                return self.res_succ
    def clear(self,port):
        if self.sys_type=="Windows":
            #print 'taskkill /im   python2.exe   /t  /f ' 
            #code=os.system('taskkill /im   python2.exe   /t  /f  ' )
            print ("start")
            pid=os.popen('start  /b  netstat  -ano |findstr %s ' % port).read()[-7:-1].replace(" ","")
            #print pid
            code=os.system('start  /b  taskkill /pid  %s /t  /f' % pid)
                #print self.res_fail
            if code==0:
                    return self.res_succ
        elif self.sys_type=="Linux":
            #code=os.system("ps aux |grep -v grep |grep %s |awk -F' ' '{print $2}'|xargs kill -9   &" ) % file
            code=os.system("netstat -nlp|grep %s |awk {'print $7'}|awk -F'/' '{print $1}'|xargs kill -9   &" ) % port
            if code==0:
                return self.res_succ
            else:
                return self.res_fail

    def json_to_dict(self,data):
        return json.loads(data)
        '''
        if type(data)!=str:

            return eval(str(data))
        else:
            return eval(data)
        pass
        '''
    def send(self,data):
        """
        data={
            phonehum:123,

        }
        """
        sms_type = 0
         # appid="140016XXXXX"
        appid="	1400162404"
        #appkey="9993bac2a2b15aXXX"
        appkey="9993bac2a2b15a202bd718ea"
        template_id=""
        sms_code=self.get_random_code
        ssender = SmsSingleSender(appid, appkey)
        try:
        #print data['remobile'],data['text']
            result = ssender.send_with_param(86, data["phonenum"],
            template_id,[sms_code,'5'], extend="", ext="")
            if result['code']==0:
                print (sms_code)
        except HTTPError as e:
            print(e)
        except Exception as e:
            print(e)
    def login(self,data):
        """
        data={
            phonenum="123",
            sms_code=""

        }
        """
        if data['sms_code']==self.send(data):
            return  True
            pass
    def get_random_code(self):
        random_code=""
        for i in range (0,6):
            num=random.randint(0,9)
            random_code="%s%s" % (random_code,num)
        return random_code

    def read_file(self,file):
        with open(file,'r',encoding='utf-8') as fd:
            read_data=fd.readlines()
            return  read_data

    def type_1_server(self,data):
        s_data=self.json_to_dict(data)
        url=s_data['url']
        
        response=s_data['response']
        
        method=s_data['method']
        
        sleeptime=s_data['sleeptime']
        
        host=s_data['host']
        
        port=s_data['port']
        app=Flask(__name__)
        @app.route(url,methods=method)
    
        def index():
            time.sleep(sleeptime/1000)
            return  json.dumps(response)
        def run(debug=False):
            try:
                app.run(host=host,port=port,debug=debug)
            except:
                print ("启动失败，检查端口是否被占用")
        run()
        pass
    #@asyncio.coroutine
    def type_2_server(self,data):
        s_data=self.json_to_dict(data)
        print (s_data,type(s_data))
        url=s_data['url']
        
        response=s_data['response']
        
        method=s_data['method']
        
        sleeptime=s_data['sleeptime']
        
        host=s_data['host']
        
        port=s_data['port']
        #executor = ThreadPoolExecutor(1)
        #print url[0]  调研一个端口支持多URL
        '''
        app=Flask(__name__)
        for i in range(0,len(url)):
            print url[i]
            #t=url[i]
            #app=Flask(__name__)
            @app.route('/'+url[i]+'/<args>',methods=method)
            
            def index(args):
                time.sleep(sleeptime/1000)
                return  json.dumps(response)
        def run(debug=False):
            try:
                app.run(host=host,port=port,debug=debug)
            except:
                print "启动失败，检查端口是否被占用"
        run()
        return True

        '''
        app=Flask(__name__)
        @app.route(url+'/<args>',methods=method)
    
        def index(args):
            time.sleep(sleeptime/1000)
            return  json.dumps(response)
        #@asyncio.coroutine
        def run(debug=False):
            try:
                app.run(host=host,port=port,debug=debug)
            except:
                print ("启动失败，检查端口是否被占用")
        #new_loop = asyncio.new_event_loop()
        #asyncio.set_event_loop(new_loop)
        #loop=asyncio.get_event_loop()
        #asyncio.ensure_future(run())
        #loop.run_forever()
        #loop.stop()
        run()
        #executor.submit(run())
        





    