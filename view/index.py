# coding: utf-8


from core.web import BaseHandler
from core.util import url

@url(r"/")
class IndexHandler(BaseHandler):
    def get(self):
        r = [{"name": "jack"}, {"name": "tk"}]
        self.render("index.html", r = r)


