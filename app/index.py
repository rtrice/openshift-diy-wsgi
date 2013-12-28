#!/usr/bin/env python
# coding:utf-8

try:
    import gevent
    import gevent.monkey
    gevent.monkey.patch_all()
except ImportError:
    pass

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World']

