# Task 2: Two sets of students need to be managed. The first set contains five student names,
# while the second set contains three student names, some of which may overlap with the first
# set. Perform the following operations:
# 1. Calculate and print the union of both sets (all unique students).
# 2. Calculate and print the intersection of both sets (students common to both groups).
# Calculate and print the difference between the first and second sets (students in the first set
# but not in the second). This task evaluates understanding of set operations, including union,
# intersection, and difference.

# 2
set1={"A","B","C","D","E"}
set2={"F","A","G"}

print("Union ",set1.union(set2))
print("Intersection ",set1.intersection(set2))
print("Difference ",set1.difference(set2))