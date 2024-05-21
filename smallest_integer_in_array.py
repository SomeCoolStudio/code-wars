
# Given an array of integers your solution should find the smallest integer.

def smallestnumber(array):

    # use first element to test against rest
    cur_int = array[0]

    for integer in array:

        # check to see if current number
        # we are testing is smallest
        # if curInt is larger then number then
        # that number is new smallest number
        if cur_int > integer:

            cur_int = integer
        
    return cur_int

print (smallestnumber([78, 56, 232, 12, 11, 43]))
