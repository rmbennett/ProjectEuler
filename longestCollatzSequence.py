
def lengthOfCollatzSequence(value):
	temp = value
	length = 1
	#print temp
	while temp > 1:
		if temp % 2 == 0:
			temp = temp/2
			length+=1
		else:
			temp = (3*temp)+1
			length+=1
	#print length
	return length

def longestCollatzSequence(value):
	longest = 0 
	valueWithLongestSequence = 0 
	for x in range(2,value):
		#print x
		temp = lengthOfCollatzSequence(x)
		if temp > longest:
			longest = temp
			valueWithLongestSequence= x	
	return valueWithLongestSequence


if __name__ == '__main__':
	if not lengthOfCollatzSequence(13) == 10:
		raise AssertionError("Can't calculate length of a Collatz sequence")
	print longestCollatzSequence(1000000)	