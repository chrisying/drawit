from google.appengine.api import users

import webapp2

class MainPage(webapp2.RequestHandler):

  def get(self):

    # Checks for Google user
    user = users.get_current_user()

    if user:
      self.response.write('Hello drawit!')
    else:
      self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
