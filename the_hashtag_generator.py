# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


# def generate_hashtag(s):
    
#     hashtag = s.split()

#     new_string = ""

#     for x in range(len(hashtag)): 
#         new_string +=  (hashtag[x].capitalize())

#     new_string = "".join(("#",new_string))

#     if s and len(new_string) < 140:

#         return new_string
        
#     else:

#         return False

    

# generate_hashtag("")

# More Pythonic

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output