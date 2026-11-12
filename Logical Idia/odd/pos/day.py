# This program converts a given number of days into seconds.

days = int(input("Enter number of days: "))

hours = 24
minutes = 60
seconds = 60

total_seconds = days * hours * minutes * seconds

print("Total seconds:", total_seconds)
