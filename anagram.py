


def ana(s1,s2):

    for var in s1:
        if var in s1_h:
            s1_h[var]+=1
        else:
            s1_h[var]=1

    for var in s2:
        if var in s2_h:
            s2_h[var]+=1
        else:
            s2_h[var]=1
    print(s1_h)
    print(s2_h)

    for key in s1_h:
        print(key)
        if s1_h[key] != s2_h[key]:
            return False
    return True
s1 = 'MATPP123'
s2 = 'AT123PMP'

s1_h={}
s2_h={}
print(ana(s1,s2))


print('*************')
def ana_sorted(s1,s2):
    if sorted(s1)==sorted(s2):
        return True
    else :
        return False
    
print(ana_sorted(s1,s2))