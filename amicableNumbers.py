

def properDivisors(value):
	temp = 0
	for x in range(1, (value/2)+1):
		if (value % x) == 0:
			temp += x
	return temp

def amicableNumbers(value):
	temp = properDivisors(value)
	if value == properDivisors(temp) and (temp != value):
		return True
	else:
		return False

def sumAmicableNumbers(value):
	amicableSum = 0
	for x in range(1, value):
		if amicableNumbers(x):
			print x 
			amicableSum += x
	return amicableSum


if __name__ == '__main__':
	if not properDivisors(220) == 284:
		raise AssertionError("Failure")
	if not properDivisors(284) == 220:
		raise AssertionError("Failure")
	if not amicableNumbers(220) == True:
		raise AssertionError("Numbers should be Amicable")
	print sumAmicableNumbers(10000)
