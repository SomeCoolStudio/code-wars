
# Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

def opposite(number):
  
  # multiply by negative number for inverse
  inverse_result = number * -1
  
  return inverse_result

print(opposite(-4))