
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
import time,os,sys,datetime,unittest
import os
sys.path.append("../")
sys.path.append("../jw_modules")
import httplib
import unittest
from jw_utils.logUtils import *



class testcase_api_httpget_testcase001(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('open09.edaixi.cn1111111', 81, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    # change user interface for bazaar_utils & access story
    def test_testcase001(self):
        try:

            self.httpClient.request('GET', '/wisdomBsWeb/bs/BsSysUser/userListGetData')
            # response object
            response = self.httpClient.getresponse()
            print response.status
            statucode = response.status
            print response.read()
            if statucode == '200' or statucode == '201':
                print "The get_order_list status is 200 or 201"
                #self.assertEqual(1, 2);self.assertNotEqual(a, b)();
                print " the self.assertEqual(1, 2);self.assertNotEqual(a, b) ===========>", self.assertEqual(1, 2);self.assertNotEqual(a, b)
                self.assertEqual(1, 2);self.assertNotEqual(a, b)
                # for each_list in self.assertEqual(1, 2);self.assertNotEqual(a, b):
                #     print (each_list);
            else:
                raise "The get_order_list has exception"
                print response.reason
                print response.read()
                # self.assertEqual(statucode, 200,'incorrect default size')
        except Exception, e:
            print e
        #finally:
            #if self.httpClient:
                #self.httpClient.close()
