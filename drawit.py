from google.appengine.api import users

import webapp2

from mainpage import MainPage
# from drawpage import DrawPage
from picture import GetImage

application = webapp2.WSGIApplication([
  ('/', MainPage),
  # ('/draw', DrawPage),
  ('/picture', GetImage),
], debug=True)
