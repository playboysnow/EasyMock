#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect
import urllib,requests,sys
import logging
import json
import time
reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')


class runserver(object):
    '''#{"url":"/123","response":{"code ":"ok "},"type":1,"method":["POST"],"sleeptime":0,"host":"0.0.0.0","port":5001}
    print type(sys.argv[1])
    req_get=json.loads(json.dumps(sys.argv[1]))
    #print type(req_get)
    print type(eval(str(req_get))),json.dumps(eval(str(req_get))),eval(str(req_get))
     #parm=json.loads(json.dumps(eval(str(req_get))))
    '''
    parm=eval(str(sys.argv[1]))
    print type(parm)
    url=parm['url']
    global response
    response=parm['response']
    type=parm['type']
    method=parm['method']
    global sleeptime 
    sleeptime=parm['sleeptime']
    global host 
    host=parm['host']
    global port 
    port=parm['port']
    def __init__(self):
        '''
        self.url=sys.argv[1]
        self.response=sys.argv[2]
        self.type=sys.argv[3]
        self.method=sys.argv[4]
        self.sleeptime=sys.argv[5]
        self.host=sys.argv[6]
        self.port=sys.argv[7]
        '''
        pass
    
    global app
    app=Flask(__name__)
    @app.route(url+'/<args>',methods=method)
    
    def index(args):
        time.sleep(sleeptime)
        return  json.dumps(response)
    def run(self,debug=False):
        app.run(host=host,port=port,debug=debug)
        pass


if __name__=='__main__':
    runserver().run()
    









    