#Natalie Carlson
#Project1
#Due 2/10/19
#This program accesses, manipulates, and outputs data from our table


import mysql.connector
import matplotlib
import numpy as np
import matplotlib.pyplot as plt



#Connect to database
mydb = mysql.connector.connect(
	host = "localhost", 
	user = "root", 
	passwd = "12345",
	database = "CAMA") 
#the object that communicates with the mySQL database
cursor = mydb.cursor()


#Mean housing price by year built
cursor.execute("SELECT AVG (Taxable_Value),  Year_Built FROM Project1 WHERE  Taxable_Value>=0 and Year_Built>0 GROUP BY Year_Built ORDER BY Year_Built")
myresult = cursor.fetchall()
meanPrice = []
meanPriceYear = []
for data in myresult:
	meanPrice.append(float(data[0]))
	meanPriceYear.append(data[1])
#Medium housing price by year built	
cursor.execute("SELECT Taxable_Value, Year_Built From Project1 WHERE Taxable_Value>=0 and Year_Built>0 ORDER BY Year_Built, Taxable_Value")
myresult = cursor.fetchall()
medianPrice = []
medianYear = []
for data in myresult:
	medianPrice.append(data[0])
	medianYear.append(data[1])
year = 0
yearIndex = -1
grouped=[[] for i in range(len(medianYear))]
mP=[]
mY=[]
for i in range(len(medianYear)):
	if year!=medianYear[i]:
		yearIndex+=1
		year = medianYear[i]
		mY.append(year)
		grouped[yearIndex].append(medianPrice[i])
	else:
		grouped[yearIndex].append(medianPrice[i])
for i in range (len(grouped)):
	length = len(grouped[i])
	if length != 0:
		medianIndex = length/2
		medianIndex = int(medianIndex)
		mP.append(grouped[i][medianIndex])
#Standard Deviation of housing price by year built
cursor.execute("SELECT  STD(Taxable_Value),  Year_Built FROM Project1 WHERE  Taxable_Value>=0 and Year_Built>0 GROUP BY Year_Built ORDER BY Year_Built")
myresult = cursor.fetchall()
stdPrice = []
stdYear = []
for data in myresult:
	stdPrice.append(float(data[0]))
	stdYear.append(data[1])

#Duration of ownership #CURRENT_DATE, STR_TO_DATE(Deed_Date, '%m/%d/%y'),
cursor.execute("SELECT  DATEDIFF(CURRENT_DATE, STR_TO_DATE(Deed_Date, '%m/%d/%y'))/365, Year_Built FROM Project1 WHERE Deed_Date<>'' and Year_Built>0 ORDER BY Year_Built")
myresult = cursor.fetchall()
duration = []
durationYear = []
for data in myresult:
	if (data[0] >= 0):
		duration.append(float(data[0]))
		durationYear.append(data[1])

#Mean bedroom count by year built
cursor.execute("SELECT AVG(Bedrooms), Year_Built FROM Project1 WHERE  Bedrooms>=0 and Year_Built>0 GROUP BY Year_Built ORDER BY Year_Built")
myresult = cursor.fetchall()
meanBed = []
meanBedYear = []
for data in myresult:
	meanBed.append(float(data[0]))
	meanBedYear.append(data[1])
#Mean bathroom  by year built
cursor.execute("SELECT AVG(Full_Baths+ Half_Baths/2), Year_Built FROM Project1 WHERE  Full_Baths>=0 and Half_Baths>=0  and Year_Built>0 GROUP BY Year_Built ORDER BY Year_Built")
myresult = cursor.fetchall()
meanBath = []
meanBathYear = []
for data in myresult:
	meanBath.append(float(data[0]))
	meanBathYear.append(data[1])
#Mean garage size by year built
cursor.execute("SELECT AVG(Basement_Garages), Year_Built FROM Project1 WHERE Basement_Garages>=0 and Year_Built>0 GROUP BY Year_Built ORDER BY Year_Built")
myresult = cursor.fetchall()
meanGarage = []
meanGarageYear = []
for data in myresult:
	meanGarage.append(float(data[0]))
	meanGarageYear.append(data[1])


#a. Median, mean and standard deviation of housing price by year
plt.title("Mean, Median, and Standard Deviation of Home Prices by Year Built")
plt.plot(meanPriceYear, meanPrice, label='Mean', color = 'r')
plt.plot(mY, mP, label='Medium', color = 'b')
plt.plot(stdYear, stdPrice, label='STD', color = 'g')
plt.legend()
plt.show()

#b. Duration of ownership.
plt.title("Duration of Ownership by Year Built")
plt.scatter(durationYear, duration)
plt.legend()
plt.show()

#c.
plt.title("Mean Bedroom Count, Bath Count, and Garage Size by Year Built ")
plt.plot(meanBedYear, meanBed, label='Bed', color = 'r')
plt.plot(meanBathYear, meanBath, label='Bath', color = 'b')
plt.plot(meanGarageYear, meanGarage, label='Garage', color = 'g')
plt.legend()
plt.show()

mydb.close()

		
		
			
