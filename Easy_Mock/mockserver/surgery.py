#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect
import os,sys,random,time
import io
import logging
import json,yaml
import platform
from qcloudsms_py import SmsSingleSender
from qcloudsms_py import SmsMobileStatusPuller
from qcloudsms_py.httpclient import HTTPError

try:
    from server import check
except:
    pass
reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')


class surgery(object):
    global sms_num
    sms_num=[]
    def __init__(self):
        self.res_succ={"code":0,"message":"server start succ"}
        self.res_fail={"code":1,"message":"server start fail"}
        #sys_type=platform.architecture()[1]
        self.sys_type=platform.system()   #"Windows,Linux"
        #self.code=[]
    def system(self,file,req):
        if self.sys_type=="Windows":
            print 'python2 %s  %s ' % (file, req)

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
            print "start"
            pid=os.popen('start  /b  netstat  -ano |findstr %s ' % port).read()[-7:-1].replace(" ","")
            print pid
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
        if type(data)!=str:

            return eval(str(data))
        else:
            return eval(data)
        pass
    def cron(self):
        time.sleep(60)
        sms_num.pop()
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
        sms_num.append(sms_code)
        ssender = SmsSingleSender(appid, appkey)
        try:
        #print data['remobile'],data['text']
            result = ssender.send_with_param(86, data["phonenum"],
            template_id,[sms_code,'1'], extend="", ext="")
            if result['code']==0:
                print sms_code,sms_num
                return True
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
        data=self.json_to_dict(data)
        if data['sms_code']  in sms_num:
            sms_num.pop()#清理
            return  True
            pass
    def get_random_code(self):
        random_code=""
        for i in range (0,6):
            num=random.randint(0,9)
            random_code="%s%s" % (random_code,num)
        return random_code

    def read_file(self,file):
        fd=io.open(file,'r',encoding='utf-8').readlines()
        #with open(file,'r',encoding='utf-8') as f:
        return fd    
        pass



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
                print "启动失败，检查端口是否被占用"
        run()
        pass
    def type_2_server(self,data):
        s_data=self.json_to_dict(data)
        url=s_data['url']
        
        response=s_data['response']
        
        method=s_data['method']
        
        sleeptime=s_data['sleeptime']
        
        host=s_data['host']
        
        port=s_data['port']
        
        app=Flask(__name__)
        @app.route(url+'/<args>',methods=method)
    
        def index(args):
            time.sleep(sleeptime/1000)
            return  json.dumps(response)
        def run(debug=False):
            try:
                app.run(host=host,port=port,debug=debug)
            except:
                print "启动失败，检查端口是否被占用"
        run()

        '''
        app=Flask(__name__)
        @app.route(url+'/<args>',methods=method)
    
        def index(args):
            time.sleep(sleeptime/1000)
            return  json.dumps(response)
        def run(debug=False):
            try:
                app.run(host=host,port=port,debug=debug)
            except:
                print "启动失败，检查端口是否被占用"
        run()
        '''
    def type_3_server(self,data):
        """
        新增逻辑判断
        """
        s_data=self.json_to_dict(data)
        url=s_data['url']
        
        response_succ=s_data['response_succ']

        response_fail=s_data['response_fail']
        
        method=s_data['method']
        
        sleeptime=s_data['sleeptime']
        
        host=s_data['host']
        
        port=s_data['port']
        
        app=Flask(__name__)
        @app.route(url+'/<args>',methods=method)
    
        def index(args):
            time.sleep(sleeptime/1000)
            data=request.get_data()
            #j_data=eval(data)
            #print j_data,type(j_data)
            #print data ,type(data)
            if  check().docheck(data):
                return  json.dumps(response_succ)
            else:
                return json.dumps(response_fail)
        def run(debug=False):
            try:
                app.run(host=host,port=port,debug=debug)
            except:
                print "启动失败，检查端口是否被占用"
        run()

    def type_4_server(self,data):
        """
        新增逻辑判断
        """
        s_data=self.json_to_dict(data)
        url=s_data['url']
        
        response_succ=s_data['response_succ']

        response_fail=s_data['response_fail']
        
        method=s_data['method']
        
        sleeptime=s_data['sleeptime']
        
        host=s_data['host']
        
        port=s_data['port']
        
        app=Flask(__name__)
        @app.route(url,methods=method)
    
        def index():
            time.sleep(sleeptime/1000)
            data=request.get_data()
            #j_data=eval(data)
            #print j_data,type(j_data)
            #print data ,type(data)
            if  check.docheck(data):
                return  json.dumps(response_succ)
            else:
                return json.dumps(response_fail)
        def run(debug=False):
            try:
                app.run(host=host,port=port,debug=debug)
            except:
                print "启动失败，检查端口是否被占用"
        run()

    def start(self,data):
        
        data=self.read_file(data)
        print data
        j_data=eval(json.dumps(data))[0]
        print type(eval(j_data))
        mock_type=eval(j_data)['type']
        #根据不同类型执行不同类型文件
        if mock_type==1:
            self.type_1_server(j_data)
           
            return  json.dumps(eval(data)['response'])
            
        elif mock_type==2:
            #调用
            #surgery.system(type_2_file,eval(data))
            self.type_2_server(j_data)
            return  json.dumps(eval(data)['response'])
            pass
        elif mock_type==3:
            self.type_3_server(j_data)
            return  json.dumps(eval(data)['response_succ'])
            pass
        elif mock_type==4:
            self.type_4_server(j_data)
            return  json.dumps(eval(data)['response_succ'])
            pass
    