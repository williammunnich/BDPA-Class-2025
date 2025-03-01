"""
If-Elif-Else Statement
- Introduce multiple conditions
- Example: If fingerprint found, high chance of arrest; if shoe print, medium chance; otherwise, low chance
"""
chance = int(input("Press 1 for fingerprint, 2 for shoe print, or 3 for no prints: "))

if chance == 1:
    print("High chance of arrest - fingerprint found")
elif chance == 2:
    print("Medium chance of arrest - shoe print found")
else:
    print("Low chance of arrest - no prints found")

# Challenge: Modify the code to add another evidence type (like DNA) 
# and its corresponding arrest probability