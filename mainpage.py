from google.appengine.api import users
from google.appengine.ext import db

import webapp2

import picture
from google.appengine.api import urlfetch

class MainPage(webapp2.RequestHandler):

  def get(self):
    
    # An example of putting an image into database
    # Delete me later
    p = picture.Picture(title = 'doge',image = db.Blob(urlfetch.Fetch('http://doge2048.com/meta/doge-600.png').content))
    p.put()

    # Checks for Google user
    user = users.get_current_user()

    if user:
      self.response.write('Hello drawit!')
    else:
      self.redirect(users.create_login_url(self.request.uri))
