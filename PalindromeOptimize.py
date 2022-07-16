arr = [9,7,7,9]
i = 0
j = len(arr)-1
isPalindrome = True

while(i<=j):
    if(arr[i]!=arr[j]):
        isPalindrome = False
        break
    else:
        i += 1
        j -=1

if(isPalindrome):
    print("It's Palindrome")
else:
    print("Not Palindrome")            