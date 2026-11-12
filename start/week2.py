# # Week 2: Decisions & Logic
# # Goal: Make your program take different paths based on conditions.
# # Concepts: Comparison operators (==, >, <), logical operators (and, or, not), if, elif, and else statements.
# # Mini-Project: Text-Based Adventure Game — A branching story where user choices determine if they win, lose, or encounter new events.

# # Python Conditions & Operators — Zero to Advanced

# These concepts are used to make a Python program **take different paths based on conditions**.

# ---

# ## 1. What is a Condition?

# ### Definition

# A **condition** is an expression that Python evaluates as either **`True` or `False`**.

# ```python
# age = 20

# print(age > 18)
# ```

# Output:

# ```text
# True
# ```

# Because `20 > 18`.

# Another example:

# ```python
# age = 15

# print(age > 18)
# ```

# Output:

# ```text
# False
# ```

# ### Basic idea

# ```text
# Condition → True / False → Decision
# ```

# ---

# # 2. Comparison Operators

# ### Definition

# > **Comparison operators are used to compare two values. The result is always `True` or `False`.**

# The main operators are:

# | Operator | Meaning               | Example    | Result |
# | -------- | --------------------- | ---------- | ------ |
# | `==`     | Equal to              | `10 == 10` | `True` |
# | `!=`     | Not equal to          | `10 != 5`  | `True` |
# | `>`      | Greater than          | `10 > 5`   | `True` |
# | `<`      | Less than             | `5 < 10`   | `True` |
# | `>=`     | Greater than or equal | `10 >= 10` | `True` |
# | `<=`     | Less than or equal    | `5 <= 10`  | `True` |

# ---

# ## 2.1 `==` Equal To

# ### Definition

# `==` checks whether two values are equal.

# ```python
# a = 10
# b = 10

# print(a == b)
# ```

# Output:

# ```text
# True
# ```

# ### Important

# ```python
# a = 10
# ```

# `=` means **assignment**.

# ```python
# a == 10
# ```

# `==` means **comparison**.

# ---

# ## 2.2 `>` Greater Than

# ### Definition

# `>` checks whether the left value is greater than the right value.

# ```python
# age = 20

# print(age > 18)
# ```

# Output:

# ```text
# True
# ```

# ---

# ## 2.3 `<` Less Than

# ### Definition

# `<` checks whether the left value is less than the right value.

# ```python
# age = 16

# print(age < 18)
# ```

# Output:

# ```text
# True
# ```

# ---

# ## 2.4 `>=` Greater Than or Equal To

# ```python
# marks = 75

# print(marks >= 75)
# ```

# Output:

# ```text
# True
# ```

# It is `True` when the value is **75 or greater**.

# ---

# ## 2.5 `<=` Less Than or Equal To

# ```python
# age = 18

# print(age <= 18)
# ```

# Output:

# ```text
# True
# ```

# It is `True` when the value is **18 or less**.

# ---

# ## 2.6 `!=` Not Equal To

# ```python
# password = "1234"

# print(password != "5678")
# ```

# Output:

# ```text
# True
# ```

# ---

# # 3. Logical Operators

# ### Definition

# > **Logical operators are used to combine or modify conditions and produce a Boolean result (`True` or `False`).**

# Python has three main logical operators:

# ```text
# and
# or
# not
# ```

# ---

# # 4. `and` Operator

# ### Definition

# > `and` returns `True` only when **all conditions are True**.

# Example:

# ```python
# age = 20
# has_id = True

# print(age >= 18 and has_id)
# ```

# Output:

# ```text
# True
# ```

# Both conditions are true:

# ```text
# age >= 18 → True
# has_id    → True

# True and True → True
# ```

# ### Example where it is False

# ```python
# age = 16
# has_id = True

# print(age >= 18 and has_id)
# ```

# Output:

# ```text
# False
# ```

# Because:

# ```text
# False and True → False
# ```

# ### Truth table

# | A     | B     | A `and` B |
# | ----- | ----- | --------- |
# | True  | True  | True      |
# | True  | False | False     |
# | False | True  | False     |
# | False | False | False     |

# ---

# # 5. `or` Operator

# ### Definition

# > `or` returns `True` when **at least one condition is True**.

# Example:

# ```python
# day = "Sunday"

# print(day == "Saturday" or day == "Sunday")
# ```

# Output:

# ```text
# True
# ```

# Because the second condition is true.

# ### Truth table

# | A     | B     | A `or` B |
# | ----- | ----- | -------- |
# | True  | True  | True     |
# | True  | False | True     |
# | False | True  | True     |
# | False | False | False    |

# ---

# # 6. `not` Operator

# ### Definition

# > `not` reverses the Boolean result of a condition.

# ```python
# is_raining = False

# print(not is_raining)
# ```

# Output:

# ```text
# True
# ```

# Because:

# ```text
# not False → True
# ```

# Another example:

# ```python
# is_student = True

# print(not is_student)
# ```

# Output:

# ```text
# False
# ```

# ---

# # 7. `if` Statement

# ### Definition

# > The `if` statement executes a block of code **only when its condition is True**.

# ### Syntax

# ```python
# if condition:
#     statement
# ```

# ### Example

# ```python
# age = 20

# if age >= 18:
#     print("You are an adult")
# ```

# Output:

# ```text
# You are an adult
# ```

# ### Flow

# ```text
# Condition
#     ↓
#  True?
#   ↓
# Execute code
# ```

# If the condition is `False`, the `if` block is skipped.

# ---

# # 8. `if-else` Statement

# ### Definition

# > `if-else` is used when there are **two possible paths**. The `if` block runs when the condition is true; otherwise, the `else` block runs.

# ### Example

# ```python
# age = 16

# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")
# ```

# Output:

# ```text
# You cannot vote
# ```

# ### Flow

# ```text
#            Condition
#                |
#         +------+------+
#        True         False
#         |              |
#        if             else
#         |              |
#         +------+-------+
#                |
#             Continue
# ```

# ---

# # 9. `elif` Statement

# ### Definition

# > `elif` means **"else if"**. It is used to check another condition when the previous `if` or `elif` condition is false.

# ### Example

# ```python
# marks = 75

# if marks >= 90:
#     print("A+")
# elif marks >= 75:
#     print("A")
# elif marks >= 60:
#     print("B")
# else:
#     print("C")
# ```

# Output:

# ```text
# A
# ```

# Python checks from top to bottom:

# ```text
# 75 >= 90 → False
# 75 >= 75 → True
# ```

# So it executes `A` and stops checking the remaining conditions.

# ---

# # 10. `if-elif-else`

# ### Definition

# > `if-elif-else` is used when a program has **multiple possible conditions or paths**.

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
# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade A+")
# elif marks >= 75:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# elif marks >= 40:
#     print("Grade C")
# else:
#     print("Fail")
# ```

# If the user enters:

# ```text
# 82
# ```

# Output:

# ```text
# Grade A
# ```

# ---

# # 11. Combining Comparison + Logical Operators

# This is where conditions become more powerful.

# Example:

# ```python
# age = 25
# salary = 40000

# if age >= 21 and salary >= 30000:
#     print("Eligible")
# else:
#     print("Not Eligible")
# ```

# Here we have two conditions:

# ```text
# age >= 21
# salary >= 30000
# ```

# Both must be true because we used `and`.

# ---

# # 12. Nested `if`

# ### Definition

# > A **nested `if`** is an `if` statement placed inside another `if` statement.

# Example:

# ```python
# age = 25
# has_id = True

# if age >= 18:
#     if has_id:
#         print("Entry allowed")
#     else:
#         print("ID required")
# else:
#     print("You are under 18")
# ```

# ### Flow

# ```text
# Age >= 18?
#     |
#    Yes
#     |
# Has ID?
#   /    \
# Yes    No
#  |      |
# Allow  ID required
# ```

# ---

# # 13. Advanced: Multiple Conditions

# You can combine several conditions:

# ```python
# age = 25
# has_id = True
# has_ticket = True

# if age >= 18 and has_id and has_ticket:
#     print("Entry allowed")
# else:
#     print("Entry denied")
# ```

# All three conditions must be true.

# ---

# # 14. Advanced: Using `not` with Conditions

# ```python
# is_blocked = False

# if not is_blocked:
#     print("Account is active")
# else:
#     print("Account is blocked")
# ```

# Output:

# ```text
# Account is active
# ```

# ---

# # 15. Advanced: Checking a Range

# Instead of:

# ```python
# age >= 18 and age <= 60
# ```

# Python allows:

# ```python
# age = 25

# if 18 <= age <= 60:
#     print("Age is within the range")
# ```

# This is called a **chained comparison**.

# ---

# # 16. Important Difference: `if` vs `elif`

# ### Multiple `if`

# ```python
# marks = 95

# if marks >= 60:
#     print("Pass")

# if marks >= 90:
#     print("Excellent")
# ```

# Output:

# ```text
# Pass
# Excellent
# ```

# Both conditions are checked.

# ### `if-elif`

# ```python
# marks = 95

# if marks >= 60:
#     print("Pass")
# elif marks >= 90:
#     print("Excellent")
# ```

# Output:

# ```text
# Pass
# ```

# Once the `if` condition is true, Python does not check the `elif`.

# ---

# # 17. Real-World Example: Login System

# ```python
# username = "admin"
# password = "1234"

# if username == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Invalid username or password")
# ```

# Here:

# ```text
# username == "admin"
#         +
# password == "1234"
#         ↓
#        and
#         ↓
# Login decision
# ```

# ---

# # 18. Real-World Example: ATM

# ```python
# balance = 5000
# withdraw = 3000

# if withdraw <= balance:
#     print("Withdrawal successful")
#     balance = balance - withdraw
#     print("Remaining balance:", balance)
# else:
#     print("Insufficient balance")
# ```

# Output:

# ```text
# Withdrawal successful
# Remaining balance: 2000
# ```

# ---

# # 19. Complete Concept Map

# ```text
#                  CONDITIONS
#                      |
#           +----------+----------+
#           |                     |
#     Comparison              Logical
#     Operators               Operators
#           |                     |
#    == != > < >= <=          and or not
#           |                     |
#           +----------+----------+
#                      |
#                True / False
#                      |
#              Conditional
#               Statements
#                      |
#           +----------+----------+
#           |          |          |
#          if       elif        else
#           |          |          |
#           +----------+----------+
#                      |
#                 Program takes
#                 different paths
# ```

# ---

# # 20. Interview-Ready Definitions

# ### Condition

# > A condition is an expression that evaluates to either `True` or `False`.

# ### Comparison Operator

# > A comparison operator compares two values and returns a Boolean result.

# ### Logical Operator

# > A logical operator combines or modifies conditions to produce a Boolean result.

# ### `if`

# > `if` executes a block of code when a specified condition is `True`.

# ### `elif`

# > `elif` checks an additional condition when the previous condition is `False`.

# ### `else`

# > `else` executes a block of code when all preceding conditions are `False`.

# ### Conditional Statement

# > A conditional statement allows a program to make decisions and execute different code paths based on conditions.

# ---

# ## Quick Revision

# ```python
# # Comparison
# 10 == 10       # True
# 10 > 5         # True
# 5 < 10         # True

# # Logical
# True and True  # True
# True or False  # True
# not True       # False

# # Condition
# age = 20

# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")
# ```

# ### Learning order

# **Condition → Comparison Operators → `if` → `else` → `elif` → `and` → `or` → `not` → Nested `if` → Complex Conditions → Chained Comparisons → Practice Programs**.
