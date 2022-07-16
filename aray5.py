import array
#integer aray
# arr=[5,17,30,46,99,87,65,83,21,12,60,54,45,87,90,100]
# for i in range (len(arr)):
#     if(i%2==0):
#         print(arr[i],end=" ")

arr = array.array("i",[])
for i in range(0,4):
    arr.insert(i,int(input()))
for i in arr:
    print(i)