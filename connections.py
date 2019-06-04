#import mysql.connector
import pymysql as MySQLdb

def connection(host,username,password):
	try:
		mydb = MySQLdb.connect(host,username,password)
		return mydb
	except:
		print("Error in connection Database")
  
	
def cursor(mydb):
	myCursor = mydb.cursor()
	return myCursor
	
def close(mydb):
	mydb.close()