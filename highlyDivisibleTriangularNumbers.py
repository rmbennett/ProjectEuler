import math


def primeChecker(value):
	for divisor in range(2, int(math.floor(math.sqrt(value))+1)):
		if value % divisor == 0:
			return False
	return True

def primeGenerator():
	candidatePrime = 3
	yield 2
	while True:
		if primeChecker(candidatePrime):
			yield candidatePrime
		candidatePrime+=2

def numDivisors(value):
	currentValue = value
	y = 0
	z = {}
	#pg = primeGenerator()
	#prime = pg.next()
	prime = 2
	numDivisors = 1
	while currentValue > 1 :
		if (currentValue % prime == 0):
			currentValue = currentValue/prime
			if not y in z:
				z[y] = 1
			else:
				z[y] += 1
		else:
			prime = prime+1
			y +=1
	for key in z:
		numDivisors *= (z[key]+1)
	return numDivisors

def overXDivisors(value):
	triangleNumber = 0
	finished = False
	x=1
	while not finished:
		triangleNumber += x
		if numDivisors(triangleNumber) > value:
			finished = True
		else:
			x+=1
	#print triangleNumber
	return triangleNumber

if __name__ == '__main__':
	if not overXDivisors(5) == 28:
		raise AssertionError("28 is the first triangle number with over 5 factors")
	print numDivisors(6552)
	print overXDivisors(500)
