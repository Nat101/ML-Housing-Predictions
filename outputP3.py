#Natalie Carlson
#Project 3 
#Due 4/25/19
#This program accesses, manipulates, and outputs data from our table

import random
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt
from statistics import mean 
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score 



def formulateValidation(d):		
	#change the degree of the data sets
	poly = PolynomialFeatures(degree = d)
	xTrain_poly = poly.fit_transform(xTrain) 
	xValidate_poly = poly.fit_transform(xValidate)
	xFuture_poly = poly.fit_transform(xFuture)
	#create the model regression object
	model = linear_model.LinearRegression()
	#train model
	model.fit(xTrain_poly, yTrain)
	#make predictions based on validation set
	yPredict = model.predict(xValidate_poly)
	#Forecast
	yFuturePredict = model.predict(xFuture_poly)
	
	#measurements
	#error performance
	loss = mean_squared_error(yValidate, yPredict) 
	#variance
	score = r2_score(yValidate, yPredict)
	print("Mean squared error for degree ", degree, ': ', loss, "  Variance score for degree ", degree, ': ', score)
	
	#Output predictions
	print("Forecasted number of homes per year:")
	xF = []
	for i in range(len(xFuture)):
		print(int(xFuture[i][0]), ' ', yFuturePredict[i])
		xF.append(int(xFuture[i][0]))
	#graph
	r = random.uniform(0,1)
	g = random.uniform(0,1)
	b = random.uniform(0,1)
	randColor = [r,g,b]
	plt.plot(xValidate['Year'], yPredict, label=("Degree " + str(degree)), color=randColor)
	plt.plot(xF, yFuturePredict, color=randColor)
	return[(loss/1000000), score]

def formulateTest(d):		
	#change the degree of the data sets
	poly = PolynomialFeatures(degree = d)
	xTrain_poly = poly.fit_transform(xTrain) 
	xTest_poly = poly.fit_transform(xTest)
	xFuture_poly = poly.fit_transform(xFuture)
	#create the model regression object
	model = linear_model.LinearRegression()
	#train model
	model.fit(xTrain_poly, yTrain)
	#make predictions based on validation set
	yPredict = model.predict(xTest_poly)
	#Forecast
	yFuturePredict = model.predict(xFuture_poly)
	
	#measurements
	#error performance
	loss = mean_squared_error(yTest, yPredict)
	#variance
	score = r2_score(yTest, yPredict)
	print("Mean squared error for degree ", degree, ': ', loss, "  Variance score for degree ", degree, ': ', score)
	#Output predictions
	xF=[]
	print("Forecasted number of homes per year:")
	for i in range(len(xFuture)):
		print(int(xFuture[i][0]), ' ', yFuturePredict[i])
		xF.append(int(xFuture[i][0]))

	#graph
	r = random.uniform(0,1)
	g = random.uniform(0,1)
	b = random.uniform(0,1)
	randColor = [r,g,b]
	plt.plot(xTest['Year'], yPredict, label=("Degree " + str(degree)), color=randColor)
	plt.plot(xF, yFuturePredict, color=randColor)
	return[(loss/1000000), score]


################################
#	Main
################################
#import data
dataset = pd.read_csv('/Users/nataliecarlson/Desktop/UAA/415_ML/Project3/CarlsonN_P3/project3.csv')
features = dataset[['Year', 'Unemployment Rate', 'Materials Inflation Rate', 'Mortgage Interest Rate']]
houseCount = dataset['House Count']

ueMean = mean(dataset['Unemployment Rate'])
matMean = mean(dataset['Materials Inflation Rate'])
mortMean = mean(dataset['Mortgage Interest Rate'])

#split data into three sets
xTrain = features[0::3]
yTrain = houseCount[0::3]
xValidate = features[1::3]
yValidate = houseCount[1::3]
xTest = features[2::3]
yTest = houseCount[2::3]

#generate x for future years and convert to numpy array
xFuture = []
for i in range(2019,2029):
	xFuture.append([i, ueMean, matMean, mortMean])
xFuture = np.array(xFuture)
lossList = []
scoreList = []
degreeList = []


###############################################################
#		Comparisons of sets
###############################################################
#error performance
loss1 = mean_squared_error(yTrain, yValidate)
loss2 = mean_squared_error(yTrain, yTest) 	
#variance
score1 = r2_score(yTrain, yValidate)
score2 = r2_score(yTrain, yTest) 

#Sets Graph
plt.title("Houses built per year")
plt.plot(features['Year'], houseCount, label="Full data set", color='grey')
plt.scatter(xTrain['Year'], yTrain, label="Train Set", color='black', s=15)
plt.scatter(xValidate['Year'], yValidate, label="Validation Set", color='blue', s=15)
plt.scatter(xTest['Year'], yTest, label="Test Set", color= 'cyan', s=15)
plt.xticks(np.arange(1945, 2035,5))
plt.yticks(np.arange(0, 20500, 500))
plt.legend()
plt.show()
#Measurement comparisons graph
plt.title("Mean squared error and variance performance\nof Validation and Test sets against Training set ")
ind = np.arange(2)
width = 0.35
p1 = plt.bar(ind, (loss1/1000000, loss2/1000000), width)
p2 = plt.bar(ind, (score1, score2), width)
plt.xticks(ind, ('Validation Set', 'Test Set'))
plt.ylim(0,11)
plt.yticks(np.arange(0, 10, 1))
plt.legend((p1[0], p2[0]), ('Loss/1000000', 'Variance'))
plt.show()		


###############################################################
#		Model training with Validation set
###############################################################
print("Validation set against training set:")
for i in range(1, 4, 1):
	degree = i
	trial = formulateValidation(degree)	
	lossList.append(trial[0])
	scoreList.append(trial[1])
	degreeList.append('degree ' + str(degree))
#for i in range(5, 21, 5):
#	degree = i
#	trial = formulateValidation(degree)	
#	lossList.append(trial[0])
#	scoreList.append(trial[1])
#	dstring = 'degree ' + str(degree)
#	degreeList.append(dstring)
#Validation graph
plt.title("Houses built per year\nValidation set against training set")
plt.scatter(xTrain['Year'], yTrain, label="Train Set", color='black', s=15)
plt.scatter(xValidate['Year'], yValidate, label="Validation Set", color='blue', s=15)
plt.xticks(np.arange(1945, 2035,5))
plt.ylim(-1000,21000)
plt.yticks(np.arange(0, 20500, 500))
plt.legend()
plt.show()
###############################################################
#		Model training with Test set
###############################################################

print("\nTest set against training set:")
degree = 1
trial = formulateTest(degree)	
lossList.append(trial[0])
scoreList.append(trial[1])
degreeList.append('Test set\ndegree ' + str(degree))

#Test Graph
plt.title("Houses built per year\nTest set against training set")
plt.scatter(xTrain['Year'], yTrain, label="Train Set", color='black', s=15)
plt.scatter(xTest['Year'], yTest, label="Test Set", color= 'cyan', s=15)
plt.xticks(np.arange(1945, 2035,5))
plt.ylim(-1000,21000)
plt.yticks(np.arange(0, 20500, 500))
plt.legend()
plt.show()

#######################################################
# Algorithm performance of all models
######################################################
#Measurement comparisons graph
plt.title("Mean squared error and variance performance")

ind = np.arange(len(lossList))
width = 0.35
p1 = plt.bar(ind, tuple(lossList), width)
p2 = plt.bar(ind, tuple(scoreList), width)
plt.xticks(ind, tuple(degreeList))
plt.ylim(0,11)
plt.yticks(np.arange(0, 10, 1))
plt.legend((p1[0], p2[0]), ('Loss/1000000', 'Variance'))
plt.show()




