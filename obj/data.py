# KAMIL MARTENCZUK 13.03.2022
# FULL ACCESS TO DB TABLES VIEWS AND SCALAR FUNCTION
from services.randomValues import randArray

class R_IDS_DataSets:
    def __init__(self, rowsItems, colsNameTypeArray):
        self.intArray = randArray('2D', "int", rowsItems, len([x for x in colsNameTypeArray if colsNameTypeArray[colsNameTypeArray.index(x)][1] == 'int']), 1, 50).array,
        self.decimalArray = randArray('2D', "decimal", rowsItems, len([x for x in colsNameTypeArray if colsNameTypeArray[colsNameTypeArray.index(x)][1] == 'decimal']), 1,50).array,
        self.textArray = ['Test' + '0' + str(x + 1) if x < 9 else 'Test' + str(x + 1) for x in range(len(['Test' for i in range(rowsItems) for x in colsNameTypeArray if colsNameTypeArray[colsNameTypeArray.index(x)][1] == 'nvarchar']))]
        self.arraySet = [0 for i in range(3)]
        self.arraySet[0]=self.intArray[0]
        self.arraySet[1] = self.decimalArray[0]
        self.arraySet[2] = self.textArray

