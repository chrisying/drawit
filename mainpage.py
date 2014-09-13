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
    p2 = picture.Picture(title = 'doge',image = db.Blob(urlfetch.Fetch('http://doge2048.com/meta/doge-600.png').content))
    p2.put()

    # Checks for Google user
    user = users.get_current_user()

    if user:
      template_values = {
          'topleft': '/picture?title=butterfly&row=0&col=0',
          'topright': '/picture?title=butterfly&row=0&col=1',
          'bottomleft': '/picture?title=butterfly&row=1&col=0',
          'bottomright': '/picture?title=butterfly&row=1&col=1',
          'reference': '/pics/butterfly.png'
      }
      template = JINJA_ENVIRONMENT.get_template('mainpage.html')
      self.response.write(template.render(template_values))
    else:
      self.redirect(users.create_login_url(self.request.uri))
