import random
#random is a built-in library in Python that allows you to generate random numbers

"""
Random Library
- Introduce `random.choice()` for picking random suspects/clues
- Example: Randomly selecting a detective’s next case
"""
# List of detective cases
cases = ["The Missing Jewels", "The Haunted Mansion", "The Bank Heist", 
         "The Mysterious Letter", "The Vanishing Painting"]

# List of suspects for each case
suspects = ["Butler", "Chef", "Gardener", "Maid", "Business Partner"]

# Randomly select a case and suspect
selected_case = random.choice(cases)
prime_suspect = random.choice(suspects)

print("New Case: " + selected_case)
print("Prime Suspect: " + prime_suspect)

# Challenge: Try modifying this code to include a list of 'clues' 
#   randomly select both a suspect and a clue for each case!