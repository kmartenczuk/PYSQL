# KAMIL MARTENCZUK 13.03.2022
# FULL ACCESS TO DB TABLES VIEWS AND SCALAR FUNCTION
from obj.init import JSONFile
from obj.init import SQLConn

#   SQL Connection Config
SQLConn1 = SQLConn(JSONFile('config', 'sql')).conn


