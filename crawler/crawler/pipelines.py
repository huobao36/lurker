# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import items, json
from lurker.service.itemservice import ItemService


class SeekingAlpahPipeline(object):
    def __init__(self):
        self.file = open('content.jl', 'wb')
        
    def process_item(self, item, spider):
        if spider.name in ['seekingalpha']:
            if item['type'] == 'content':
                ItemService().insert_article(item)
            elif item['type'] == 'reply':
                ItemService().insert_comment(item)
            line = json.dumps(dict(item)) + "\n"      
            self.file.write(line)                      








