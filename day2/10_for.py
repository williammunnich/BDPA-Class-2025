"""
For Loop
- Introduce loops with ranges
- Example: Checking multiple pieces of evidence (loop through a list of clues)
"""
# Example list of clues found at a crime scene
clues = ["footprints", "broken window", "fingerprints", "note"]

print("Detective's Investigation Log:")
for clue in range(len(clues)):
    print("Evidence #" + str(clue + 1) + ": " + clues[clue])

print("Total pieces of evidence:", len(clues))

# Challenge: Try and edit the code so that the last clue is not printed