"""
Variables - Detective Profile
- Introduce variables
- Create a detective profile with:
  - Name (string)
  - Age (integer)
  - Is detective? (boolean)
  - Rating (float)
- Print values and explain data types
"""
#A variable is a named storage location in memory that can hold a value.

# Create detective profile variables
detective_name = "Sherlock Holmes"
detective_age = 35
is_detective = True
detective_rating = 9.8

# Print profile with data type afte it
print("Detective Profile:")
print("Name: " + detective_name + " (Type: " + str(type(detective_name)) + ")")
print("Age: " + str(detective_age) + " (Type: " + str(type(detective_age)) + ")")
print("Active Detective: " + str(is_detective) + " (Type: " + str(type(is_detective)) + ")")
print("Success Rating: " + str(detective_rating) + " (Type: " + str(type(detective_rating)) + ")")