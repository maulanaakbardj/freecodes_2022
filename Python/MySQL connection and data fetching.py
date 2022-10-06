import pandas as pd
import mysql.connector as sqltor
hostname = input("Enter Host name : ")
username = input("Enter User name : ")
password = input("Enter MySQL password : ")
databasename = input("Enter database name : ")
mycon = sqltor.connect(host=hostname, user=username, passwd=password, database=databasename)
if mycon.is_connected():
	print("Succesfully Connected")
	query = input("Enter MySQL fetching query in SQL format : ")
	df1 = pd.read_sql(query,  mycon)
	print(df1)
else:
	print("MySQL Not Connected, Try Again by checking information entered...")
