#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import logging
import json,yaml
import platform
reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')


class surgery(object):
   
    def __init__(self):
        self.res_succ={"code":0,"message":"server start succ"}
        self.res_fail={"code":1,"message":"server start fail"}
        #sys_type=platform.architecture()[1]
        self.sys_type=platform.system()   #"Windows,Linux"
 
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
    def clear(self,file,port):
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
            code=os.system("ps aux |grep -v grep |grep %s |awk -F' ' '{print $2}'|xargs kill -9   &" ) % file
            if code==0:
                return self.res_succ
            else:
                return self.res_fail











    