def isAmicable(a):
	b = getScore(a)
	num2 = getScore(b)
#	print('a: ',a,' b:',b, ' num2', num2)
	return (a == num2 and a != b)
Problem 21

def getScore(n):
	total = 0
	if(n%2==0):
		limit = int((n/2)+1)
	else:
		limit = n
	for counter in range(1, limit):
		if( (n % counter) == 0):
			total += counter
#			x.append(counter)
#	print(x)
	return total

list_of_num = list()

for counter in range(10,10001):
	if(isAmicable(counter)):

		list_of_num.append(counter)

print('total ', sum(list_of_num))
