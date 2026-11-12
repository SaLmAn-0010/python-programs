# Temperature to Celsius conversion

unit = input("is this temperature in celsius or fahrenheit (c/f): ")
temp = float(input("Enter temperature: "))

if unit == "c":
    temp =round((9 * temp) / 5 + 32, 1 )
    print(f"{temp}°F")
elif unit == "f":
    temp = ((temp - 32) * 5/9)
    print(f"{temp}°C")      

else:
    print(f"{unit} was not valid")