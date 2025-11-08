fruits = ("apple","bannana","cherry","apple","pineapple")

print("fruit tuple:",fruits)

print("first fruit:",fruits[0])
print("second fruit:",fruits[1])

print("last fruit:",fruits[-1])

print("first two fruits :",fruits[0:2])

count = 1
for i in fruits:
    print(f"fruit number {count} is {i}")
    count += 1

print("apple count",fruits.count("apple")) 

print("index of banana:",fruits.index("banana"))