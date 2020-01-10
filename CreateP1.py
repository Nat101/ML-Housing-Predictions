

#Natalie Carlson
#Project 1 
#Due 2/10/19
#This program creates a database in mySQL, creates a table in the database, and fills the table with data


import mysql.connector
import csv

#Set up database
mydb = mysql.connector.connect(
	host = "localhost", 
	user = "root", 
	passwd = "12345",
	database = "CAMA") #add database line AFTER running "create database"

#the object that communicates with the mySQL database
cursor = mydb.cursor()

#Create Database
def create_database(cursor):
	cursor.execute("CREATE DATABASE CAMA")  
	#test database creation
	cursor.execute("SHOW DATABASES")
	for d in cursor:
		print(d)

#Create Table
def create_table(cursor):
	cursor.execute("CREATE TABLE Project1 (Deed_Date VARCHAR(20), Taxable_Value INTEGER(20), Year_Built INTEGER(4), Bedrooms INTEGER(5), Full_Baths INTEGER (5), Half_Baths INTEGER(5), Basement_Garages INTEGER(5))")  
	#test table
	cursor.execute("SHOW TABLES")
	for t in cursor:
		print(t)

#Add Data to Table
def add_table(cursor):
	#this guides the addition of data into our table
	sqlFormula = "INSERT INTO Project1 (Deed_Date, Taxable_Value, Year_Built, Bedrooms, Full_Baths, Half_Baths, Basement_Garages) VALUES(%s, %s, %s, %s, %s, %s, %s)"   

	#read in file and add data from desired columns into table
	camaFile = "CAMA_Property_Inventory_-_Residential_with_Details.csv" 
	with open(camaFile) as csv_file:
		data = csv.reader(csv_file, delimiter=',') #seperate values
		rowNum = 0 #track row number
		for d in data:
			if rowNum == 0: #header row
				#print(d[25], d[43], d[54], d[57], d[59], d[60], d[80]) #testing
				rowNum += 1 #increase rowTracker count
			else: #all other rows
				#convert all empty strings to -1 (so we can ignore these values later)
				#if(d[25] == ''):
				#	d[25] == '0/0/00'
				if (d[43] == ''):
					d[43] = -1
				if (d[54] == ''):
					d[54] = -1
				if (d[57] == ''):
					d[557] = -1
				if (d[59] == ''):
					d[59] = -1
				if (d[60] == ''):
					d[60] = -1
				if (d[80] == ''):
					d[80] = -1

				selectedValues = ( d[25], int(d[43]), int(d[54]), int(d[57]), int(d[59]), int(d[60]), int(d[80]) ) #the values we want added to the table
				cursor.execute(sqlFormula, selectedValues) #send into table
				rowNum += 1 #increase rowTracker count
			

	mydb.commit()# finalize data entry

#create_database(cursor)#can only run this code once #RUN CREATE DATABASE, THEN ADD DATABASE TO CONNECTOR AND COMMENT OUT
#create_table(cursor)#can only run this code once #RUN CREATE TABLE, after commenting out create database
#add_table(cursor)#can only run this code once or you will duplicate your data