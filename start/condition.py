# #  Make your program take different paths based on conditions.
# # Python Conditional Statements — Detailed Beginner Explanation

# ## 1. Definition of Conditional Statements

# **Definition:**

# > **Conditional statements are used in Python to make decisions and execute different blocks of code depending on whether a condition is `True` or `False`.**

# In simple words:

# **Condition → Check → Decision → Execute code**

# For example, imagine:

# > If it is raining → take an umbrella.
# > Otherwise → don't take an umbrella.

# Python does the same thing using `if`, `elif`, and `else`.

# ---

# # 2. What is a Condition?

# ### Definition

# > A **condition** is an expression that Python evaluates as either `True` or `False`.

# Example:

# ```python
# age = 20

# age >= 18
# ```

# The result is:

# ```text
# True
# ```

# Another example:

# ```python
# age = 15

# age >= 18
# ```

# Result:

# ```text
# False
# ```

# So:

# ```text
# Condition
#     ↓
# True or False
# ```

# ---

# # 3. `if` Statement

# ### Definition

# > The `if` statement executes a block of code only when the given condition is `True`.

# ### Syntax

# ```python
# if condition:
#     statement
# ```

# Example:

# ```python
# age = 20

# if age >= 18:
#     print("You are an adult")
# ```

# ### How it works

# Python checks:

# ```python
# age >= 18
# ```

# Since `20 >= 18` is `True`, Python executes:

# ```python
# print("You are an adult")
# ```

# Output:

# ```text
# You are an adult
# ```

# ---

# # 4. Indentation

# Python uses **indentation** to identify which statements belong to the `if` block.

# Correct:

# ```python
# age = 20

# if age >= 18:
#     print("Adult")
# ```

# The spaces before `print()` are important.

# Usually, Python uses **4 spaces**.

# ```python
# if condition:
#     # 4 spaces
#     statement
# ```

# Incorrect:

# ```python
# if age >= 18:
# print("Adult")
# ```

# This produces an indentation error.

# ---

# # 5. `if-else` Statement

# Sometimes we have **two possible paths**.

# For example:

# ```text
# If age >= 18
#        ↓
#     Adult

# Otherwise
#        ↓
#     Minor
# ```

# ### Definition

# > The `if-else` statement executes one block when the condition is `True` and another block when the condition is `False`.

# ### Syntax

# ```python
# if condition:
#     statement
# else:
#     statement
# ```

# ### Example

# ```python
# age = 16

# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")
# ```

# Output:

# ```text
# You are a minor
# ```

# Because:

# ```text
# 16 >= 18 → False
# ```

# Therefore, Python executes `else`.

# ---

# # 6. `if-elif-else`

# What if we have **more than two conditions**?

# For example, grades:

# ```text
# 90 or above → A+
# 75 or above → A
# 60 or above → B
# Below 60    → C
# ```

# We can use `if-elif-else`.

# ### Definition

# > The `if-elif-else` statement is used when a program needs to check multiple conditions and execute the block corresponding to the first condition that is `True`.

# ### Syntax

# ```python
# if condition1:
#     statement
# elif condition2:
#     statement
# elif condition3:
#     statement
# else:
#     statement
# ```

# ### Example

# ```python
# marks = 82

# if marks >= 90:
#     print("Grade A+")
# elif marks >= 75:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# else:
#     print("Grade C")
# ```

# Output:

# ```text
# Grade A
# ```

# ### Why?

# Python checks from top to bottom:

# ```text
# 82 >= 90  → False
# 82 >= 75  → True
# ```

# So it executes:

# ```python
# print("Grade A")
# ```

# After finding a true condition, Python skips the remaining conditions.

# ---

# # 7. Comparison Operators

# Conditions frequently use **comparison operators**.

# ### Definition

# > Comparison operators are used to compare two values and return either `True` or `False`.

# | Operator | Meaning               | Example    | Result |
# | -------- | --------------------- | ---------- | ------ |
# | `==`     | Equal to              | `10 == 10` | `True` |
# | `!=`     | Not equal to          | `10 != 5`  | `True` |
# | `>`      | Greater than          | `10 > 5`   | `True` |
# | `<`      | Less than             | `5 < 10`   | `True` |
# | `>=`     | Greater than or equal | `10 >= 10` | `True` |
# | `<=`     | Less than or equal    | `5 <= 10`  | `True` |

# ### Important Difference

# `=` and `==` are different.

# ### `=`

# Used for **assignment**:

# ```python
# age = 20
# ```

# Meaning:

# > Store `20` in the variable `age`.

# ### `==`

# Used for **comparison**:

# ```python
# age == 20
# ```

# Meaning:

# > Is `age` equal to `20`?

# ---

# # 8. Logical Operators

# Python has three important logical operators:

# ```text
# and
# or
# not
# ```

# ## `and`

# ### Definition

# > `and` returns `True` when **both conditions are True**.

# Example:

# ```python
# age = 20
# has_id = True

# if age >= 18 and has_id:
#     print("Entry allowed")
# ```

# Both conditions are true:

# ```text
# age >= 18 → True
# has_id    → True

# True and True → True
# ```

# ---

# ## `or`

# ### Definition

# > `or` returns `True` when **at least one condition is True**.

# Example:

# ```python
# day = "Sunday"

# if day == "Saturday" or day == "Sunday":
#     print("Weekend")
# ```

# Here:

# ```text
# Saturday? → False
# Sunday?   → True

# False or True → True
# ```

# Output:

# ```text
# Weekend
# ```

# ---

# ## `not`

# ### Definition

# > `not` reverses a Boolean value. `True` becomes `False`, and `False` becomes `True`.

# Example:

# ```python
# is_raining = False

# if not is_raining:
#     print("You don't need an umbrella")
# ```

# ---

# # 9. Nested `if`

# ### Definition

# > A **nested `if`** is an `if` statement placed inside another `if` statement.

# Example:

# ```python
# age = 20
# has_id = True

# if age >= 18:
#     if has_id:
#         print("Entry allowed")
#     else:
#         print("ID required")
# else:
#     print("You are under 18")
# ```

# Here, the second `if` is inside the first `if`.

# ```text
# age >= 18?
#     |
#    Yes
#     |
# has_id?
#     |
#    Yes
#     |
# Entry allowed
# ```

# ---

# # 10. Real-Life Example

# Suppose an ATM checks whether you can withdraw money.

# ```python
# balance = 5000
# amount = 2000

# if amount <= balance:
#     print("Withdrawal successful")
# else:
#     print("Insufficient balance")
# ```

# Here the condition is:

# ```python
# amount <= balance
# ```

# Python checks:

# ```text
# 2000 <= 5000 → True
# ```

# Therefore:

# ```text
# Withdrawal successful
# ```

# ---

# # 11. Complete Example for Beginners

# ```python
# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Excellent! Grade A+")
# elif marks >= 75:
#     print("Very Good! Grade A")
# elif marks >= 60:
#     print("Good! Grade B")
# elif marks >= 40:
#     print("Pass! Grade C")
# else:
#     print("Fail")
# ```

# ### Example 1

# ```text
# Enter your marks: 92
# Excellent! Grade A+
# ```

# ### Example 2

# ```text
# Enter your marks: 68
# Good! Grade B
# ```

# ### Example 3

# ```text
# Enter your marks: 30
# Fail
# ```

# ---

# # 12. Main Points to Remember

# ```text
# Conditional Statements
#         |
#         ├── if
#         ├── if-else
#         ├── if-elif-else
#         └── nested if
# ```

# ### Definitions for Interview

# **`if`:**

# > Used to execute code when a condition is true.

# **`else`:**

# > Used to execute code when the `if` condition is false.

# **`elif`:**

# > Used to check another condition when the previous condition is false.

# **Condition:**

# > An expression that evaluates to `True` or `False`.

# **Conditional Statement:**

# > A statement that allows a program to make decisions and follow different execution paths based on conditions.

# ### Simple formula

# ```text
# if     → First condition
# elif   → Another condition
# else   → None of the above conditions
# ```

# **Next topic:** `if`, `if-else`, and `if-elif-else` practice programs — **even/odd, positive/negative, voting eligibility, largest of 2/3 numbers, and grade calculator**.
