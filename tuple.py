# A tuple is an immutable ordered collection of elements.
# Use for grouping together related data.
# A tuple is created by placing all the items inside parentheses (), separated by commas.
# Creating a Tuple
tup = ()
print(tup)
# Using String
tup = ('Sakshi', 'Adale')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Python')
print(tup)
# Tuple unpacking
tup = (100, 200, 300)

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)
# Program 
student = ("Student",21, "Female")

print(student.count(21))
print(student.index("Female"))

for x in student:
    print(x)

if "Female" in student:
    print("Yes, 'Female' is in the student tuple.")




