def merge_list(arr1, arr2):
    new_arr = arr1[:]
    for i in range(len(arr2)):
        cnt = 0
        for j in range(len(arr1)):
            if arr1[j] == arr2[i]:
                cnt=cnt+1
        
        if cnt == 0:
            new_arr.append(arr2[i])

    new_arr.sort()
    return new_arr

print(merge_list([1,2,3,4],[1,2,5]))
print(merge_list([0,1,10],[1,2,6,7,8]))