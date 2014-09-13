import os
import urllib
import cgi

from google.appengine.ext import db
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
    #if (len(db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', 'butterfly', 0, 0).fetch(1)) > 0):
     # if (len(db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', 'butterfly', 0, 1).fetch(1)) > 0):
      #  if (len(db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', 'butterfly', 1, 0).fetch(1)) > 0):
  #        if (len(db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', 'butterfly', 1, 1).fetch(1)) > 0):
   #         picture_number = 1
   #       else:
   #         picture_number = 4
   #     else:
   #       picture_number = 3
   #   else:
    #    picture_number = 2
    #else:
     # picture_number = 1
    if (len(db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', 'butterfly', 0, 0).fetch(1)) > 0):
      print("DAMN")
    else:
      print(1111111);

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
      'user_linktext': user_linktext,
      #'picture_number': picture_number,
      #'row': (picture_number - 1) / 2
      #'col': (picture_number - 1) % 2
    }

    template = JINJA_ENVIRONMENT.get_template('drawPage.html')
    self.response.write(template.render(template_values))

class Upload(webapp2.RequestHandler):
  def post(self):
    pass