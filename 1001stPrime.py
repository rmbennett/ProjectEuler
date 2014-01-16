

def primeChecker(value):
	for divisor in range(2, int(math.floor(math.sqrt(value))+1)):
		if value % divisor == 0:
			return False
	return True

def nthPrime(nthValue):
	prime = 0
	currentValue = 0
	for value in range(1, 999999999):
		if primeChecker(value):
			prime = primeChecker(value)
			currentValue+=1
			print currentValue
			if nthValue == currentValue :
	 			return prime;

	



if __name__ == '__main__':
	main()