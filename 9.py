#Special Pythagorean triplet
#Problem 9
import math

def isPerfectSquare(c_squared):
	root = math.sqrt(c_squared)
	return root.is_integer(),root


for a in range(1, 1000):
	for b in range(a+1, 1000):
		a_squared = a**2
		b_squared = b**2
		c_squared = a_squared + b_squared
		eval = isPerfectSquare(c_squared)
		if(eval[0]):
			c = eval[1]
			if((a + b + c) == 1000):
				print('product: ', (a*b*c))
			elif((a+b+c) > 1000):
				break;
			
		