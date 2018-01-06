#Prime generating integers
#Problem 357

def isPrime(n):
	if n==2 or n==3:
		return True
	if n%2==0 or n<2:
		return False
	for i in range(3,int(n**0.5)+1,2):   # only odd numbers
		if n%i==0:
			return False    
	return True

def isAllFactorsPrime(counter, list_factor):
	allPrime = True
	for each_factor in list_factor:
		temp = each_factor + (counter/each_factor)
		if(not (isPrime(temp))):
			allPrime = False
			break
	return allPrime
		
upper_limit = 100000000
for counter in range(2,upper_limit):
	list_of_divisors = list()
	for divisor_of_counter in range(2,int(counter/2)+1):
		if(counter % divisor_of_counter == 0):
			list_of_divisors.append(divisor_of_counter)
	list_of_divisors.append(1)
	list_of_divisors.append(counter)
	print(isAllFactorsPrime(counter,list_of_divisors),' counter: ', counter, ' divisors: ',list_of_divisors)
	
	