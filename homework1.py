'''
Homework #1 
Analyzer Algorithm
Gwynie Dunlevy
'''
from array import *
import math, random

d = 12
n = 4
inputX = []
inputY = []
q = []
c = []
p = []
h = []
error = [] 
good = 0
sqrt = float(math.sqrt(n))

#getting random 0 and 1's 
for i in range (n):
	random_y = random.randint(0,1)
	inputY.append(random_y)
	x= []
	for j in range(d):
		random_x = random.randint(0,1)
		x.append(random_x)
	inputX.append(x)
print("\n-------input S(x,y)-------")
print ("X: ", str(inputX))
print ("Y: ", str(inputY), "\n")


print("--------q and c-------")
#qj is 1 when x[j] = 1
#qj is 0 otherwise 
for i in range(n):
	qj = [] #qj (x,y)
	for j in range(d):
		if (inputX[i][j] == inputY[i]):
			qj.append(1)
		elif (inputX[i][j] != inputY[i]):
			qj.append(0)
	q.append(qj)
print("q: ", str(q), "\n")
#cj equation and checking to see what is "good" 
for i in range(n):
	#*******COME BACK*******
	equation = float(((1/2)+(1/sqrt)))
	for j in range(d):
		qSum = ([sum(x) for x in zip(*q)]) #getting the summation
		cEquation = float((float((1/n))*qSum[j]))
		c.append(cEquation) #getting the cj

	if (c[i] > equation): #is cj (or in this case ci) greater than (1/2)+(1/math.sqrt(n))
		p.append(1) #append 1 if it is into set p
		good += 1
	else:
		p.append(0) #else append 0 into set p
#print(qSum)
print("c: ", str(c), "\n")


# getting prediction 
print("--------Good q's for set p-------")
print("Good q's: ", good, "\n")
print("Set p: ", p, "\n")

for i in range(n):
	if p[i] >= float((good/2)):
		h.append(1)
	else: 
		h.append(0)
print("--------Prediction-------")
print("Prediction Rule: ", str(h),"\n")



errorCount = 0
for i in range(n):
	if h[i] != inputY[i]:
		error.append(1)
		errorCount +=1
	else:
		error.append(0)

print("--------Errors-------")
print("Errors: ", str(error))
print("How many errors: ", str(float(errorCount)))

#errorCount = 0.0
errorP = float(errorCount/n)
print("Error Percent: ", str(errorP*100), "%")

#error rate decreases as d increases, and increases as k increases 



