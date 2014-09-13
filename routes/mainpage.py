import os, sys

from google.appengine.api import users
from google.appengine.ext import db

import jinja2
import webapp2

import picture
from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

  def get(self):
    
    # An example of putting an image into database
    # p2 = picture.Picture(title = 'doge',row=3, col=3, image = db.Blob(urlfetch.Fetch('http://doge2048.com/meta/doge-600.png').content))
    # p2.put()

    # Checks for Google user
    user = users.get_current_user()
    init = self.request.get('init')

    result1 = db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', 'butterfly', 0, 0).fetch(1)
    result2 = db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', 'butterfly', 0, 1).fetch(1)
    result3 = db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', 'butterfly', 1, 0).fetch(1)
    result4 = db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', 'butterfly', 1, 1).fetch(1)

    if user:
      template_values = {
          'topleft': result1[0].image if len(result1) > 0 else '',
          'topright': result2[0].image if len(result2) > 0 else '',
          'bottomleft': result3[0].image if len(result3) > 0 else '',
          'bottomright': result4[0].image if len(result4) > 0 else '',
          'reference': '/assets/butterfly.png',
          'showimg': not init
      }
      template = JINJA_ENVIRONMENT.get_template('mainpage.html')
      self.response.write(template.render(template_values))
    else:
      self.redirect(users.create_login_url(self.request.uri))
