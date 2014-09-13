'''Database entry template for all images.'''

from google.appengine.ext import db

import webapp2

class Picture(db.Model):
  # Unique title to image
  title = db.StringProperty(required=True)

  # Image binary
  image = db.BlobProperty(required=True)

  # True if image is subimage of another image
  isSub = db.BooleanProperty()

  # Row/col of subimage (0 indexed)
  # Ignored if isSub is false
  row = db.IntegerProperty()
  col = db.IntegerProperty()

  # True if image is a user drawn image
  isUser = db.BooleanProperty()

  # Email of user who drew this picture
  # Ignored if isUser is false
  user = db.EmailProperty(default=None)

class GetImage(webapp2.RequestHandler):
  def get(self):
    title = self.request.get('title')
    isSub = self.request.get('isSub')
    isUser = self.request.get('isUser')
    row = self.request.get('row')
    col = self.request.get('col')
    if not isSub and not isUser:
      result = db.GqlQuery('SELECT * FROM Picture WHERE title = :1 LIMIT 1',
                           title).fetch(1)
      if result:
        picture = result[0]
      else:
        picture = None

    # Missing two isSub/isUser cases

    if picture:
      self.response.headers['Content-Type'] = 'image/png'
      self.response.out.write(picture.image)
    else:
      self.response.write('Picture not found!')
