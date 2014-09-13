import os, sys

from google.appengine.api import users
from google.appengine.ext import db

import jinja2
import webapp2

import picture
from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

  def get(self):
    
    # An example of putting an image into database
    # Does not work yet!
    '''
    p1 = picture.Picture(title = 'butterfly',image = db.Blob(urlfetch.Fetch('http://localhost:8080/pics/butterfly.png').content))
    p1.put()
    '''
    p2 = picture.Picture(title = 'doge',image = db.Blob(urlfetch.Fetch('http://doge2048.com/meta/doge-600.png').content))
    p2.put()

    # Checks for Google user
    user = users.get_current_user()

    if user:
      # Fetch the recent 10 images user has contributed to
      # TODO

      # Temp
      template_values = {
          'pictures': db.GqlQuery('SELECT * FROM Picture WHERE title = :1 LIMIT 1', 'doge').fetch(1)
      }
      template = JINJA_ENVIRONMENT.get_template('mainpage.html')
      self.response.write(template.render(template_values))
    else:
      self.redirect(users.create_login_url(self.request.uri))
