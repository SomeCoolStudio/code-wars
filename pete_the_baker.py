
# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

# Examples:

# # must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# # must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

recipe = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
available = {'sugar': 500, 'flour': 2000, 'milk': 2000, 'apples': 15, 'oil': 20}


def cakes(recipe, available):

    ingredient_found = True

    num_that_can_be_made = []

    for x in recipe:

        if ingredient_found == True:

            if x in available:

                ingredient_found = True

                if recipe.get(x) <= available.get(x):
                    
                    num_that_can_be_made.append(available.get(x) // recipe.get(x))
                
                else:

                    return 0

            else:

                ingredient_found = False
                return 0
            
    return min (num_that_can_be_made)

      
print (cakes(recipe,available))

# Pythonic Solution

def cakes(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)

print (cakes(recipe,available))