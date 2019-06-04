import connections
import operations

def main():
	#Python MySql CRUD Operations
	
	#connect to DB 
	mydb=connections.connection("localhost","root","admin")
	myCursor=connections.cursor(mydb)
	
	#create DB
	operations.createDatabase(myCursor,"Employees")
	
	#create table 
	operations.createTable(myCursor,"Employees","EmployeesMaster",id="VARCHAR(255)",name="VARCHAR(255)",phone="VARCHAR(255)")

	#Insert table 
	operations.insertInTable(myCursor,"Employees","EmployeesMaster",id="1",name="TheRock",phone="+016 3334454")
	
	#Select table 
	operations.getTable(myCursor,"Employees","EmployeesMaster")
	
	#Insert table 
	operations.insertInTable(myCursor,"Employees","EmployeesMaster","2","JohnCena","+016 4444454")
	
	#Select table 
	operations.getTable(myCursor,"Employees","EmployeesMaster")
	
	#Select table with condition 
	operations.getTableWithParam(myCursor,"Employees","EmployeesMaster",id="1")
	
	#Select table with condition 
	operations.getTableWithParam(myCursor,"Employees","EmployeesMaster",id="1",name="\"TheRock\"")
	
	#Update table with condition
	operations.updateTable(myCursor,"Employees","EmployeesMaster",{"id":"1"},id="3",name="\"Spiderman\"")
	
	#Select table with condition 
	operations.getTableWithParam(myCursor,"Employees","EmployeesMaster",id="3")
	
	#Delete table 
	operations.deleteTable(myCursor,"Employees","EmployeesMaster")
	
	#Delete DB
	operations.deleteDatabase(myCursor,"Employees")
  
if __name__== "__main__":
  main()