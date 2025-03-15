# A choose-your-own-adventure game simulating a day in the life of an accountant with multiple paths and endings
"""
Life of an Accountant Game

This is a text-based adventure game that simulates the first day of an accountant
at a new job. Players make choices that lead to different outcomes and endings.
The game flow is structured as a decision tree with multiple branches leading to
different endings. Each function presents the player with choices, processes their
input, and directs them to the next appropriate function based on their decision.
"""
# +-----------------------------+
# |   O                         |
# |  /|\                        |
# |   |    Fix my code          |
# |  / \   please. It's         |
# |        giving me an error!! |
# +-----------------------------+

def start_game():
    
    print("Welcome to the life of an accountant!")
    print("You are starting your first day at a new job.")
    first_choice()

def first_choice():
    print("\nDo you want to:")
    print("1. Organize your desk")
    print("2. Meet your colleagues")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        organize_desk()
    elif choice == "2":
        meet_colleagues()
    else:
        print("Invalid choice. Please try again.")
        first_choice()

def organize_desk():
    print("\nYou decided to organize your desk.")
    print("Do you want to:")
    print("1. Start with the files")
    print("2. Start with the stationery")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        files()
    elif choice == "2":
        stationery()
    else:
        print("Invalid choice. Please try again.")
        organize_desk()

def meet_colleagues():
    print("\nYou decided to meet your colleagues.")
    print("Do you want to:")
    print("1. Introduce yourself to your manager")
    print("2. Chat with your peers")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        manager()
    elif choice == "2":
        peers()
    else:
        print("Invalid choice. Please try again.")
        meet_colleagues()

def files():
    print("\nYou started organizing the files.")
    print("Do you want to:")
    print("1. Sort them by date")
    print("2. Sort them by client name")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("\nYou sorted the files by date. Your manager is impressed. You get a promotion!")
        end_game("Promotion")
    elif choice == "2":
        print("\nYou sorted the files by client name. It took longer than expected. You missed an important meeting.")
        end_game("Missed Meeting")
    else:
        print("Invalid choice. Please try again.")
        files()

def stationery():
    print("\nYou started organizing the stationery.")
    print("Do you want to:")
    print("1. Arrange them by type")
    print("2. Arrange them by color")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("\nYou arranged the stationery by type. It looks very neat. Your colleagues appreciate it.")
        end_game("Appreciation")
    elif choice == "2":
        print("\nYou arranged the stationery by color. It looks pretty but not very practical. Your manager is not happy.")
        end_game("Manager Unhappy")
    else:
        print("Invalid choice. Please try again.")
        stationery()

def manager():
    print("\nYou introduced yourself to your manager.")
    print("Do you want to:")
    print("1. Ask for advice")
    print("2. Discuss your career goals")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("\nYour manager gives you valuable advice. You feel more confident in your role.")
        end_game("Confidence")
    elif choice == "2":
        print("\nYour manager appreciates your ambition. You are given more responsibilities.")
        end_game("More Responsibilities")
    else:
        print("Invalid choice. Please try again.")
        manager()

def peers():
    print("\nYou started chatting with your peers.")
    print("Do you want to:")
    print("1. Join them for lunch")
    print("2. Discuss work-related topics")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("\nYou joined your peers for lunch. You made new friends.")
        end_game("New Friends")
    elif choice == "2":
        print("\nYou discussed work-related topics. You learned new things.")
        end_game("Learned New Things")
    else:
        print("Invalid choice. Please try again.")
        peers()

def end_game(outcome):
    print(f"\nGame Over: {outcome}")
    print("Thank you for playing the life of an accountant!")
    play_again()

def play_again():
    print("\nDo you want to play again?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        play_again()

if __name__ == "__main__":
    start_game()