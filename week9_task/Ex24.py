def add_list(arr1, arr2):
    new_arr=[]
    if len(arr1) >= len(arr2):
        long_arr = arr1
        short_arr = arr2
    else:
        long_arr = arr2
        short_arr = arr1

    for i in range(len(long_arr)):
        if i < len(short_arr):
            new_arr.append(long_arr[i]+short_arr[i])
        else:
            new_arr.append(long_arr[i])

    return new_arr

print(add_list([1,2,3,4], [1,2]))
print(add_list([0,1], [1,2,6,7,8]))
    