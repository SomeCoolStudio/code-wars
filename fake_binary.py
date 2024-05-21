
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string


# def fake_bin(digit_string):
     
#     fake_binary_string = ""

#     for x in digit_string:

#         if int(x) >= 5:
#             fake_binary_string += "1"
#         else:
#             fake_binary_string += "0"
        
#     return fake_binary_string

# Pythonic Solution

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)