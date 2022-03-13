# KAMIL MARTENCZUK 13.03.2022
# FULL ACCESS TO DB TABLES VIEWS AND SCALAR FUNCTION
import json
import pypyodbc
import csv

class JSONFile:
    def __init__(self, path, name):
        self.filepath = path
        self.filename = name
        self.data = json.load(open(self.filepath + '/' + self.filename + '.json'))

class CSVFile:
    def __init__(self, path, name, delimiter):
        self.filepath = path
        self.filename = name
        self.delim = delimiter
        with open(self.filepath + '/' + self.fileName + '.csv', mode='r') as sourcefile:
            self.data = csv.reader(sourcefile, delimiter=self.delim)

class SQLConn:
    def __init__(self, configFile: JSONFile) -> object:
        self.drivers = configFile.data['drivers']
        self.server = configFile.data['server']
        self.port = configFile.data['port']
        self.user = configFile.data['user']
        self.password = configFile.data['password']
        self.database = configFile.data['database']
        self.trustmode = configFile.data['Trusted_Connection']
        self.conn = pypyodbc.connect('DRIVER={' + self.drivers + '};SERVER='+ self.server +';UID='+ self.user +';PWD='+ self.password +';DATABASE='+ self.database +';Trusted_Connection='+ self.trustmode +';')

class RandomSQL3TypeDataSets:
    def __init__(self, firstTypeData, secondTypeData, ThirdTypeData):
        self.intDataSet = firstTypeData
        self.decimalDataSet = secondTypeData
        self.stringDataSet = ThirdTypeData
        self.dataArraySet = [self.intDataSet, self.decimalDataSet, self.stringDataSet]