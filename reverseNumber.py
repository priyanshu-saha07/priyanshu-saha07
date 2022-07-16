x=123
length=3
remainder=0
numCopy=0
for i in range (0,length):
    remainder=x%10
    numCopy=numCopy*10+remainder
    x=x//10
print(numCopy)    

