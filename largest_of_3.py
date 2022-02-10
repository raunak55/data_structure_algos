

r= [1,2,4,5,3,11]
target = 13
m = len(r)

for i in range(0,m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            print(i,j,k)
            if( (r[i]+r[j]+r[k]) == target):
                print('Got it')

for i in range(0,m):
    for j in range(i+1,m):
        no = target-r[i]-r[j]
        print(no)
        if ( no in r):
            print('Got it')