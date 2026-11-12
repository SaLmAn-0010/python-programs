#  Check Positive, Negative or Zero

num = input("Enter a number: ")
if int(num) > 0:
    print(f"{num} is a positive number")
elif int(num) < 0:
    print(f"{num} is a negative number")
else:
    print(f"{num} is zero")