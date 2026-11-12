# Exercise 2 shopping cart program

items = input(" what item would you like to  buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many would you like?: "))
total = price * quantity

print(f"you have bought {quantity} x{items}/s ")
print(f"your total is : {total} $")

