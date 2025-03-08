"""
# Functional Programming: Processing Ingredients
Modify the function below to **add another transformation step**, like "Chop the onions".
"""

# Using functions to transform ingredients
def transform_ingredients(ingredients):
    return list(map(lambda ingredient: f"Cooked {ingredient}", ingredients))

ingredients = ["Tomato", "Mushroom", "Spinach"]
print(transform_ingredients(ingredients))
# Challenge: Modify the lambda function to also print "Chopped" before cooking.
