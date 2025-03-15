"""
Rick Astley Dance Animation
This program displays an ASCII animation of Rick Astley dancing in the terminal
along with displaying lyrics from "Never Gonna Give You Up". The animation
consists of simple ASCII art frames that cycle to create a dancing effect.
The program will continue to run until interrupted with Ctrl+C.
Usage:
    Simply run the script and Rick will start dancing with lyrics.
    Press Ctrl+C to exit the animation.
Functions:
    clear_screen(): Clears the terminal screen based on the operating system
    dance(): Displays the dancing animation with lyrics
"""
# +-----------------------------+
# |   O                         |
# |  /|\                        |
# |   |    Fix my code          |
# |  / \   please. It's         |
# |        giving me an error!! |
# +-----------------------------+

import time
import os
import random

# ASCII frames for Rick Astley dance
frames = [
    """
    o
   /|\\
   / \\
    """,
    """
    o
   /|\\
    | \\
    """,
    """
    o
   /|\\
   / |
    """,
    """
     o
    /|\\
   / \\
    """,
    """
    o_
   /|\\
   / \\
    """
]

lyrics = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you"
]

def clear_screen():
    # Clear terminal screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

def dance():
    lyric_index = 0
    
    try:
        while True:
            for frame in frames:
                clear_screen()
                print("\n\n")
                print(lyrics[lyric_index])
                print("\n")
                print(frame)
                
                # Move to next lyric
                lyric_index = (lyric_index + 1) % len(lyrics)
                
                # Sleep to control animation speed
                time.sleep(0.3)
    except KeyboardInterrupt:
        clear_screen()
        print("Rick rolled away...")

if __name__ == "__main__":
    print("Rick Astley is dancing! Press Ctrl+C to stop.")
    time.sleep(2)
    dance()