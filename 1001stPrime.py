import math
from time import time

def primeChecker(value):
	for divisor in range(2, int(math.floor(math.sqrt(value))+1)):
		if value % divisor == 0:
			return False
	return True

def nthPrime(nthValue):
	prime = 0
	currentValue = 0
	for value in range(1, 9999999):
		if primeChecker(value):
			prime = value
			currentValue+=1
			print currentValue
			if nthValue == currentValue-1 :
				print "This is the nth prime ", prime 
	 			return prime

	



if __name__ == '__main__':
	if not nthPrime(6) == 13:
		raise AssertionError("Fail")
	start = time()
	print nthPrime(10001)
	finish = time()
	timetaken = finish - start
	print timetaken
