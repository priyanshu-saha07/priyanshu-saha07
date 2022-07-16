
A=[1,9,3,7,6,4,0,2,50,80,92,16]
KEY=16
for i in range (0,len(A)):
    if A[i]==KEY:
        break;
if(A[i]==KEY):
    print(i)
else:
    print("not found")            