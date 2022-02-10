
s = 'a3b2c7'
output=''
for var in s:
    #print(var)
    if var.isalpha():
        x=var
    else:
        output=output+x*int(var)
print(output)


s='aaabbbbbcccccccc'

previous = s[0]
output=''
i=1
c=1
while i <= len(s)-1:
    #print(i)
    if(s[i] == previous):
        c=c+1
    else:
        output = output + str(c) +previous
        print(output)
        previous = s[i]
        c=1
    if (i == len(s)-1):
        output = output + str(c) +previous
    #print(s[i])
    i=i+1
print(output)




print(ord('a'))
print(chr(98))


s = 'a4k3b2'
out=''
for var in s:
    if(var.isalpha()):
        out=out + var
        previous=var
    else:
        i = chr(int(var) + ord(previous))
        out=out + i
print(out)



s='aaabbccdd'
l=[]
for var in s:
    if (var not in l):
        l.append(var)

print(l)    
print('_'.join(l))



#DICTIONARY

r = {}

r['A']=1
r['B']=2

print(r)

r['A'] = 2

print(r)
print(r.get('B'))


d= {'A':100,'B':200,'C':300}

for k,v in d.items():
    print(k,v)

print("\5")


word='ABBBBAAACCCBBBBB'
d={}

for var in word:
    d[var] = d.get(var,0)+1

print(d)

for k,v in d.items():
    print('{} occurs {} times'.format(k,v))




def reverseList(A, start, end):
    while start < end:
        temp = A[start]
        A[start]= A[end]
        A[end] = temp
        print(start,end)
        print(A)
        start += 1
        end -= 1
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6,7]
print(A)
reverseList(A, 0, 6)
print("Reversed list is")
print(A)


def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
