# number = int(input("enter a number: "))
# if number > 50:
#     print("number is greater than 50 and it is :-")
#     if number % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("number is smaller than 50")

# number = int(input("enter a number"))
# if number > 90 :
#     print("number is greater than 90")
# else:
#     print("number is smaller than 90")

# # if statement
# num = int(input("enter a num"))
# if num % 2 == 0:
#     print(f"{num}  is even num ")
# else:
#     print(f"{num} is odd num")

# age = 18
# if age >= 18:
#     print("You are eligible to vote!")


# if-elif-else statement
# marks = 75
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("Grade: F")


# number = 10
# if number > 0:
#     if number % 2 == 0:
#         print("Positive Even Number")
#     else:
#         print("Positive Odd Number")
# else:
#     print("Not a Positive Number")

#
import datetime
# Current date and time
currentTime = datetime.datetime.now()
print("Current Date and Time:", currentTime)

# Extracting date and time
print("Year:", currentTime.year)
print("Month:", currentTime.month)
print("Day:", currentTime.day)
print("Hour:", currentTime.hour)
print("Minute:", currentTime.minute)
print("Second:", currentTime.second)

# Formatting date and time
formatted_time = currentTime.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date and Time:", formatted_time)
