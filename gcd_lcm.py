def getGL(num1, num2):
	g = gcd(num1, num2)
	l = lcm(num1, num2, g)
	print "".join("%s\n%s" % (g, l))
	
def gcd(a, b):
	if (a % b) == 0:
		return b
	else:
		return gcd(b, a % b)

def lcm(a, b, gcd):
	return (a/gcd) * b

if __name__ == "__main__":
	getGL(4328394962, 37285493920)
