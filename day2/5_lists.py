"""
Lists (Arrays)
- Introduce lists and how they store multiple values
- Example: Storing multiple suspects in a list and iterating through them
"""
# Create a list of suspects
suspects = ["Colonel Mustard", "Professor Plum", "Miss Scarlet", "Mrs. Peacock"]

# Print each suspect using a for loop
print("List of Suspects:")
for suspect in suspects:
    print("- " + suspect)

# Access specific suspects by index
print("\nPrime Suspect: " + suspects[0])
print("Last Added Suspect: " + suspects[-1])

# Add a new suspect to the list
suspects.append("Mr. Green")
print("\nUpdated suspect list has " + str(len(suspects)) + " people")

"""
Challenge: 
Try modifying the code to:
1. Remove a suspect using .pop() or .remove()
    Example ==> list.pop(0)  # removes first suspect
    Example ==> list.remove("Suspect Name")  # removes specific suspect
2. Sort the suspects alphabetically using .sort()
    Example ==> list.sort()
    print("Sorted list:", list)
3. Print the index of 'Miss Scarlet' using .index()
    Example ==> index = list.index("Suspect Name")
    print("Miss Scarlet is at index: " + index)
"""