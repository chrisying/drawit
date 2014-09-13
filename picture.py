'''Database entry template for all images.'''

from google.appengine.ext import db

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
    row = self.request.get('row')
    col = self.request.get('col')
    result = db.GqlQuery('SELECT * FROM Picture WHERE title = :1 AND row = :2 AND col = :3 LIMIT 1', title, row, col).fetch(1)
    if result:
      self.response.headers['Content-Type'] = 'image/png'
      self.response.out.write(result[0].image)
    else:
      self.response.write('Picture not found!')

  def post(self):
    picture = Picture(
        title=self.request.get('title'),
        image=self.request.get('content')
        row=self.request.get('row'),
        col=self.request.get('col')
    )
    picture.put()
