class Bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("invalid amount!!!")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. Remaining amount: {self.__balance}") 
        else:
            print("insufficent balance or Invalid amount !!!")

account = Bankaccount("Rohann",7000)
print("account owner :",account.owner)
print("initial balance: ", account.get_balance())
account.deposit(3000)
account.withdraw(2000)                                                   