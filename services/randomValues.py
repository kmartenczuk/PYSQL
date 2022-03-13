# KAMIL MARTENCZUK 13.03.2022
# FULL ACCESS TO DB TABLES VIEWS AND SCALAR FUNCTION
import numpy as np
from services.scalarFunctionUpdate import *

class randArray:
    def __init__(self, mode, type, itemsX, itemsY=0, min=0, max=0):
        if mode == '1D':
            if type!='int': self.array = np.random.rand(itemsX)
            elif type == 'int': self.array = np.random.randint(min, max, size = (itemsX))
        elif mode == '2D':
            if type != 'int':
                self.array = np.random.rand(itemsX,itemsY)
            elif type == 'int':
                self.array = np.random.randint(min, max, size = (itemsX, itemsY))

def insertRandomValuesToTableSQL(connection, path, tableName, randomIntValuesArr, randomDecimalValuesArr, stringSampleArr):
    dataSQL(connection, "DROP VIEW IF EXISTS [pysql-demo-app].[View_Test]")
    rowsItems = len(randomIntValuesArr)
    collNames = dataSQL(connection, "Select COLUMN_NAME, DATA_TYPE from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+tableName+"'").data
    dataSQL(connection,"Truncate Table " + path)
    collNamesStrArr = str(collNames[0][0])
    for x in collNames:
        if collNames.index(x)>0: collNamesStrArr+=","+x[0]
    values_arr = [0 for i in collNames]
    indexString=0
    for i in range(rowsItems):
        indexInt = 0
        indexDecimal = 0
        for x in collNames:
            if x[1]=='int':
                values_arr[collNames.index(x)]=randomIntValuesArr[i][indexInt]
                indexInt += 1
            if x[1]=='decimal':
                values_arr[collNames.index(x)]=randomDecimalValuesArr[i][indexDecimal]
                indexDecimal += 1
            if x[1]=='nvarchar':
                values_arr[collNames.index(x)]=stringSampleArr[indexString]
                indexString += 1
        values_str = "'"+str(values_arr[0])+"'"
        for x in values_arr:
            if values_arr.index(x) > 0: values_str += ",'" + str(x)+"'"
        dataSQL(connection,"Insert INTO " + path + " (" + collNamesStrArr + ") VALUES ("+values_str+")")
    view_test_update(connection)
