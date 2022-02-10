import time
list1=[1,2,3,4,5,6,7,8,9,10]
#for i in range(0,100):
#    print(i)
    #time.sleep(1)#sleep for 1 second 

if len(list1) == 10:
    print('adasd')
else:
    pass

d=1
array= []
for var in range(d,len(list1)):
    array.append(list1[var])

for var in range(0,d):
    array.append(list1[var])
print(array)

arr = [1,2,3,4,5]
rotations = 4
arr = arr[4:]+arr[:4]
print(arr)


i=1
try:
    f = 3.0**i
    for i in range(100):
        print (i, f)
    f = f ** 2
except OverflowError as err:
    print ('Overflowed after ')