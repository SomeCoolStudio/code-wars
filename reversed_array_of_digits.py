
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    
    # int is not iterable
    # convert to str as strings in python are arrays 
    # and are iterable
    n = str(n)

    # create empty array
    result = []
    
    # iterate through array
    for integer in n:

        #add to array and convert to int
        result.append(int(integer))
        
    # return list reversed    
    return list(reversed(result))

# print results
print (digitize(128))