# Task 3: Create a tuple that contains four integers. Attempt to modify one element of the
# tuple to demonstrate the immutability of tuples. After encountering the immutability error,
# convert the tuple into a list, modify the list, and convert it back into a tuple. Print the new
# tuple.

# 3
Thetuple=(1,2,3,.4,5);
# Thetuple[1]=25
Thelist=list(Thetuple)
Thelist[1]=25
Thetuple=tuple(Thelist)
print("New Tuple ",Thetuple)