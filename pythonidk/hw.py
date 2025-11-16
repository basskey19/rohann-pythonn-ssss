class Animal():
    def __init__(self, name):
        self.name = name
        print(f"{self.name}'s object has been created")

    def sound(self):
        print(f"{self.name} is now making sound")

    def walk(self):
        print(f"{self.name} is now walking")

    def __del__(self):
        print(f"{self.name} object has been deleted")

dog = Animal("Buddy")
dog.sound()
dog.walk()

cat = Animal("billu")
cat.sound()
cat.walk()

del dog
del cat
cat.sound() # this line will give err


#
class Student:
    def __init__(self, name, age, grade):
        # Constructor: Automatically called when a new object is created
        self.name = name
        self.age = age
        self.grade = grade
        print(f"\nStudent record created for {self.name}.")

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

    def updateGrade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade has been updated to {self.grade}.")

    def __del__(self):
        # Destructor: Automatically called when the object is deleted or program ends
        print(f"Student record for {self.name} has been deleted.")

# Main program starts here
if __name__ == "__main__":
    print("Welcome to the Student Management System")

    # Creating first student using constructor
    student1 = Student("Anjali", 14, "8th")
    student1.showDetails()

    print("\nUpdating student grade...")
    student1.updateGrade("9th")

    print("\nCreating one more student...")
    student2 = Student("Rahul", 15, "9th")
    student2.showDetails()

    print("\nNow deleting Rahul's record...")
    del student2  # Destructor will be called here

    print("\nProgram is ending... remaining student records will be deleted automatically.")




class Person:
    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Hello, {self.name}! Your age is {self.age}. Object has been created !")


    # Method to display a greeting
    def greet(self):
        print(f"Welcome, {self.name}! Have a great day!")

    # Destructor to clean up
    def __del__(self):
        print(f"Goodbye, {self.name}! Your data is being deleted.")

# Creating an object of the Person class
print("Creating a Person object...")
person1 = Person("Sadia", 25)  # Constructor is called here

# Using the greet method
print("Calling the greet method...")
person1.greet()

# Deleting the object
print("Deleting the Person object...")
del person1  # Destructor is called here




#//////////////////////////

# Step 1: Create a class
class BankAccount:
    # Step 2: Constructor to initialize account details
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        print(f"Account created for {self.name} with Account Number: {self.account_number}")

    # Step 3: Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            # self.balance = self.balance + amount
            self.balance += amount
            print(f"{amount} deposited successfully. Current Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    # Step 4: Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully. Current Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    # Step 5: Destructor to clean up resources
    def __del__(self):
        print(f"Account for {self.name} is being deleted.")

# Step 6: Creating objects (accounts) of the class
print("\n--- Creating Accounts ---")
account1 = BankAccount("Izyan", "1234567890", 500)  # Constructor called
account2 = BankAccount("Faiq", "1123421112", 1000)
account3 = BankAccount("Sadia", "09876513121", 1000)

# Step 7: Performing operations
print("\n--- Account Operations ---")
account1.deposit(200)
account1.withdraw(100)

account2.deposit(500)
account2.withdraw(1200)

# Step 8: Delete an object manually
print("\n--- Deleting an Account ---")
del account1  # Destructor called manually
