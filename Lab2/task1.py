# Task 1: Create a list that contains five student names. After the list is created, add two more
# student names. Then, remove one student from the list. Sort the final list of names
# alphabetically and print the length of the list (i.e., the number of students).

# 1
students = ["Zulqarnain","Zack","ali","samar","HAHHAAHA"];
students.append("hehehehhe");
students.append("lalalalla");
print(students);
students.remove("ali");
students.sort();
print(students);
print("Number of students",len(students))