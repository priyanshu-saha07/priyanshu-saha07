num=int(input("Enter The Number:"))
factorial=1
if num < 0:
    print ("Factorial Does Not exist for Negative Number")
elif num==0 or num==1:
    print("The Factorial of 0 is 1")
else:
    for i in range(2,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial);

