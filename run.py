#!/usr/bin/env python
# coding: utf-8
#
# web server run app
#

import os
import logging

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.process
import tornado.httpserver

from core.util import get_handlers
from view.error import NotFoundHandler
from settings import DEBUG, GZIP, PORT



def main():
    tornado.options.parse_command_line()
    tornado.options.print_help()
    settings = dict(
        debug=DEBUG,
        gzip=GZIP,
        autoescape="xhtml_escape",
        cookie_secret="YjQwYzRkN2YtMGExYi00ODAyLTlhMjQtYWJkZjYyMTBiMjI3YjhjMjZmNTQtODFlYi00ZDA0LTlhNzQtNDAyOGRiYWM0OWNj",
        login_url="/login",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

    handlers = get_handlers()
    handlers.append((r"/.*", NotFoundHandler))
    application = tornado.web.Application(handlers, **settings)
    
    if DEBUG: logging.getLogger().setLevel(logging.DEBUG)
    print "listen on ", PORT

    # http_server.listen(PORT)
    # http_server.bind(options.port)
    # http_server.start()
    sockets = tornado.netutil.bind_sockets(PORT)
    # tornado.process.fork_processes(0)

    ssl_options = {
        "certfile": "static/server.crt",
        "keyfile": "static/server.key",
        #"cert_reqs": ssl.CERT_REQUIRED,
        #"ca_certs": "static/ca.crt"
        }
    http_server = tornado.httpserver.HTTPServer(application)#, ssl_options=ssl_options)
    http_server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    main()
