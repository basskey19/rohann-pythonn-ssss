def say_hello():
    print("hello Multiverse")


say_hello() 

def greet(name):#parameter name
    print(f"Hello,{name}!")#using the para

greet("Rohann")
greet("peter")

def sum(a,b):
    return a + b
print(sum(4,3))

def square(number):
    return number + number

result = square(7)
print("square:",result)

def greet(count):
    if count == 0:
        return
    print("hello",count)
    greet(count-1)
greet(7)    