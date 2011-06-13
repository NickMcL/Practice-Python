class NumOperations:
	
	def __init__(self, num1, num2):
		g = self.GCD(num1, num2)
		l = self.LCM(num1, num2, g)
		print "".join("%s\n%s" % (g, l))
		
	def GCD(self, a, b):
		if (a % b) == 0:
			return b
		else:
			return self.GCD(b, a % b)

	def LCM(self, a, b, gcd):
		return (a/gcd) * b

if __name__ == "__main__":
	NumOperations(4328394962, 37285493920)
