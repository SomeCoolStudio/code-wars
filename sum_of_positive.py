# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.


def positive_sum(arr):
    
    result = 0

    for x in arr:

        if x > 0:

            result += x
            

    return print(result)
    
positive_sum([1,2,3,4,5])
