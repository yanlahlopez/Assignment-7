import math
# Create a program that will ask for grade percentage
# Display equivalent grade/mark and description
# Grading System
# Grade/Mark    Percentage      Description
# 1.0           97-100          Excellent
# 1.25          94-96           Excellent
# 1.5           91-93           Very Good
# 1.75          88-90           Very Good
# 2.0           85-87           Good
# 2.25          82-84           Good
# 2.50          79-81           Satisfactory
# 2.75          76-78           Satisfactory
# 3.0           75              Passing
# 5.0           65-74           Failure
# Inc.                          Incomplete
# W                             Withdrawn
# D                             Dropped


Percentage = input("Grade Percentage: ")

if Percentage == "Inc.":
    print("Description: Incomplete")
elif Percentage == "W":
    print("Description: Withdrawn")
elif Percentage == "D":
    print("Description: Dropped")
else:
    percentage = float(Percentage)
    if percentage >= 96.5 and percentage <= 100:
        print("Grade/Mark: 1.0")
        print("Description: Excellent")
    elif percentage >= 93.5 and percentage <= 96.4:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    elif percentage >= 90.5 and percentage <= 93.4:
        print("Grade/Mark: 1.50")
        print("Description: Very Good")
    elif percentage >= 87.5 and percentage <= 90.4:
        print("Grade/Mark: 1.75")
        print("Description: Very Good")
    elif percentage >= 84.5 and percentage <= 87.4:
        print("Grade/Mark: 2.0")
        print("Description: Good")
    elif percentage >= 81.5 and percentage <= 84.4:
        print("Grade/Mark: 2.25")
        print("Description: Good")
    elif percentage >= 78.5 and percentage <= 81.4:
        print("Grade/Mark: 2.50")
        print("Description: Satisfactory")
    elif percentage >= 75.5 and percentage <= 78.4:
        print("Grade/Mark: 2.75")
        print("Description: Satisfactory")
    elif percentage >= 74.5 and percentage <= 75.4:
        print("Grade/Mark: 3.00")
        print("Description: Passing")
    elif percentage >= 64.5 and percentage <= 74.4:
        print("Grade/Mark: 5.00")
        print("Description: Failure")
    elif percentage <= 64.4:
        pass