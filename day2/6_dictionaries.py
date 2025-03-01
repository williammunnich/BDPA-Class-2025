"""
Dictionaries
- Explain key-value pairs and how they are useful
- Example: Storing detective profiles using dictionaries
"""
# A dictionary is like a container that stores pairs of related information
# Each pair has a 'key' (like a label) and a 'value' (the actual data)

detective_profiles = {
    "Sherlock": {
        "age": 35,
        "specialty": "deductive reasoning",
        "cases_solved": 142
    },
    "Poirot": {
        "age": 62,
        "specialty": "psychological analysis",
        "cases_solved": 89
    }
}

# Access information using keys
print("Sherlock's specialty: " + str(detective_profiles['Sherlock']['specialty']))
print("Poirot's solved cases: " + str(detective_profiles['Poirot']['cases_solved']))

# Challenge: Add a new detective to the profiles with their own stats!