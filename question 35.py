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
# Different from permutation	
def isCircularPrime(n):
	perm_values = populate(str(n))
	for counter in perm_values:
		perm_value_int = int(counter)
		if(not(isPrime(perm_value_int))):
			return False
	
	return True
	
def populate(n):
	values = list()
	values.append(n)
	for counter in range(1, len(n)):
		values.append(n[counter:]+ n[:counter])
	return values

	
total = 0
for counter in range(1,1000000):
	if(isCircularPrime(counter)):
		total+=1
		print(counter)

print('total: ',total)
	
		