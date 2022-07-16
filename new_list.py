list = [190,120,150,15,160,110]
small = list[0]
for i in range(0,6):
    if list[i] < small:
        small = list[i]
        smallIndex = i
print(smallIndex,":",small)
 
large = list[0]
index = 0
for i in range(0,6):
    if list[i] > large:
        large = list[i]
        index = i
print(index,":",large)

        

