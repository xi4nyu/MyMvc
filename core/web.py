# coding: utf-8
#
# Web Handler core
#


import tornado.web



class BaseHandler(tornado.web.RequestHandler):
    def _get(self, key, default=None):
        return self.get_argument(key, default)


    def _gets(self, key):
        return self.get_arguments(key)
