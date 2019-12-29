# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:24:11 2019

@author: luiscar
"""

import urllib.request, http.client,io

class VerboseHTTPResponse(http.client.HTTPResponse):
        def _read_status(self):
            s = self.fp.read()
            print('-' * 20 , 'Response', '-' * 20)
            t = s.decode("UTF-8")
            print(t.split('\r\n\r\n')[0])
            #self.fp = io.StringIO(s)
            self.fp = io.BytesIO(s)
            return http.client.HTTPResponse._read_status(self)

class VerboseHTTPConection(http.client.HTTPConnection):
        response_class = VerboseHTTPResponse
        def send(self,s):
            print('-' * 50)
            print(s.strip())
            http.client.HTTPConnection.send(self,s)

class VerboseHTTPHandler(urllib.request.HTTPHandler):
        def http_open(self,req):
            return self.do_open(VerboseHTTPConection,req)

if __name__ == '__main__':
    from bs4 import BeautifulSoup as bs
    opener = urllib.request.build_opener(VerboseHTTPHandler)
    #info = opener.open('http://www.ietf.org/rfc/rfc2616.txt')
    info = opener.open('http://192.168.0.14:80')
    print(info.code)
    print(info.msg)
    bsObj = bs(info.read(),"lxml")
    print(bsObj.tr,)
