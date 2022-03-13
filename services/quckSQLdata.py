# KAMIL MARTENCZUK 13.03.2022
# FULL ACCESS TO DB TABLES VIEWS AND SCALAR FUNCTION
from services.connections import dataSQL

def colNames(Connection, tableName):
    return dataSQL(Connection, "Select COLUMN_NAME, DATA_TYPE from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+tableName+"'").data