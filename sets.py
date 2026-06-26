# =====================================================
# Topic: Sets in Python
# File Name: sets.py
# Author: Sakshi Adale
#
# Concepts Covered:
# - Creating Sets
# - Set Methods
# - Union
# - Intersection
# - Difference
# - Frozen Sets
#
# Description:
# This program demonstrates the basic concepts and
# operations of Python Sets.
# =====================================================

# Sets = Collection of unique elements, unordered, Unindexed and mutable. 
# It is a data structure that can be used to store multiple items in a single variable. Sets are useful when you want to eliminate duplicate values from a collection or when you want to perform mathematical operations like union, intersection, and difference.

#dishes = set(["Pizza", "Burger", "Pasta", "Salad", "Sushi"])
#print(dishes)
#print(type(dishes))

utensils = {"Fork", "Spoon", "Knife", "Chopsticks"}
dishes = {"Pizza", "Burger", "Pasta", "Salad", "Sushi"}

utensils.add("Plate")
print(utensils)
utensils.remove("Spoon")
print(utensils)
utensils.update(dishes)

dishes_table = dishes.union(utensils)

for x in dishes_table:
    print(x)

# Frozen sets = Immutable sets, meaning that once a frozen set is created, its elements cannot be modified or changed. Frozen sets are useful when you want to create a set that should not be modified accidentally or when you want to use a set as a key in a dictionary.
# Frozen sets do set of operations like union, intersection, and difference, but they do not support methods that modify the set, such as add() or remove().
frozen = frozenset({"Apple", "Banana", "Mango"})
print(frozen)
# print(frozen.add("Orange"))   # This would raise an error

# Union = Combine elements from both sets.
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b))

# Intersection = Return elements that are common to both sets.
a = {1,2,3}
b = {2,3,4}
print(a.intersection(b))

# Difference = Return elements that are in the first set but not in the second set.
a = {1,2,3}
b = {3,4,5}
print(a.difference(b))
print(b.difference(a))
