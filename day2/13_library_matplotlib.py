"""
Matplotlib Plotting Example
- Demonstrates basic line plotting using matplotlib
- Shows relationship between days and clues found in an investigation
- Example: Tracking progress of evidence collection over time
- Includes challenges for practicing different plotting patterns
"""
# Importing the necessary library
# pip install matplotlib
#matplotlib is a plotting library 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o')
plt.xlabel("X-axis | Day")
plt.ylabel("Y-axis | Clues Found")
plt.title("Simple Line Plot")
plt.show()


#Challenge 1: plot points into a straight line so there are the same number of clues each day
#Challenge 2: Plot points into a shape, a smile, or a piece of art