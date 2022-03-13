# KAMIL MARTENCZUK 13.03.2022
# FULL ACCESS TO DB TABLES VIEWS AND SCALAR FUNCTION

from services.quckSQLdata import *
from obj.connections import *

schemaName = 'pysql-demo-app'
tableName = 'Table_Test'
viewName = 'View_Test_SCALAR'
tablepath = '['+schemaName+'].['+tableName+']'
viewpath = '['+schemaName+'].['+viewName+']'
colTableNames = colNames(SQLConn1, tableName)