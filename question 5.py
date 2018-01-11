
'''number = 2519

while(not(number%2 == 0 and
	  number%3 == 0 and
	  number%4 == 0 and
	  number%5 == 0 and
	  number%6 == 0 and
	  number%7 == 0 and
	  number%8 == 0 and
	  number%9 == 0 and
	  number%10 == 0 and
	  number%11 == 0 and
	  number%12 == 0 and
	  number%13 == 0 and
	  number%14 == 0 and
	  number%15 == 0 and
	  number%16 == 0 and
	  number%17 == 0 and
	  number%18 == 0 and
	  number%19 == 0 and
	  number%20 == 0 
  )):
	number += 1
print(number)'''

#### OTHER SOLUTION ####
#Recursive Euclid's algorithm for GCD

#Base Condition
#GCD(A, 0) = A

#Recurrence Relation
#GCD(A, B) = GCD (B, A mod B)

def GCD(M, N):
    while (N != 0):
        M, N = N, M % N
    return M

LCM = 1
for X in range(1, 21):
    LCM = (X * LCM)/GCD(X, LCM)
print(LCM)