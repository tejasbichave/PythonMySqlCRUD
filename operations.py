import sys



"""
Name:createDatabase
Description: This method creates Database
Parameters: 
	myCursor: Name of Cursor
	databaseName: Database name
"""
def createDatabase(myCursor,databaseName):
	try:
		print("CMD: creating database\n")
		myCursor.execute("CREATE DATABASE "+str(databaseName))
		print("RESULT: database created successfully\n")
	except:
		print("RESULT: Error in creating Database")




"""
Name:deleteDatabase
Description: This method deletes Database
Parameters: 
	myCursor: Name of Cursor
	databaseName: Database name
"""
def deleteDatabase(myCursor,databaseName):
	try:
		print("\n\nCMD: drop database\n")
		print("Query: DROP DATABASE "+str(databaseName)+" ;")
		myCursor.execute("DROP DATABASE "+str(databaseName)+" ;")
		print("RESULT: database droped successfully\n")
	except:
		print("RESULT: Error in droping Database")




"""
Name:showTables
Description: This method prints table in Database
Parameters: 
	myCursor: Name of Cursor
"""
def showTables(myCursor):
	try:
		print("\n\nCMD: Show Tables\n")
		print("Query: SHOW TABLES;")
		myCursor.execute("SHOW TABLES;")
	except:
		print("RESULT: Error in droping Database")



"""
Name:createTable
Description: This method creates table in Database
Parameters: 
	myCursor: Name of Cursor
	databaseName: Database names
	table: Table names
	columnWithKeyValue: Column name and type
"""
def createTable(myCursor,databaseName,table,**columnWithKeyValue):
	try:
		print("\n\nCMD: create Table\n")
		values = None
		query = "CREATE TABLE IF NOT EXISTS %s " % table
		if columnWithKeyValue:
			keys = columnWithKeyValue.keys()

			my_list=[]
			for key, value in columnWithKeyValue.items(): 
				my_list.append("%s %s" %(key, value)) 
			s = [str(i) for i in my_list] 
			res = (",".join(s)) 
			query+="("+res+");"
			print("Query: "+str(query))
			myCursor.execute("USE "+str(databaseName)+";")
			myCursor.execute(query)
	except Exception as e:
		print("RESULT: Error in creating Tables\n"+str(sys.exc_info()[-1].tb_lineno))




"""
Name:insertInTable
Description: This method insert data in  table in Database
Parameters: 
	myCursor: Name of Cursor
	databaseName: Database names
	table: Table names
	columns: only default column
	columnWithKeyValue: Column name and type
"""		
def insertInTable(myCursor,databaseName,table,*columns,**columnWithKeyValue):
	try:
		
		values = None
		query = "INSERT INTO "+databaseName+"."+table+" "
		if columnWithKeyValue:
			print("\n\nCMD: Insert data in Table in Key Value style\n")
			keys = columnWithKeyValue.keys()
			values = tuple(columnWithKeyValue.values())
			query += "(" + ",".join(["`%s`"] * len(keys)) %  tuple (keys) + ") VALUES " + str(values)  + ""
		elif columns:
			print("\n\nCMD: Insert data in Table in only Value style\n")
			values = columns
			query += " VALUES" + str(columns) + ";"
		print("Query 1: USE "+str(databaseName)+";")
		print("Query 2: "+str(query))
		myCursor.execute("USE "+str(databaseName)+";")
		rows_affected=myCursor.execute(query)
		print("ROW Affected: "+str(rows_affected))
	except:
		print("RESULT: Error in creating Tables\n"+str(sys.exc_info()[-1].tb_lineno))




"""
Name:deleteTable
Description: This method delete   table in Database
Parameters: 
	myCursor: Name of Cursor
	databaseName: Database names
	table: Table names
"""		
def deleteTable(myCursor,databaseName,table):
	try:
		print("\n\nCMD: deleteTable\n")
		print("Query: DROP TABLE "+str(databaseName)+"."+str(table)+" ;")
		myCursor.execute("DROP TABLE "+str(databaseName)+"."+str(table)+" ;")
		print("RESULT: Table droped successfully\n")
	except:
		print("RESULT: Error in droping Database")





"""
Name:getTable
Description: This method select all data from table
Parameters: 
	myCursor: Name of Cursor
	databaseName: Database names
	table: Table names
"""		
def getTable(myCursor,databaseName,table):
	try:
		print("\n\nCMD: Select * from Table\n")
		values = None
		query = "SELECT * FROM "+databaseName+"."+table+" ;"
		rows_affected=myCursor.execute(query)
		myresult = myCursor.fetchall()
		for x in myresult:
			print(x)
	except:
		print("RESULT: Error in getting Tables\n"+str(sys.exc_info()[-1].tb_lineno))



"""
Name:getTableWithParam
Description: This method select Specific  data from table
Parameters: 
	myCursor: Name of Cursor
	databaseName: Database names
	table: Table names
	conditons: condition with key and value pair
"""		
def getTableWithParam(myCursor,databaseName,table,**conditons):
	try:
		print("\n\nCMD: Select Table with condition\n")
		values = None
		query = "SELECT * FROM %s WHERE " % table
		if conditons:
			keys = conditons.keys()

			my_list=[]
			for key, value in conditons.items(): 
				my_list.append("%s=%s" %(key, value)) 
			s = [str(i) for i in my_list] 
			res = (" AND ".join(s)) 
			query+="("+res+");"
			print("Query: "+str(query))
			myCursor.execute("USE "+str(databaseName)+";")
			myCursor.execute(query)
			myresult = myCursor.fetchall()
			for x in myresult:
				print(x)
	except Exception as e:
		print("RESULT: Error in creating Tables\n"+str(sys.exc_info()[-1].tb_lineno))




"""
Name:updateTable
Description: This method modify Specific  data from table
Parameters: 
	myCursor: Name of Cursor
	databaseName: Database names
	table: Table names
	where: condition 
	newData: newData with key and value pair
"""			
def updateTable(myCursor,databaseName,table,where=None,**newData):
	try:
		print("\n\nCMD: updateTable\n")
		values = None
		query = "UPDATE %s SET " % table
		if newData:
			keys = newData.keys()

			my_list=[]
			for key, value in newData.items(): 
				my_list.append("%s=%s" %(key, value)) 
			s = [str(i) for i in my_list] 
			res = (" , ".join(s)) 
			condition=str(getWhereClause(where))
			if(condition=="None"):
				query+=""+res+";"
			else:
				query+=""+res+""
				query += " WHERE "+str(getWhereClause(where))+" ;" 
			print("Query: "+str(query))
			myCursor.execute("USE "+str(databaseName)+";")
			myCursor.execute(query)
			myresult = myCursor.fetchall()
			for x in myresult:
				print(x)
	except Exception as e:
		print("RESULT: Error in creating Tables\n"+str(sys.exc_info()[-1].tb_lineno))

def getWhereClause(where):
	try:
		if (where):
			my_list=[]
			for key, value in where.items(): 
				my_list.append("%s=%s" %(key, value)) 
			s = [str(i) for i in my_list] 
			res = (" , ".join(s)) 
			return ""+res+";"
		else :
			return None
	except Exception as e:
		print("RESULT: Error in creating Tables\n"+str(sys.exc_info()[-1].tb_lineno))