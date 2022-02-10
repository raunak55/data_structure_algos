
def binary_search(arr,l,num):
    
    low = 0
    high = l
    while low <= high:
        print(low,high)
        mid = (high+low)//2
        print(mid)
        if (arr[mid] == num):
            return mid
        if( num < arr[mid] ):
            high = mid-1
        elif( num > arr[mid] ):
            low = mid+1

arr = [2,7,19,34,53,72]
#arr = [1,2,3,4,5]
num=72
l = len(arr) - 1
print(binary_search(arr,l,num))