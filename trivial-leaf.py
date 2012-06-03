import webapp2
import json

from google.appengine.api import urlfetch

import os
from google.appengine.ext.webapp import template

class RootResponse(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'leaf.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', RootResponse)],
                              debug=True)
