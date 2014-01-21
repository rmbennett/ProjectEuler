

def selfPowerSum(value):
	answer = 0
	for x in range(1, value+1):		
		answer += x**x
	return answer

if __name__ == '__main__':
	if not selfPowerSum(10) == 10405071317:
		raise AssertionError("Wrong Answer")
	print selfPowerSum(1000)