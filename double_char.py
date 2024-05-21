
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


# s = "1234!"

# def double_char(s):
    
#     new_string = "" 

#     for x in s:
#         new_string +=  x*2

#     return (new_string)


# print(double_char (s))


# Pythonic Solution
def double_char(s):
    return ''.join(c * 2 for c in s)

print (double_char("String"))