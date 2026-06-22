# Topic: Python Lists
# Date: 22-06-2026
# Practiced common list operations and methods
# List is a built-in data structure used to store an ordered collection of items.
# Mutable: list elements can be changed, update, added and removed.
# Index-based: elements are accessed using their position, starting from index 0.
# List creating: 1) Using Square Brackets [], 2) Using list() Constructor and 3) Creating List with Repeated Elements.
# Program 1:
l = [10,20,30,40,50]

l.insert(1,15)
print(l)
print(15 in l)
print(l.count(30))
print(l.index(20))
print(l.clear())

# Program 2:
s = [10,20,30,40,50,60,70,80]

s.remove(20)
print(s)
print(s.pop(1))
print(max(s))
print(min(s))
print(sum(s))
s.reverse()
print(s)
s.sort()
print(s)
