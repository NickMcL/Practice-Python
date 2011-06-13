class NumOperations:
	
	def __init__(self, num1, num2):
		primef1 = self.factorize([num1])
		primef2 = self.factorize([num2])
		print self.getLCM(primef1, primef2)
	
	def factorize(self, num):
		for x in num:
			if self.isPrime(x):
				num.remove(x)
				num.extend(self.factorize(self.isPrime(x)))
		return num
	
	def isPrime(self, num):
		x = 2
		
		while num % x != 0:
			x += 1
		if x == num:
			return []
		else:
			return [x, num/x]

	def getLCM(self, primef1, primef2):
		lcmpf = []
		lcm = 1
		checked = []
		
		for x in primef1:
			if x not in checked:
				if primef1.count(x) > primef2.count(x):
					lcmpf.extend([x] * primef1.count(x))
				else:
					lcmpf.extend([x] * primef2.count(x))
				checked.append(x)
				
		for x in primef2:
			if x not in checked:
				lcmpf.extend([x] * primef2.count(x))
				checked.append(x)
		
		for x in lcmpf:
			lcm *= x
		return lcm
		

if __name__ == "__main__":
	NumOperations(2578, 12348)
