import math
from time import time
def primeChecker(value):
	for divisor in range(2, int(math.floor(math.sqrt(value))+1)):
		if value % divisor == 0:
			return False
	return True

def primeSummation(MaxValue):
	total = 0
	for value in range(2, MaxValue):
		if primeChecker(value):
			total += value
	print total
	return total

if __name__ == '__main__':
	if not primeChecker(3):
		raise AssertionError("3 is prime")
	if primeChecker(9):
		raise AssertionError("9 is not prime")
	if not primeChecker(29):
		raise AssertionError("11 is prime")
	if primeChecker(28):
		raise AssertionError("28 is not prime")
	if not primeSummation(10) == 17:
		raise AssertionError("Should be 17")	
	start = time()
	primeSummation(2000000)
	finish = time()
	timetaken = finish - start
	print timetaken