#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect
import urllib,requests,sys
import logging
import json
reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')

class run(object):

    def __init__(self,url,response,type,method,sleeptime,host,port):
        self.url=url
        self.response=response
        self.type=type
        self.method=method
        self.sleeptime=sleeptime
        self.host=host
        self.port=port
        pass
    app=Flask(__name__)
    @app.route(self.url,methods=self.method)











    def start(self,url,response,type,method,sleeptime,host,port):
        
        #@self.app.route(url,methods=method)
        if type==1:
            #@self.app.route(url,methods=method)
            self.index(response=response,sleeptime=sleeptime)
            self.run(host=host,port=port)
        elif type==2:
            #@self.app.route(url+'args',methods=method)
            self.index(args='args',response=response,sleeptime=sleeptime)
            self.run(host=host,port=port)
        else:
            pass

    def stop(self,port):
        pass
    
    def run(self,host,port,debug=False):
        self.app.run(host=host,port=port,debug=debug)
        pass

    def index(self,response,sleeptime=0):
        sleep(sleeptime)
        return  json.dumps(response)













server_args={}

def get_args(*args):
    
    return json.dumps(server_args)

#handler=logging.FileHandler('run.log',encoding='UTF-8')
sendurl='/send'
port=5001
method=["POST"]
app=Flask(__name__)
#app.logger.addHandler(handler)
@app.route(sendurl,methods=method)
def send():
    pass



if __name__=='__main__':

	app.run(host='0.0.0.0',port=port,debug=True)