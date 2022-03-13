# KAMIL MARTENCZUK 13.03.2022
# FULL ACCESS TO DB TABLES VIEWS AND SCALAR FUNCTION
from services.connections import dataSQL

def view_test_update(SQLConnection):
	query = "CREATE VIEW [pysql-demo-app].[View_Test] AS SELECT ROW_NUMBER() OVER (ORDER BY TestNo ASC) AS [Id], *, [pysql-demo-app].[scalarFunction1Test]((row_Number() OVER (ORDER BY TESTNo ASC)), 'EU', 'US') AS [RegTest], [pysql-demo-app].[scalarFunction2Test]('Table_Test') AS [INT], [pysql-demo-app].[scalarFunction3Test]('Table_Test') AS [DEC] FROM [DEMO.PYSQL].[pysql-demo-app].[Table_Test]"
	dataSQL(SQLConnection, query)

def view_scalar_update(SQLConnection, colIntNames):
	dataSQL(SQLConnection, "DROP VIEW IF EXISTS [pysql-demo-app].[View_Test_SCALAR]")
	colInt_str = colIntNames[0]
	for x in colIntNames:
		if colIntNames.index(x)>0: colInt_str += ", " + x
	query = "CREATE VIEW [pysql-demo-app].[View_Test_SCALAR] AS SELECT [RegTest], [id], [pysql-demo-app].[scalarFunction4Test]((SELECT COUNT( *) FROM INFORMATION_SCHEMA.COLUMNS WHERE (DATA_TYPE = 'int' AND TABLE_NAME = 'Table_Test')), (ROW_NUMBER() OVER (ORDER BY[id]))) AS scalar, "+ colInt_str +",[Perc] FROM[pysql-demo-app].[View_Test]"
	dataSQL(SQLConnection, query)

def sqlScalarFunction4Update(SQLConnection, tableName):
	colNames = dataSQL(SQLConnection, "Select COLUMN_NAME, DATA_TYPE from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+tableName+"'").data
	colIntNames = [x[0] for x in colNames if x[1]=='int']
	colDecimalNames = [x[0] for x in colNames if x[1] == 'decimal']
	colIntStr = "@"+colIntNames[0]
	for x in colIntNames:
		if colIntNames.index(x)>0: colIntStr+="+@"+x
	colDecimalStr = colDecimalNames[0]
	for x in colDecimalNames:
		if colDecimalNames.index(x)>0: colDecimalStr+="+"+ x
	colIntCount=len(colIntNames)
	colDecimalCount= len(colDecimalNames)
	declaration_arr = ["@"+ x +" AS INT " for x in colIntNames]
	declaration_str = declaration_arr[0]
	set_str = ""
	for x in declaration_arr:
		if declaration_arr.index(x) > 0: declaration_str += ", " + x
	for x in colIntNames:
		set_str +="SET @" + x + "=(SELECT[" + x + "] from [pysql-demo-app].[View_Test] WHERE[id]=@rowNum) "
	query_str = "ALTER FUNCTION [pysql-demo-app].[scalarFunction4Test](@INTNum AS INT, @rowNum AS INT) " \
				"RETURNS DECIMAL(10,2) " \
				"BEGIN DECLARE @RESULT AS DECIMAL(10,2), @valP As DECIMAL(10,2), " + declaration_str + "; " + set_str +"SET @valP=(SELECT [Perc] from [pysql-demo-app].[View_Test] WHERE [id]= @rowNum)" \
																													   "SELECT @RESULT = CAST(CAST(("+colIntStr+") AS DECIMAL(10,2)) / CAST(" + str(colIntCount) + " AS DECIMAL(10,2))* CAST(@valP AS DECIMAL(10,2)) AS DECIMAL(10,2)) RETURN @RESULT END"
	dataSQL(SQLConnection, query_str)
	dataSQL(SQLConnection, "DROP VIEW IF EXISTS [pysql-demo-app].[View_Test]")
	view_test_update(SQLConnection)
	view_scalar_update(SQLConnection,colIntNames)