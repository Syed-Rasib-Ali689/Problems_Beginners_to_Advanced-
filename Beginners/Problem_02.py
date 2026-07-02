"""
Takes a student's marks (0–100) as input.
Validates the input — if the marks are outside the 0–100 range, print an error message and stop.
If valid, assign a letter grade based on this scale:
"""

marks = int(input("Enter Your Marks"))

if marks > 100 or marks == 0:
    print("Please Enter Valid Marks")

elif marks <= 90:
    print("Your Grade Is : B")

elif marks <= 70:
    print("Your Grade Is : C")

elif marks <= 60:
    print("Your Grade Is : D")

else:
    print("You Are Fail")

