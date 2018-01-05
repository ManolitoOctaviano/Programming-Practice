
unique = list()
N = 101
for a in range(2, N):
	for b in range(2, N):
		product = a ** b
		if (product not in unique):
			
			unique.append(product)
			
print('count ', len(unique))