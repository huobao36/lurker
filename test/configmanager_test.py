import unittest
from lurker.core.configmanager import ConfigManager
import ConfigParser


class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_getdbconfig(self):
        print 'user: ' + ConfigManager().get_db_config("user")
        print 'host: ' + ConfigManager().get_db_config('host') 
        print 'passwd: ' + ConfigManager().get_db_config('passwd') 

    def test_getconfig(self):
        print ConfigManager().get_config('settings', 'default')

if __name__ == '__main__':
    unittest.main()
        
   
