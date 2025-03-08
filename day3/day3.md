# 🍳 Cooking with Python - Paradigm Challenges
SEE CODE ONLINE HERE: https://onlinegdb.com/Y-PEJRWPo
## 📌 Introduction
This project contains four different Python scripts, each demonstrating a different **programming paradigm** using a **cooking theme**.  

Your goal is to **read the code, understand the paradigm, and complete the challenge** in each file.  

---

## 📝 Challenges Overview

### 1️⃣ **Procedural Programming** (`procedural_cooking.py`)
**Concept:** Organizing code into reusable **functions** that perform **step-by-step** tasks.

#### **Problem:**
The `cook_omelette()` function provides a basic cooking process, but it's missing an important step.

#### **Challenge:**
Modify the function to **add a new cooking step**, such as:
- Seasoning with salt and pepper  
- Adding cheese to the omelette  
- Serving on a plate  

#### **Hint:**
Inside the `cook_omelette()` function, add a new `print()` statement with the missing step.

---

### 2️⃣ **Object-Oriented Programming (OOP)** (`oop_cooking.py`)
**Concept:** Representing **real-world objects** (e.g., a **Recipe**) as **Python classes** with **methods**.

#### **Problem:**
The `Recipe` class has methods for **preparing** and **cooking**, but it lacks a method for **serving** the dish.

#### **Challenge:**
Add a `serve()` method inside the `Recipe` class that prints:
```python
print("The dish is ready!")
```

#### **Hint:**
Inside the class, define a new method:
```python
def serve(self):
    print("The dish is ready!")
```
Then, after `pasta.prepare()` and `pasta.cook()`, call:
```python
pasta.serve()
```

---

### 3️⃣ **Functional Programming** (`functional_cooking.py`)
**Concept:** Using **pure functions** and **data transformations** instead of changing variables.

#### **Problem:**
The function `transform_ingredients()` converts raw ingredients into "Cooked [ingredient]" using `map()`, but it doesn’t include an extra **"Chopped"** step.

#### **Challenge:**
Modify the `lambda` function to **prepend** `"Chopped "` before `"Cooked "`.

#### **Hint:**
Update this line:
```python
return list(map(lambda ingredient: f"Chopped {ingredient}, Cooked {ingredient}", ingredients))
```
Now, the output should be:
```python
["Chopped Tomato, Cooked Tomato", "Chopped Mushroom, Cooked Mushroom", "Chopped Spinach, Cooked Spinach"]
```

---

### 4️⃣ **Modular Programming** (`modular_cooking.py`)
**Concept:** Splitting code into **separate files** for reusability.

#### **Problem:**
A function `boil_water()` is missing from `cooking_helpers.py`. Instead of writing it in `modular_cooking.py`, we need to **import it from another file**.

#### **Challenge:**
1. **Create a new file** called `cooking_helpers.py`.
2. **Move `boil_water()` into it**, like this:
```python
# cooking_helpers.py
def boil_water():
    print("Boiling water...")
```
3. **Import it in `modular_cooking.py`**, then call it:
```python
from cooking_helpers import boil_water
boil_water()
```

#### **Hint:**
If you get an **ImportError**, make sure:
- `cooking_helpers.py` is in the **same directory** as `modular_cooking.py`.
- The function is properly defined with `def boil_water():`.

---

## ✅ Next Steps
1. Open each Python file and **try to complete the challenge**.  
2. Run the script to **test your solution**.  
3. If stuck, review the **hints** above or search online for examples.  

---

💡 **Bonus Challenge:**  
Can you modify these programs to support **different recipes** instead of just an omelette or pasta?  

Happy coding and happy cooking! 🍽️👨‍🍳🔥  


---

### **How to Use This:**
- Save this file as **`README.md`** in the project folder.
- It gives **clear instructions** for students and helps them **understand each paradigm**.
- They can **refer back** to it while working on the coding challenges.

Would you like any **adjustments** or **extra hints**? 🚀😊