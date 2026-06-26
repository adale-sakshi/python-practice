# =====================================================
# Topic: Dictionaries in Python
# File Name: dictionaries.py
# Date: 26-06-2026
# Author: Sakshi Adale
#
# Concepts Covered:
# - Dictionary Creation
# - Accessing Values
# - get()
# - keys()
# - values()
# - items()
# - update()
# - pop()
# - popitem()
# - Iterating through Dictionary
# =====================================================

# Dictionary = Collection of key-value pairs, ordered, changeable, and does not allow duplicate keys.

a = {"x": 1,
     "y": 2,
     "z": 3}
print(a)

#Acessing items in a dictionary
d = {"name": "Dog", "age": 5}
print(d["name"])
print(d.get("age"))
print(d.get("Color"))

# Example 
capitals = {"India": "New Delhi",
            "USA": "Washington D.C.",
            "France": "Paris",
            "Japan": "Tokyo"}

print(capitals["India"])
print(capitals.get("USA"))
print(capitals.get("Canada"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals.update({"Germany": "Berlin"}))
print(capitals)
print(capitals.pop("India"))
print(capitals.popitem())
print(capitals)

# Iterate Key-Value Pairs

for key, value in capitals.items():
    print(key, value)

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

