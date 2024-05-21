
# Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):

    # using built in python function
    # string.replace(oldvalue, newvalue, count)
    x = x.replace(" ", "")
    
    return x

print(no_space("Hi there!    "))