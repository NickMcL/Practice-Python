class NumOperations:
	
	def __init__(self, num1, num2):
		primef1 = self.factorize([num1])
		primef2 = self.factorize([num2])
		print self.getLCM()
	
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

	def getLCM(self):
		lcmpf = []
		lcm = 1
		checked = []
		
		for x in self.primef1:
			if x not in checked:
				if self.primef1.count(x) > self.primef2.count(x):
					lcmpf.extend([x] * self.primef1.count(x))
				else:
					lcmpf.extend([x] * self.primef2.count(x))
				checked.append(x)
				
		for x in self.primef2:
			if x not in checked:
				lcmpf.extend([x] * self.primef2.count(x))
				checked.append(x)
		
		for x in lcm:
			lcm *= x
		return lcm
		

if __name__ == "__main__":
	NumOperations(60,54)
