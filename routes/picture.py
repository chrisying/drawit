'''Database entry template for all images.'''

from google.appengine.ext import db
from google.appengine.api import urlfetch

import webapp2

class Picture(db.Model):
  # Unique title to image
  title = db.StringProperty(required=True)

  # Image binary
  image = db.BlobProperty(required=True)

  # Row/col of subimage (0 indexed)
  # Ignored if isSub is false
  row = db.IntegerProperty()
  col = db.IntegerProperty()

  # Email of user who drew this picture
  # Ignored if isUser is false
  user = db.EmailProperty(default=None)

class ImagePage(webapp2.RequestHandler):
  def get(self):
    title = self.request.get('title')
    row = int(self.request.get('row'))
    col = int(self.request.get('col'))
    result = db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', title, row, col).fetch(1)
    if result:
      self.response.out.write('<img src="' + result[0].image + '">')
    else:
      self.response.write('Picture not found!')

  def post(self):
    picture = Picture(
        title=self.request.get('title'),
        image=self.request.get('image').encode('utf-8'),
        #image=db.Blob(urlfetch.fetch(self.request.get('image')).content),
        row=int(self.request.get('row')),
        col=int(self.request.get('col'))
    )
    picture.put()
