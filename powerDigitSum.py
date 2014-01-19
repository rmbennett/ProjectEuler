

def powerOfTwo(power):
	return 2**power

def sumDigits(value):
	answer = 0
	stringValue = str(value)
	for c in stringValue:
		answer += int(c)
	return answer

def powerDigitSum(value):
	power = 2**value
	answer = 0
	stringValue = str(power)
	for c in stringValue:
		answer += int(c)
	return answer


if __name__ == '__main__':
	if not powerOfTwo(15) == 32768:
		raise AssertionError("Incorrect answer 2^15 is 32768")
	if not powerOfTwo(2) == 4:
		raise AssertionError("Incorrect answer 2^2 is 4")
	if not sumDigits(32768) == 26:
		raise AssertionError("Incorrect answer - should be 26")
	if not powerDigitSum(15) == 26:
		raise AssertionError("Should be 26")	
	print powerDigitSum(1000)	