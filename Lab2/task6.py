# Create a dictionary where each key is a subject name (e.g., 'Math', 'Science') and the
# corresponding value is a set of student names enrolled in that subject. Perform the following
# operations:
# 1. Add a new student to the 'Math' subject.
# 2. Remove a student from the 'Science' subject.
# 3. Identify and print the students enrolled in both 'Math' and 'Science' using set
# intersection.
# 4. Identify and print all unique students across all subjects using set union. This task tests
# the ability to combine dictionaries with sets and perform operations such as
# intersection and union in a multi-dimensional context.

# 6
subjects = {
    "Math": {"Ali", "Sara", "Ahmed"},
    "Science": {"Sara", "Ahmed", "Ayesha"}
}

subjects["Math"].add("Hassan")

subjects["Science"].remove("Ayesha")

both = subjects["Math"].intersection(subjects["Science"])
print("Students in both Math and Science:", both)

all_students = subjects["Math"].union(subjects["Science"])
print("All unique students:", all_students)
