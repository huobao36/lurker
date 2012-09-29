from lurker.db.dbutil import DBUtil
from lurker.core.basefunc import singleton

# encoding = utf-8

@singleton
class ItemService:    
    SQL_INSERT_CONTENTITEM = "insert into article (user_name, title, content, time)\
            values ('{0}', '{1}', '{2}', '{3}')"

    SQL_INSERT_COMMENTITEM = 'insert into comment(id, reply_to, reply_to_type, content, time)\
            values ({0}, {1}, {2}, {3}, {4})'

    SQL_SELECT_NEWEST_ATICLEID = 'select id from article order by time desc limit 1'

    SQL_SELECT_NEWEST_COMMENTID = 'select id from comment order by time desc limit 1'

    def insert_article(self, contentitem):
        print('sql: ' + self.SQL_INSERT_CONTENTITEM.format(contentitem['user_name'], 
            contentitem['title'], contentitem['content'], contentitem['time']))
#        DBUtil.execute(self.SQL_INSERT_CONTENTITEM.format(contentitem['user_name'],
#            contentitem['title'], contentitem['content'], contentitem['time']))
       
    def insert_comment(self, replyitem):
        DBUtil.execute(self.SQL_INSERT_COMMENTITEM.format(replyitem['id'],replyitem['user_name'],
            replyitem['title'], replyitem['content'], replyitem['time']))

    def get_newest_article_id(self):
        return DBUtil.query(self.SQL_SELECT_NEWEST_ATICLEID)

    def get_newest_coment_id(self):
        return DBUtil.query(self.SQL_SELECT_NEWEST_REPLYID)




