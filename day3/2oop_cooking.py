"""
# Object-Oriented Programming (OOP): Recipe Class
Complete the `Recipe` class by adding a `serve()` method that prints "The dish is ready!"
"""

# Using a class to represent a recipe
class Recipe:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        print(f"Preparing {self.name}")

    def cook(self):
        print(f"Cooking {self.name}")

    # Challenge: Add a serve() method that prints "The dish is ready!"

pasta = Recipe("Pasta")
pasta.prepare()
pasta.cook()
# Call pasta.serve() here after implementing it!
