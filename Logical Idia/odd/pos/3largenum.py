# Find the Largest of Three Numbers
a = input("Enter first number:")
b = input("Enter second number:")   
c = input("Enter third number:")
if a > b and a > c:
    print(f"{a} first number is the largest")
elif b > a and b > c:
    print(f"{b} second number is the largest")
else:
    print(f"{c} third number is the largest")
