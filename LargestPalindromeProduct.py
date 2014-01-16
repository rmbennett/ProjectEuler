

def palindromeCheck(n):
	return str(n) == str(n)[::-1]

def somefunction(low, high):
	currentMax = 0
	for value1 in range(low, high):
		for value2 in range(low, high):
			answer = value1 * value2
			if palindromeCheck(answer) and (currentMax < answer): 
				currentMax = answer
	return currentMax




if __name__ == '__main__':

	if not palindromeCheck(9009):
		raise AssertionError("Dude is Palindrome man...")
	if not somefunction(10, 100) == 9009:
		raise AssertionError("somefunction is shit")
	print somefunction(100, 1000)
