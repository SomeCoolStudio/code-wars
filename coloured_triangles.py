# <!-- A coloured triangle is created from a row of colours, each of which is red, green or blue. 
# Successive rows, each containing one fewer colour than the last, are generated by considering the two touching colours in the previous row. 
# If these colours are identical, the same colour is used in the new row. If they are different, the missing colour is used in the new row. 
# This is continued until the final row, with only a single colour, is generated.

# The different possibilities are:

# Colour here:        G G        B G        R G        B R
# Becomes colour:      G          R          B          G
# With a bigger example:

# R R G B R G B B
#  R B R G B R B
#   G G B R G G
#    G R G B G
#     B B R R
#      B G R
#       R B
#        G
# You will be given the first row of the triangle as a string and its your job to return the final colour which would appear in the bottom row as a string. 
# In the case of the example above, you would the given RRGBRGBB you should return G.

# The input string will only contain the uppercase letters R, G, B and there will be at least one letter so you do not have to test for invalid input.
# If you are only given one colour as the input, return that colour. -->


def triangle(row):
    
    new_string = " "
    # new_string = " ".join((row,"\n "))
    new_row = row.split()
    i_counter = 0

    for x in new_row:
        
        # print (new_row.index(x))
        i_counter += 1

        if i_counter in range(len(new_row)):
                

                if x == new_row[i_counter]:
                    
                    new_string += x + " "

                else:
                    if x == "R":

                        if new_row[i_counter] == "B":
                        
                            new_string += "G "

                        elif new_row[i_counter] == "G":

                             new_string += "B "
                            
                    if x == "B":

                        if new_row[i_counter] == "R":
                        
                            new_string += "G "

                        elif new_row[i_counter] == "G":

                             new_string += "R "

                    if x == "G":

                        if new_row[i_counter] == "R":
                        
                            new_string += "B "

                        elif new_row[i_counter] == "B":

                             new_string += "R "
    
    print (new_string)

    if len(new_string) > 5:
        
        triangle(new_string)          
                     

    

print ("R R G B R G B B") 
triangle("R R G B R G B B")
