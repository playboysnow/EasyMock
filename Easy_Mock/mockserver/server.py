#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,redirect
import urllib,requests,sys
import logging
import json
reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')
class check(object):
    
    def __init__(self):
        
        pass

    def docheck(self,req):
        #print req
        data=eval(req)
        #print data    
        if data["code"]==1:
                """
                返回response_succ
                """
                return True
        else:
                """
                返回response_fail
                """
                return False      
    
    
