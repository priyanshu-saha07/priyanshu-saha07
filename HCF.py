a=int(input())
b=int(input())
HCF=1
for i in range (2,b+1):
    if a %i==0 and b %i==0:
        HCF= i
print(HCF)        
        
