import math

def factorialDigitSum(base):
	temp = 0
	answer = math.factorial(base)
	for c in str(answer):
		temp += int(c)
	return temp

if __name__ == '__main__':
	if not math.factorial(10) == 3628800:
		raise AssertionError("Factorial does not return correctly")
	if not factorialDigitSum(10) == 27:
		raise AssertionError("factorial digit Sum Does not work")
	print factorialDigitSum(100)