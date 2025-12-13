with open("sample.txt","r")as file:
    print("reading only part of the line (10 characters):")
    print(file.read(10))

with open("sample.txt","r")as file:
    print("\nreading one single line: ")
    print(file.readline())

with open("sample.txt","r")as file:
    print("\nreading first three lines")
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open("sample.txt","r")as file:
    print("\nreading all lines in a list:")
    print(file.readlines())

with open("sample.txt","r")as file:
    print("\nlooping through file lines:")
    for line in file:
        print(line.strip())                