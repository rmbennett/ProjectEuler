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

def LargestPrimeFactor(value):
	pg2 = primeGenerator()
	currentValue = value
	currentprime = pg2.next()
	while not primeChecker(currentValue):
		print currentValue
		print currentprime
		primeFactor = float(currentValue)/float(currentprime)
		if not primeFactor % 1:
			currentValue = primeFactor
		else:
			currentprime = pg2.next()
	print int(currentValue)
	return currentValue		


if __name__ == '__main__':
	if not primeChecker(3):
		raise AssertionError("3 is prime")
	if primeChecker(9):
		raise AssertionError("9 is not prime")
	if not primeChecker(29):
		raise AssertionError("11 is prime")
	if primeChecker(28):
		raise AssertionError("28 is not prime")
	pg = primeGenerator()
	listPrimes = [pg.next() for i in range(5)]
	print listPrimes
	if not listPrimes == [2, 3, 5, 7, 11]:
		raise AssertionError("primeGenerator is shit")
	if not LargestPrimeFactor(13195) == 29:
		raise AssertionError("LargestPrimeFactor is shit")
	print LargestPrimeFactor(600851475143)

