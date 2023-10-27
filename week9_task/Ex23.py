def search_index(arr, num):
    new_arr=[]
    for i in range(len(arr)):
        if arr[i] == num:
            new_arr.append(i)

    return new_arr

print(search_index([35,28,30,29,30], 30))
print(search_index([35,28,30,29,30], 31))
