
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
# Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas

input_string = " a #b\nc\nd $e f g"

markers_list = ['#', '$']

def strip_comments(strng, markers):
    
    s_list = strng.split('\n')
    
    n_list = []

    for x in s_list:
        
        s = ""
        
        for x in x:
        
            if x in markers:

                break
                
            else:

                s += x

        n_list.append(s.rstrip())
        
    return "\n".join(n_list)


print (strip_comments(input_string,markers_list))