"""bigger_number = 2312947017
smallr_number = 0

print("modulo profile of",bigger_number)
for i in range(1,10):
    print(" %"+str(i)+":",bigger_number%i)

for i in range(2,10):
    
    if divmod(bigger_number, i)[1] == 0 and smallr_number==0:
        smallr_number = i
        print(i,"--",smallr_number,"set to",i,"equals:",end=" ")
    elif divmod(bigger_number, i)[1] == 0:
        smallr_number *= i
        print(i,"--",smallr_number,"times",i,"equals:",end=" ")
    print(smallr_number)

print("modulo profile of",smallr_number)
for i in range(1,10):
    print(" %"+str(i)+":",smallr_number%i)"""

import random
bigger_number = random.randint(2312947017, 12439102547326)
smallr_number = 1

def getModuloProfile(number):
    res = {}
    for i in range(2,10):
        res[i]=number%i

    return res

target = getModuloProfile(bigger_number)
while getModuloProfile(smallr_number) != target:
    smallr_number += 1

print("OKAY!")
print("Big boy:",bigger_number)
print("with profile:")
for i in range(1,10):
    print(" %"+str(i)+":",bigger_number%i)
print("Small boy:",smallr_number)
print("with profile:")
for i in range(1,10):
    print(" %"+str(i)+":",smallr_number%i)
