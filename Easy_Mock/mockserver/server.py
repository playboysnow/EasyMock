#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib,requests,sys
import logging
import json
reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')
class play(object):
    def __init__(self,req):
        pass 
    def check(self,data):
        if data['id']==1:
            return True
        else:
            return False
    
