from google.appengine.api import users

import webapp2

from routes.mainpage import MainPage
from routes.drawPage import DrawPage
from routes.picture import ImagePage

application = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/draw', DrawPage),
  ('/picture', ImagePage),
], debug=True)
