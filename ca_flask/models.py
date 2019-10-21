from mongoengine import *

class Articles(Document):
    source = StringField()
    url = StringField()
    article_name = StringField()
    date = StringField()

