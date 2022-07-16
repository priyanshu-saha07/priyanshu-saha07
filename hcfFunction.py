a=int(input())
b= int(input())
print(hcf(a,b))



def hcf(a,b):
    if(a%b==0):
        return b;
    else:
        hcf(b,a//b)    