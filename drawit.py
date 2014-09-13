from google.appengine.api import users

import webapp2

from mainpage import MainPage
# from drawpage import DrawPage

application = webapp2.WSGIApplication([
  ('/', MainPage),
  # ('/draw', DrawPage),
], debug=True)
