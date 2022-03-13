# KAMIL MARTENCZUK 13.03.2022
# FULL ACCESS TO DB TABLES VIEWS AND SCALAR FUNCTION

from obj.connections import *
from services.connections import *
from services.randomValues import *
from services.quckSQLdata import *
from services.scalarFunctionUpdate import *
from obj.data import *
from config.sql import *

#------------------------------------- TEST ROWS -----------------------------------
rowsItems = 50

#------------------------ TEST RANDOM ARRAY (INT/DECIMAL/VARCHAR) ------------------
def generateNewRandomValuesArray(rowsItems,colTableNames):
    return R_IDS_DataSets(rowsItems, colTableNames).arraySet

# --------- INSERT DATA TO SQL FROM RANDOM ARRAY AND SCALAR FUNCTION UPDATE --------
def addNewRandomValuesToSQL(SQLconnection,tablepath,tableName,testRandomArray):
    insertRandomValuesToTableSQL(SQLconnection,tablepath,tableName,testRandomArray[0],testRandomArray[1],testRandomArray[2])
    sqlScalarFunction4Update(SQLconnection, tableName)

# -------------- SELECT DATA FROM VIEW WITH UPDATED SCALAR FUNCTION ----------------
def selectSQLData(SQLconnection,viewpath):
    return dataSQL(SQLconnection, "Select * FROM " + viewpath + "").data

#-------------------------------------------------------------------
#------------------------  MAIN & TESTS ----------------------------
#-------------------------------------------------------------------
if __name__ == '__main__':
    #------------- We generate new Array , insert data to SQL and select data from view with scalar function ----------
    testRandomArray = generateNewRandomValuesArray(rowsItems, colTableNames)
    addNewRandomValuesToSQL(SQLConn1,tablepath,tableName,testRandomArray)
    viewData = selectSQLData(SQLConn1, viewpath)

#----- TEST 1 - Return from SCALAR FUNCTION AVG COLUMNS * COLUMN Perc. VS data from Random Array ------------------
    assert len(colTableNames) == len(testRandomArray[0][0])+len(testRandomArray[1][0])+len(testRandomArray[2][0][0])
    assert float(viewData[0][2]) == round([sum(x) for x in testRandomArray[0]][0]/len(testRandomArray[0][0])*round(float(testRandomArray[1][0]),2),2)
    assert float(viewData[2][2]) == round([sum(x) for x in testRandomArray[0]][2] / len(testRandomArray[0][2]) * round(float(testRandomArray[1][2]), 2),2)
    assert float(viewData[4][2]) == round([sum(x) for x in testRandomArray[0]][4] / len(testRandomArray[0][4]) * round(float(testRandomArray[1][4]), 2),2)

    #------------- We add 2 New Columns and generate new Array with new values -----------------
    dataSQL(SQLConn1, "IF NOT EXISTS(SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '"+tableName+"' AND COLUMN_NAME = 'ColTest1') BEGIN ALTER TABLE "+tablepath+" ADD ColTest1 INT NULL, ColTest2 INT NULL END")
    colTableNames = dataSQL(SQLConn1, "Select COLUMN_NAME, DATA_TYPE from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+tableName+"'").data
    testRandomArray = generateNewRandomValuesArray(rowsItems, colTableNames)
    addNewRandomValuesToSQL(SQLConn1,tablepath,tableName,testRandomArray)
    viewData = selectSQLData(SQLConn1, viewpath)

# ----- TEST 2 -  We add 2 New Columns and check one more time another values SCALAR vs Array Data -----------------
    assert len(colTableNames) == len(testRandomArray[0][1]) + len(testRandomArray[1][0]) + len(testRandomArray[2][0][1])
    assert float(viewData[1][2]) == round([sum(x) for x in testRandomArray[0]][1]/len(testRandomArray[0][1])*round(float(testRandomArray[1][1]),2),2)
    assert float(viewData[3][2]) == round([sum(x) for x in testRandomArray[0]][3] / len(testRandomArray[0][3]) * round(float(testRandomArray[1][3]), 2),2)
    assert float(viewData[5][2]) == round([sum(x) for x in testRandomArray[0]][5] / len(testRandomArray[0][5]) * round(float(testRandomArray[1][5]), 2),2)

    #------------- We drop 2 New Columns and generate new Array with new values -----------------
    dataSQL(SQLConn1, "ALTER TABLE " + tablepath + " DROP COLUMN ColTest1, ColTest2")
    colTableNames = dataSQL(SQLConn1, "Select COLUMN_NAME, DATA_TYPE from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+tableName+"'").data
    testRandomArray = generateNewRandomValuesArray(rowsItems, colTableNames)
    addNewRandomValuesToSQL(SQLConn1,tablepath,tableName,testRandomArray)
    viewData = selectSQLData(SQLConn1, viewpath)
