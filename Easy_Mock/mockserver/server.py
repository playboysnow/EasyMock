#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect
import urllib,requests,sys
import logging
import json
reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')


def play(req):
        data=eval(str(req))
        gl_data=data
        host=data['host']
        
        port=data['port']
        run(host,port)
       
    
    
app=Flask(__name__)
@app.route(gl_data['url'],methods=gl_data['method'])  
def index():
        sleep(gl_data['sleeptime']/1000)
        return  json.dumps(gl_data['response'])
    
def run(host,port,debug=False):
        app.run(host=host,port=port,debug=debug)
        pass