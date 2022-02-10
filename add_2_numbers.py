l1 = [2,4,3]
l2 = [5,6,4]

#Output: [7,0,8]
#Explanation: 342 + 465 = 807.


len_l1 =len(l1)-1
len_l2 = len(l2)-1

sum = 0
sum_1 = 0 

while (len_l1 >= 0):
    sum = sum + 10**len_l1 * l1[len_l1]
    len_l1 = len_l1 -1

while (len_l2 >= 0):
    sum_1 = sum_1 + 10**len_l2 * l2[len_l2]
    len_l2 = len_l2 -1

sum_final = sum + sum_1 
print(sum_final)
print(list(str(sum_final)[::-1]))
print(list(map(int,str(sum_final)[::-1])))