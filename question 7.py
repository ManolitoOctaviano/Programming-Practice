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
while(total !=10001):
	counter+= 1
	if(isPrime(counter)):
		total+=1
		if(total == 10001):
			print(counter)

print('total: ',total)
	
		