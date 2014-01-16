#http://mathforum.org/library/drmath/view/55811.html

def pythagTripleCheck(a, b, c):
	if a**2 + b**2 == c**2:
		#print "New Triple"
		#print a
		#print b
		#print c
 		return True
 	else:
 		return False

def generateTriples():
	a = 1
	b = 1
	c = 1
	for n in range(1, 500):
		for m in range(2, 500):
			for d in range(1, 500):
				if (m > n > 0):
					a = d*(m**2 - n**2)
					b = 2*d*m*n
					c = d*(m**2 + n**2)
					if(pythagTripleCheck(a, b, c) and a+b+c == 1000):
						return a*b*c

if __name__ == '__main__':
	if not pythagTripleCheck(3, 4, 5):
		raise AssertionError("Do not pass go, do not collect 200 quid, return your GCSE Maths Certificate")
	print generateTriples()