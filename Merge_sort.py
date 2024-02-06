import math
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 # mid array 
    left_half = arr[:mid] # left from start to mid 
    right_half = arr[mid:] # right from mid ro end

    left_half = merge_sort(left_half) # recursive function to do tha same 
    right_half = merge_sort(right_half) # ...............

    return merge(left_half, right_half) # return those halfs 

def merge(left, right): # compare and merge 
    result = [] # list for the result to save sorted elements here
    left_idx, right_idx = 0, 0 # vals for right and left indexs

    while left_idx < len(left) and right_idx < len(right): # while left index smaller than right ( it is sorted)
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx]) # append it to tha result 
            left_idx += 1 # increase the value to ireate on the next 
        else: # else do the inverse 
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:]) # add alls 
    result.extend(right[right_idx:]) # add alls 
    return result

print (merge_sort([math.pi,4,2,1,6,5,32,684,321,00])) # try here 
