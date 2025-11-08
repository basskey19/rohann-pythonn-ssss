fruitsSet = {"apple","bannana","cherry","apple"}
print("fruits in the set :",fruitsSet)
fruitsSet.add("pineapple")
print("fruits after adding:",fruitsSet)
fruitsSet.remove("cherry")
print("fruits after removing :",fruitsSet)

numbers = {1,2,3,4,5,1,2}
print("number set :",numbers)
numbers.add(6)
print("after adding 6:",numbers)
numbers.remove(3)
print("after removing 3:",numbers)
numbers = {1,2,3,4,5,1,2}
print("numbers set:",numbers)
numbers.add(6)
print("after removing 3:",numbers)

set1 = {1,2,3}
set2 = {3,4,5}

print("union:",set1.union(set2))

print("intersection:",set1.intersection(set2))

print("difference(set1 - set2):",set1.difference(set2))
