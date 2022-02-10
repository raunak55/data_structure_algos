
# Brute Force
r = [-2,2,5,-11,6]
l = len(r)
max=0
for i in range(0,l):
    sum=0
    for j in range(i,l):
        #print(i,j)
        #print(r[i],r[j])
        sum +=r[j]
        #print(sum)
        if (sum > max):
            max = sum
            #print(max)
#print(max)


#Kadence algorithm

#r = [-2,2,5,-11,6]
r = [6,-6,-2,1,2,4,-5,-1]
l = len(r)
curr_sum=0
max_sum=0
for i in range(0,l):
    curr_sum=curr_sum+r[i]
    print(curr_sum)
    if (curr_sum > max_sum):
        max_sum=curr_sum

    if (curr_sum < 0):
       curr_sum=0
print(max_sum)