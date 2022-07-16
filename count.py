arr=[5,7,8,4,9,2,1,3]
even=0
odd=0
for i in range(len(arr)):
    if(arr[i]%2==0):
        even+=1
    else:
        odd+=1
print("even: ",even)
print("odd: ",odd)