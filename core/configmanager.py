import os, ConfigParser
from lurker.core.basefunc import singleton


@singleton
class ConfigManager:
    root_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
    cfg_parser = ConfigParser.ConfigParser()
    cfg_files = []
    DB_SETTINGS = "dbsettings"

    def __init__(self):
        for r,d,f in os.walk(self.root_dir):
            for files in f:
                if files.endswith(".cfg"):
                    print('config file: ' + os.path.join(r, files))
                    self.cfg_files.append(os.path.join(r,files))
        self.cfg_parser.read(self.cfg_files)
      
    def get_config(self, section, key):
        return self.cfg_parser.get(section, key)
    
    def get_db_config(self, key):
        return self.cfg_parser.get(self.DB_SETTINGS, key)
        
   
ConfigManager = singleton(ConfigManager)
        
        
