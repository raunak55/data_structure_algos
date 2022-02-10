arr = [ 1, 2, 5, 10, 20, 50, 100, 500, 1000]

target = 121

t_arr = []
i=len(arr)-1
print(i)

while (i >= 0):
    print(arr[i])
    while target >= arr[i]:
        target -= arr[i]
        print(target)
        t_arr.append(arr[i])
    i = i-1
print(t_arr)