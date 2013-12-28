#!/usr/bin/env python
# coding:utf-8

from app import application

if __name__ == '__main__':
    import os, logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - - %(asctime)s %(message)s', datefmt='[%b %d %H:%M:%S]')
    host = os.environ.get('OPENSHIFT_DIY_IP', '127.0.0.1')
    port = os.environ.get('OPENSHIFT_DIY_PORT', '8080')
    logging.info('local python application serving at %s:%s', host, port)
    from gevent.wsgi import WSGIServer
    WSGIServer((host, int(port)), application).serve_forever()

