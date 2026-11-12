# python weight converter

weight = float(input("Enter weight"))
unit = input("kilogram or pound (kg/lb): ")

if unit == "kg":
    weight = weight * 2.20462
elif unit == "lb":
    weight = weight / 2.20462
else:
    print(f"{unit} was not valid")

    