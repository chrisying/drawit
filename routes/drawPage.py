import os
import urllib
import cgi

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../views')),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

class DrawPage(webapp2.RequestHandler):
  def get(self):
    if users.get_current_user():
      user = users.get_current_user()
      user_url = users.create_logout_url(self.request.uri)
      user_linktext = 'logout'
    else:
      user = None
      user_url = users.create_login_url(self.request.uri)
      user_linktext = 'login'

    template_values = {
      'user': user,
      'user_url': user_url,
      'user_linktext': user_linktext
    }

    template = JINJA_ENVIRONMENT.get_template('drawPage.html')
    self.response.write(template.render(template_values))

class Upload(webapp2.RequestHandler):
  def post(self):
    pass

application = webapp2.WSGIApplication([
    ('/', DrawPage)
], debug=True)