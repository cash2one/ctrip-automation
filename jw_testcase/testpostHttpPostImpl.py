
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
import time,os,sys,datetime,unittest
import os
sys.path.append("../")
sys.path.append("../jw_modules")
import httplib
import unittest


class testcase_api_httpget(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('open09.edaixi.cn', 81, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    # change user interface for bazaar_utils & access story
    def test_testcasename001(self):
        try:
            self.httpClient.request('GET', '/client/v1/get_order?user_id=11452&order_id=12173793044055')
            # response object
            print "------------------>/client/v1/get_order?user_id=11452&order_id=12173793044055"
            response = self.httpClient.getresponse()
            print response.status
            statucode = response.status
            print response.read()
            if statucode == '200' or statucode == '201':
                print "The get_order_list status is 200 or 201"
                testpost();
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
