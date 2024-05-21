# When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. 
# Implement a function that meets these requirements:

# Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
# Returns a Map<String, int> with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
# Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")

# Example
# "#FF9933" --> {r: 255, g: 153, b: 51}

hex_string = "#FF9933"

def hex_string_to_RGB(hex_string): 

    rgb = {"r":0, "g":0, "b":0}
    start =1
    
    for k,v in rgb.items():
        
        for i in range(start,len(hex_string)-1):
            decimal = int(hex_string[i:i+2], 16)
            rgb[k] = decimal
            start += 2
            break
  
    return rgb


#Pythonic Solution


def hex_string_to_RGB(hex_string): 
   
   return {'r': int(hex[1:3],16),'g': int(hex[3:5],16), 'b': int(hex[5:7],16)}

print (hex_string_to_RGB(hex_string))
