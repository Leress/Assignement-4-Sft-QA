import math 




# funcitons to determin BMI
def convertFeetToInches(heightFeet):
		newHeightToInches = heightFeet * 12 #convert feet to inches
		return newHeightToInches

def completeHeightToInches(feet, inches):# convert entire height to 
	fullConvert = feet + inches

	return fullConvert

def convertHeightToMetric(height):
	metricHeight = (height * 0.025) # convert height to metric

	return metricHeight

def convertWeightToMetric(weight):# convert weight to metric
	metricWeight = (weight * 0.45)

	return metricWeight

def squareMetricHeight(height):#square height
	squaredResult = (height * height)

	return squaredResult

def getBmiNumber(weight, heightSquared):

	finalBMI = (weight/ heightSquared)

	return finalBMI



	

def tellBMI(heightInFeet, heightInInches, weight):#main function to give BMI result
	
	newHeightFeet = convertFeetToInches(heightInFeet)
	newHeight = completeHeightToInches(newHeightFeet, heightInInches)
	metricHeight = convertHeightToMetric(newHeight)

	convertedHeight = squareMetricHeight(metricHeight)

	covertedWeight = convertWeightToMetric(weight)

	newBMI = getBmiNumber(covertedWeight, convertedHeight)



	if newBMI > 30:
		statement = "Obese"
		
	if newBMI <= 29.9 and newBMI >= 25:
		statement = "Overweight"
		
	if newBMI <=24.9 and newBMI >=18.5:
		statement = "Normal Weight"
		
	if newBMI < 18.5:
		statement = "Underweight"
		

	return statement


#TESTING IF BMI FUNCTIONS WORK// COMPLETE
# if __name__ =='__main__':

# 	feet = float(input('Enter feet of height: '))
# 	inches = float (input('Enter inches of height: '))
# 	pounds = float(input('Enter weight in pounds: '))

# 	resultant = tellBMI(feet, inches, pounds)

# 	print(resultant)


#functions for Distance Formula

def  subtractXValues(Xpoint1, Xpoint2): #subtract X values
	subXValue = (Xpoint2 - Xpoint1)
	return subXValue

def subtractYValues(Ypoint1, Ypoint2): #subtract Y Values
	subYValue = (Ypoint2 - Ypoint1)
	return subYValue

def squareXValue(Xvalue): #square X Values
	squaredXValue = (Xvalue * Xvalue)
	return squaredXValue

def squareYValue(Yvalue): #sqaure Y Values
	squaredYValue = (Yvalue * Yvalue)
	return squaredYValue

def addValue(Xsquared, Ysquared): #add squared values together
	totalValue = (Xsquared + Ysquared)
	return totalValue

def getDistance(totalBeforeSquaring): #get square root of distance
	distance = math.sqrt(totalBeforeSquaring)
	return distance


def distanceFormula(X1,Y1,X2,Y2): # aggrate functions to perform distance formula
	firstParthesis = subtractXValues(X1, X2)
	secondParthesis = subtractYValues(Y1,Y2)
	squareFirstParthesis = squareXValue(firstParthesis)
	squareSecondParthesis = squareYValue(secondParthesis)
	totalValues = addValue(squareFirstParthesis, squareSecondParthesis)
	finalDistance = getDistance(totalValues) 

	return finalDistance

#TESTING DISTANCE FORMULA// COMPELETE
	
# if __name__ =='__main__':

# 	X1 = int (input('Enter X coordinate of First point: '))
# 	Y1 = int (input('Enter Y coordinate of First point: '))
# 	X2 = int(input('Enter X coordinate of Second point: '))
# 	Y2 = int (input('Enter Y coordinate of Second point: '))

# 	resultant = distanceFormula(X1, Y1, X2, Y2)

# 	print(resultant)


#Functions for Retirement

def covertPercentage(amount, percentage):
	newAmount = amount * percentage

	return newAmount


def matchedSavings(amount):

	savingsMatch = amount + amount

	return savingsMatch

def increaseAge(age):

	newAge = age + 1

	return newAge

def totalSavingsAmount(myPart, employerPart):

	totalPart = myPart + employerPart

	return totalPart



def getRetirement (startAge,salary,percentage,goal):


	totalSavings = 0

	finalAge = startAge


	while (totalSavings < goal) :

		 myPercentage = covertPercentage(salary, percentage)
		 employerMatch = matchedSavings(myPercentage)
		 totalSavings = totalSavings + totalSavingsAmount(myPercentage, employerMatch)
		 finalAge = increaseAge(finalAge)

		 if (finalAge >= 100):
		 	print ('Goal not met')
		 	break





	print ('Goal met by age ' + str(finalAge) )


	return


# if __name__ =='__main__':

# 	userAge = int (input('Enter your current age: '))
# 	userAnnualSalary = float (input('Enter annual salary: $'))
# 	userPercentage = float(input('Enter percentage saved (as a decimal percentage): '))
# 	userGoal = float(input('Enter desired retirment savings goal: $'))

# 	getRetirement(userAge,userAnnualSalary,userPercentage,userGoal)

	


#functions for Email Verifier

def parseOutAtSymbolInString(string):

	parsed = string.split('@')

	return parsed

def parseOutDotSymbolInString(string):

	parsed = string.split('.')

	return parsed

def verfiyString(string):

	if ( len(string) <= 3):

		validation = "Valid Email"

	else:
		validation = "Invalid Email"

	return validation



# if __name__ =='__main__': #testing email validation

# 	enteredEmail = str(input('Enter e-mail to be verified: '))
# 	testem = parseOutAtSymbolInString(enteredEmail)
# 	testem2 = parseOutDotSymbolInString(testem[1])
# 	testem3 = verfiyString(testem2[1])


# 	print(testem3)
	
