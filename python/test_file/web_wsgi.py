#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import wsgiref.simple_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'derek')
    return [body.encode('utf-8')]

httpd = wsgiref.simple_server.make_server('', 8000, application)
print('Start Http Server on 8000...')

httpd.serve_forever()

