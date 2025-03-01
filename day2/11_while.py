"""
While Loop
- Explain while loops with conditions
- Example: Keep guessing the secret code until correct
"""
#A while loop is a control flow statement that allows code to be executed based on a condition

secret_code = "6"
guess = ""

print("Welcome to the Secret Code Game!")
print("Try to guess the 1-digit code.")

while guess != secret_code:
    guess = input("Enter your guess: ")
    if guess == secret_code:
        print("Congratulations! You cracked the code!")
    else:
        print("Wrong guess, try again!")

# Challenge: Modify the code to:
# 1. Count how many attempts the user takes and print the count at the end
# 2. Add a hint if their guess is higher or lower than the secret code