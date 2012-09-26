# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class ContentItem(Item):
    # define the fields for your item here like:
    # name = Field()
    id = Field()
    user_name = Field()         
    title = Field()
    content = Field()
    time = Field()
    type = Field()
    def __init__(self):
        self.type = 'content'

class ReplyItem(Item):  
    id = Field()
    reply_to = Field()
    reply_to_type = Field()
    content = Field()
    time = Field()    
    type = Field()
    def __init__(self):
        self.type = 'comment'
   


