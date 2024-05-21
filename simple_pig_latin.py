
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    
    t_list = text.split()

    pig_string = ""

    for item in t_list:

        if item.isalpha():
            pig_string += item[1:] + item[0] + "ay "
        
        else:
            pig_string += item
    
    return (pig_string.rstrip())


print (pig_it('Hello world !'))


# Pythonic Solution


def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())