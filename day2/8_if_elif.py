"""
Basic If Statement
- Introduce simple `if` conditions
- Example: Checking if a clue is found
"""
# Define a variable to track if a clue was found
clue_found = True

# Check if the clue was found
if clue_found:
    print("You found a clue!")
elif clue_found == False:
    print("Keep searching...")

# Challenge: Try modifying this code to add another variable called 'clue_type'
#  and use an elif statement to check for different types of clues (like 'footprint', 'note', or 'photo')