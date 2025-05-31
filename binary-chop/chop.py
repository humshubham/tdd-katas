def binary_search(target, arr, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search(target, arr, low, mid-1)
        else:
            return binary_search(target, arr, mid+1, high)
        
    else:
        return -1

def chop(target:int, array:list)->int:
    n = len(array)
    return binary_search(target, array, 0, n-1)
    

    
print(chop(5, [1,3,5]))