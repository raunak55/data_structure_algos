def selection_sort(arr,t):
    for i in range(0,t):
        min = i
        for j in range(i+1,t):
            print(i,j)
            print(arr[min],arr[j])
            if arr[min] > arr[j]:
                print('True')
                min=j
        arr[i], arr[min] = arr[min], arr[i]
        #print(i,j)
        print(arr)
    return arr

arr = [8,10,4,3,2]
print(arr)
t = len(arr)
out = selection_sort(arr,t)
print(out)
