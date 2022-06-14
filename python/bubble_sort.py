def bubble_sort(arr):
    swaps = 0
    l, r = 0, 1

    while l < len(arr):
        while r < len(arr):
            if arr[l] > arr[r]:
                swaps += 1
                arr[l], arr[r] = arr[r], arr[l]
                
            r += 1
        l += 1
        r = l + 1






    return swaps 

print(bubble_sort([4,3,5,0,1]))