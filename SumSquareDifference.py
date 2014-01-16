import math

def  NumberSquarer(value):
	return value**2

def NumberSummer(currentTotal, newValue):	
	return currentTotal + newValue

def SumSquareNatural(nthValue):
	total = 0
	for value in range(1, nthValue+1):
		total += NumberSquarer(value)
	#print total
	return total

def SquareSumNatural(nthValue):
	total = 0
	for value in range(1, nthValue+1):
		total += value
	total  = total**2
	#print total
	return total

def SumSquareDifference(nthValue):
	return SquareSumNatural(nthValue) - SumSquareNatural(nthValue)


if __name__ == '__main__':
	if not (SumSquareNatural(10) == 385):
		raise AssertionError("Do you even SumSquareNatural, Bro?")
	if not (SquareSumNatural(10) == 3025):
		raise AssertionError("Do you even SquareSumNatural, Bro?")
	if not (SumSquareDifference(10) == 2640):
		raise AssertionError("Do you even SumSquareDifference, Bro?")
	answer = SumSquareDifference(100)
	print answer