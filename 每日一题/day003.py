import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    else:
            return True


numlist = []
for i in range(0,200):
       if i >= 2 and isPrime(i) :
                numlist.append(i)

print(numlist)



