
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"


def domain_name(url):
    
    modified_string = ""
    n_string = ""

    if "https://www." in url:
        modified_string = "".join(url.split("https://www."))
        for char in modified_string:
            if char != ".":
                n_string += char
            else:
                break
        return n_string
    
    elif "https://" in url:
        modified_string = "".join(url.split("https://"))
        for char in modified_string:
            if char != ".":
                n_string += char
            else:
                break
        return n_string
    
    elif "http://www." in url:
        modified_string = "".join(url.split("http://www."))
        for char in modified_string:
            if char != ".":
                n_string += char
            else:
                break
        return n_string
    
    elif "http://" in url:
        modified_string = "".join(url.split("http://"))
        for char in modified_string:
            if char != ".":
                n_string += char
            else:
                break
        return n_string
    
    elif "www." in url:
        modified_string = "".join(url.split("www."))
        for char in modified_string:
            if char != ".":
                n_string += char
            else:
                break
        return n_string
    
    else:
        modified_string = "".join(url.split())
        for char in modified_string:
            if char != ".":
                n_string += char
            else:
                break
        return n_string

    return n_string

#Pythonic Solution
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


print(domain_name("http://www.zombie-bites.com"))