# Task 4: Create a list of lists where each inner list contains three elements: a student's name,
# age, and GPA. Access and print the details of the second student. Next, sort the list of students
# in descending order based on their GPA and print the sorted list. Finally, add a new student’s
# record to the list and print the updated list.

# 4
students = [
    ["Ali", 20, 3.2],
    ["Sara", 21, 3.8],
    ["Ahmed", 19, 3.5],
    ["Ayesha", 22, 3.9]
]

print("Second student's details:", students[1])

students.sort(key=lambda student: student[2], reverse=True)

print("Students sorted by GPA:", students)

students.append(["Hassan", 20, 3.6])

print("Updated list:", students)
