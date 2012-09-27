# coding: utf-8
import MySQLdb
from lurker.core.configmanager import ConfigManager

class DBUtil:
    host = ''
    user = ''
    passwd = ''
    db = ''

    def get_connection():
        con = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, 
                    db=self.db, charset='utf8');
        return con
             
    def close_connection(con):
        if con:
            con.close()
       

    def __init__(self):
        self.host = ConfigManager().get_db_config('host')
        self.user = ConfigManager().get_db_config('user')
        self.db = ConfigManager().get_db_config('db')
        self.passwd = ConfigManager().get_db_config('passwd')

    @staticmethod
    def execute(sql):
        con = None
        try:
           con = get_connection()
           cursor = con.cursor()
           cursor.execute(sql)
           cursor.close()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])     
        finally:
            self.close_connection(con)

    @staticmethod
    def query(sql):
         con = None
         try:
            con = get_connection()                                           
            cursor = con.cursor()                                       
            cursor.execute(sql)                                              
            rows = cursor.fetchall()
            cursor.close()
            return rows
         except MySQLdb.Error, e:
             print "Error %d: %s" % (e.args[0], e.args[1])     
         finally:
             close_connection(con)
