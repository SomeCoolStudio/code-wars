# Given a non-empty array of integers, return the result of multiplying the values together in order
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24 


def grow(arr):

    result = 1
    
    for x in range(len(arr)):
        
        result = arr[x] * result

    return result

print (grow([4, 1, 1, 1, 4]))