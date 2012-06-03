import webapp2
import json

from google.appengine.api import urlfetch

import os
from google.appengine.ext.webapp import template

class RootResponse(webapp2.RequestHandler):
    def get(self):
        data_urls = self.request.get_all('d')
        try:
            urlfetch.fetch(url = data_urls[0],
                           method = urlfetch.POST)
        except:
            pass
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'leaf.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', RootResponse)],
                              debug=True)
