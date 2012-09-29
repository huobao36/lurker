# coding: utf-8
import MySQLdb
from lurker.core.configmanager import ConfigManager

class DBUtil:
    @staticmethod
    def get_connection():
        dbhost = ConfigManager().get_db_config('host')
        dbuser = ConfigManager().get_db_config('user')
        dbname = ConfigManager().get_db_config('db')
        dbpasswd = ConfigManager().get_db_config('passwd')
        con = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, 
                    db=dbname, charset='utf8');
        return con
    
    @staticmethod
    def close_connection(con):
        if con:
            con.close()

    @staticmethod
    def execute(sql):
        con = None
        try:
           con = DBUtil.get_connection()
           cursor = con.cursor()
           cursor.execute(sql)
           cursor.close()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])     
        finally:
            DBUtil.close_connection(con)

    @staticmethod
    def query(sql):
         con = None
         try:
            con = DBUtil.get_connection()                                           
            cursor = con.cursor()                                       
            cursor.execute(sql)                                              
            rows = cursor.fetchall()
            cursor.close()
            return rows
         except MySQLdb.Error, e:
             print "Error %d: %s" % (e.args[0], e.args[1])     
         finally:
             DBUtil.close_connection(con)
