# IF = Do some code if a condition is true
# ESLSE = Do some code if a condition is false

age = int(input("What is your age? ")) 
if age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You are not born yet.")
elif age >= 13 and age < 18:
    print("You are a teenager.")
else:
    print("You are a minor.")
    