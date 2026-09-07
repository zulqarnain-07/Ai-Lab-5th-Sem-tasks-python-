# Task 4: Student Performance Predictor
# Write a Python program that takes a student's marks as input and predicts their performance.

marks = int(input("Enter marks: "))

if marks >= 80:
    print("Excellent")
elif marks >= 70:
    print("Good")
elif marks >= 60:
    print("Average")
elif marks >= 50:
    print("Needs Improvement")
else:
    print("At Risk")
