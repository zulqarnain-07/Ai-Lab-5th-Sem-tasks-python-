# Task 2: Temperature Advisor
# Write a Python program that asks the user to enter the temperature and gives advice according to the temperature range.

temperature = int(input("Enter temperature: "))

if temperature >= 35:
    print("Very Hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Pleasant")
else:
    print("Cold")