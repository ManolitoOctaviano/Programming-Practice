Maximum path sum I
Problem 18

input = open(r'input.txt','r').readlines()

input_list = []
for x in input:
	string = x.strip().split(' ')
	input_list.append(string)

total = 0
for row in range(len(input_list)-1,0,-1):
	above_list_value = input_list[row-1]
	bottom_list_value = input_list[row]
	#print(bottom_list_value)
	for counter in range(1,len(bottom_list_value),1):
		temp = int(above_list_value[counter-1]) + max(int(bottom_list_value[counter-1]), int(bottom_list_value[counter]))
		above_list_value[counter-1] = temp
		
print(above_list_value)
		
		
	


		
	
	
	
	
	