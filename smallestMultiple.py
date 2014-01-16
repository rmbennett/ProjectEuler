from time import time

def checkdivisor(low, high):	
	currentValue = 1
	finished = False
	while(not finished): 
		for value in range(low, high+1):
			if not (currentValue % value == 0):
				currentValue += 1
				break							
		else:
			finished = True
			print currentValue
			return currentValue

if __name__ == '__main__':
	if not checkdivisor(1,10) == 2520:
		raise AssertionError("Not Checked")
	start = time()
	print checkdivisor(1, 20)
	finish = time()
	timetaken = finish - start
	print timetaken