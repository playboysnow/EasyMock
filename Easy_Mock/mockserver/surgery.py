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

            if os.system('python2  %s  "'"%s"'" ' % (file , req)) ==0:
                #print self.res_fail
                return self.res_succ
        elif self.sys_type=="Linux":
            if os.system('python (%s  "'"%s"'" )' % (file, req)) ==0:
                return self.res_succ













    