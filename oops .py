# object oriented programming

# hero class

# class Hero:
#     def __init__(self,name,health_power):
#         self .name = name
#         self .health_power = health_power

#     def decrease_health(self,power):
#         self.health_power -= power
#         return self.health_power



# # creating a object of hero class
# captain_america = Hero("steve",100)
# iron_man = Hero("tony",50)

# print(captain_america.name,captain_america.health_power,iron_man.name,iron_man.health_power)


# captain_america =Hero("steve",100)
# print(captain_america.health_power)
# captain_america.decrease_health(45)
# print(captain_america.health_power)

# class Dog:
#     def __init__(self,name,bread,age,colour):
#         self.name = name
#         self.bread = bread
#         self.age = age
#         self.color = colour

# bull = Dog("roshan","dungen",65,"pink")
# pog = Dog("anuj","dore",45,"purple")
# husky = Dog("sudip","nepali",20,"black_and_white")

# print(bull.name, bull.bread, bull.color, pog.name, bull.bread, bull.color, husky.name, husky.bread, husky.color)
 
# class Bank_Account:
#     def __init__(self,name,number,balance,history=[]):
#         self.name = name
#         self.number = number
#         self.balance = balance
#         self.history = history
#     def deposite(self,balance):
#             self.deposite += balance
#     def withdraw(self,balance):
#         self.withdraw -= balance
#     def fund_transfer(self,target_account,amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             target_account.balance += amount
#             return "Transfer successful"
#         else:
#             return "Insufficient balance"

#         self.history.append(f"Transferred {amount} to {target_account.name}")
#         target_account.history.append(f"Received {amount} from {self.name}")

#     def show_history(self):
#         print(f"\nTransaction History of {self.name}:")
#         if not self.history:
#             print("No transactions yet")
#         else:
#             for i in self.history:
#                 print("-", i)

# first_account = Bank_Account('sohan','1233abcd',10000)
# second_account = Bank_Account('puku','43251abce',1000)
# print(first_account.name,first_account.number,)

# first_account.fund_transfer(second_account,300)

# first_account.show_history()
# second_account.show_history()

# print("First Account Balance:", first_account.balance)
# print("Second Account Balance:", second_account.balance)

# encaplusulation
#  lass mobile:
#     def __init__(self,brand,model,price,ram):
#         self.__brand = brand
#         self.__model = model
#         self.__price = price
#         self.__ram = ram
        
# samsung = mobile("samsung","galaxy",20000,8)
# print(samsung._brand)  # will give error because of encapsulationc

