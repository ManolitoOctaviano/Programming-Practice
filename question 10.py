import itertools

def isPrime(n):
	if n==2 or n==3:
		return True
	if n%2==0 or n<2:
		return False
	for i in range(3,int(n**0.5)+1,2):   # only odd numbers
		if n%i==0:
			return False    
	return True

	
total = 0
counter = 0
for counter in range(1,2000000):
	if(isPrime(counter)):
		total+=counter


print('total: ',total)
	
		