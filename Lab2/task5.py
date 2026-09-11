#  Create a dictionary where the keys are student names and the values are tuples
# containing each student's age and GPA. Perform the following operations:
# 1. Access and print the age and GPA of a specific student.
# 2. Update the GPA of one student.
# 3. Add a new student to the dictionary.
# 4. Remove a student from the dictionary. This task tests skills related to dictionary
# # manipulation, including accessing, updating, and deleting entries.

# 5
students = {
    "Ali": (20, 3.2),
    "Sara": (21, 3.8),
    "Ahmed": (19, 3.5)
}

age, gpa = students["Sara"]
print("Sara's Age:", age)
print("Sara's GPA:", gpa)

students["Ali"] = (20, 3.6)

students["Ayesha"] = (22, 3.9)

del students["Ahmed"]

print(students)
