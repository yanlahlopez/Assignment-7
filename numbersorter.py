# Create a program that will ask for four numbers
# Display the numbers from highest to lowest
# Using only if-else statements

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

if num1 > num2 > num3 > num4:
    print(f"Highest to lowest: {num1}, {num2}, {num3}, {num4}")
elif num1 > num2 > num4 > num3:
    print(f"Highest to lowest: {num1}, {num2}, {num4}, {num3}")
elif num1 > num3 > num2 > num4:
    print(f"Highest to lowest: {num1}, {num3}, {num2}, {num4}")
elif num1 > num4 > num2 > num3:
    print(f"Highest to lowest: {num1}, {num4}, {num2}, {num3}")
elif num1 > num3 > num4 > num2:
    print(f"Highest to lowest: {num1}, {num3}, {num4}, {num2}")
elif num1 > num4 > num3 > num2:
    print(f"Highest to lowest: {num1}, {num4}, {num3}, {num2}")

elif num2 > num1 > num3 > num4:
    print(f"Highest to lowest: {num2}, {num1}, {num3}, {num4}")
elif num2 > num1 > num4 > num3:
    print(f"Highest to lowest: {num2}, {num1}, {num4}, {num3}")
elif num2 > num3 > num1 > num4:
    print(f"Highest to lowest: {num2}, {num3}, {num1}, {num4}")
elif num2 > num4 > num1 > num3:
    print(f"Highest to lowest: {num2}, {num4}, {num1}, {num3}")
elif num2 > num3 > num4 > num1:
    print(f"Highest to lowest: {num2}, {num3}, {num4}, {num1}")
elif num2 > num4 > num3 > num1:
    print(f"Highest to lowest: {num2}, {num4}, {num3}, {num1}")

elif num3 > num1 > num2 > num4:
    print(f"Highest to lowest: {num3}, {num1}, {num2}, {num4}")
elif num3 > num1 > num4 > num2:
    print(f"Highest to lowest: {num3}, {num1}, {num4}, {num2}")
elif num3 > num2 > num1 > num4:
    print(f"Highest to lowest: {num3}, {num2}, {num1}, {num4}")
elif num3 > num4 > num1 > num2:
    print(f"Highest to lowest: {num3}, {num4}, {num1}, {num2}")
elif num3 > num2 > num4 > num1:
    print(f"Highest to lowest: {num3}, {num2}, {num4}, {num1}")
elif num3 > num4 > num2 > num1:
    print(f"Highest to lowest: {num3}, {num4}, {num2}, {num1}")

elif num4 > num1 > num2 > num3:
    print(f"Highest to lowest: {num4}, {num1}, {num2}, {num3}")
elif num4 > num1 > num3 > num2:
    print(f"Highest to lowest: {num4}, {num1}, {num3}, {num2}")
elif num4 > num2 > num1 > num3:
    print(f"Highest to lowest: {num4}, {num2}, {num1}, {num3}")
elif num4 > num3 > num1 > num2:
    print(f"Highest to lowest: {num4}, {num3}, {num1}, {num2}")
elif num4 > num2 > num3 > num1:
    print(f"Highest to lowest: {num4}, {num2}, {num3}, {num1}")
elif num4 > num3 > num2 > num1:
    print(f"Highest to lowest: {num4}, {num3}, {num2}, {num1}")