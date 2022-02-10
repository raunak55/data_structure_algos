def isAnagram(a,b):
    #code here
    arr1={}
    arr2={}
   
    for ch in a:
    #    print(ch)
        if ch in arr1:
            arr1[ch]+=1
        else:
            arr1[ch]=1
    
    for ch in b:
        print(ch)
        if ch in arr2:
            arr2[ch]+=1
        else:
            arr2[ch]=1
        print(arr2[ch])
    
    print(arr1)
    print(arr2)
    #for key,value in arr1.items():
    #    if (key in arr2.keys() and value in arr2.values()):
    #        return True
    #    else:
    #        return False
#
    for key in arr1:
        print(key)
        if arr1[key] != arr2[key]:
            return False
    return True

a_1 = 'aabaaaa'
b_1 = 'aaaaaab'
out = isAnagram(a_1,b_1)
print(out)