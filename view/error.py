# coding: utf-8


from core.web import BaseHandler


class NotFoundHandler(BaseHandler):
    def prepare(self):
        self.send_error(404)
