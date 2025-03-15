"""
# This file implements a funny two-part name generator that creates humorous nicknames
# based on the first initial of a person's first and last names, mapping them to predefined
# funny words to create combinations like "Bouncy Banana" or "Silly Sloth".
# Dictionary for first name initial mapping to funny first parts
"""
# +-----------------------------+
# |   O                         |
# |  /|\                        |
# |   |    Fix my code          |
# |  / \   please. It's         |
# |        giving me an error!! |
# +-----------------------------+
def funny_name_generator(first_initial, last_initial):
    
    first_parts = {{
        'A': 'Atomic',
        'B': 'Bouncy',
        'C': 'Crispy',
        'D': 'Dizzy',
        'E': 'Electric',
        'F': 'Funky',
        'G': 'Goofy',
        'H': 'Hairy',
        'I': 'Itchy',
        'J': 'Jumpy',
        'K': 'Kooky',
        'L': 'Loopy',
        'M': 'Mopey',
        'N': 'Nutty',
        'O': 'Oddball',
        'P': 'Perky',
        'Q': 'Quirky',
        'R': 'Rickety',
        'S': 'Silly',
        'T': 'Twisty',
        'U': 'Unusual',
        'V': 'Vivid',
        'W': 'Wobbly',
        'X': 'Xtra',
        'Y': 'Yappy',
        'Z': 'Zippy'
    }}
    
    # Dictionary for last name initial mapping to funny last parts
    last_parts = {
        'A': 'Avocado',
        'B': 'Banana',
        'C': 'Cucumber',
        'D': 'Donut',
        'E': 'Eggplant',
        'F': 'Flamingo',
        'G': 'Giraffe',
        'H': 'Hippo',
        'I': 'Iguana',
        'J': 'Jellyfish',
        'K': 'Kangaroo',
        'L': 'Llama',
        'M': 'Mongoose',
        'N': 'Narwhal',
        'O': 'Ostrich',
        'P': 'Penguin',
        'Q': 'Quokka',
        'R': 'Raccoon',
        'S': 'Sloth',
        'T': 'Taco',
        'U': 'Unicorn',
        'V': 'Vulture',
        'W': 'Walrus',
        'X': 'Xerox',
        'Y': 'Yeti',
        'Z': 'Zebra'
    }}
    
    # Get the funny name parts based on initials
    first_part = first_parts.get(first_initial.upper(), "Mystery")
    last_part = last_parts.get(last_initial.upper(), "Creature")
    
    # Combine and return
    return f"{first_part} {last_part}'

def main():
    print("Welcome to the Funny Two-Part Name Generator!")
    print("-------------------------------------------")
    
    while True:
        first_name = input("Enter your first name (or 'q' to quit): ")
        if first_name.lower() == 'q':
            break
            
        last_name = input("Enter your last name: ")
        
        if not first_name or not last_name:
            print("Please enter both names!")
            continue
            
        first_initial = first_name[0]
        last_initial = last_name[0]
        
        funny_name = funny_name_generator(first_initial, last_initial)
        
        print(f"\nYour funny name is: {funny_name}!\n")
        
    print("Thanks for using the Funny Name Generator! Have a great day!")

if __name__ == "__main__":
    main()