n = int(input())
reverseNum =0
remainder = 0
while n>0:
    remainder = n%10
    reverseNum = reverseNum*10+remainder
    n = n//10

print(reverseNum)    
