def in_asc_order(arr):
    # random_ is not allowed
    bool = True
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            continue
        else:
            bool = False
            break

    return bool #(True or false)


arr = [2, 1]
print(in_asc_order(arr))
