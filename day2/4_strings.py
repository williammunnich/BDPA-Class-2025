"""
Strings
- Explain string operations (concatenation, length, slicing)
- Example: Creating and manipulating a detective’s name
"""

# Demonstrate string operations with a detective's name
detective_first = "Sherlock"
detective_last = "Holmes"

# Concatenation - combining strings
full_name = detective_first + " " + detective_last
print("Full name:", full_name)

# String length
name_length = len(full_name)
print("Name length:", name_length)

# String slicing
first_initial = detective_first[0]
last_five = detective_last[-5:]
middle_chars = full_name[3:8]

print("First initial:", first_initial)
print("Last 5 letters of last name:", last_five)
print("Middle characters:", middle_chars)


#Change the First name to "Smitty" last name to "Werbenjagermanjensen"
# What do you think will happen? when you run it