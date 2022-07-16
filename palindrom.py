import array

arr=[9,7,7,9]
newArr= array.array("i",[])
i=len(arr)-1

isPalindrome=True
while(i>=0):
    newArr.append(arr[i])
    i -= 1

for x in range(len(arr)):
    if(arr[x]!=newArr[x]):
        isPalindrome=False
        break;
    else:
        x+=1

if(isPalindrome):
    print("it's Palindrome") 
else:
    print(" Not Palindrome")               
