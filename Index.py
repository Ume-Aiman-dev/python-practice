# # LEC 1 |
# print("Hello World!")
# # data types
# x = 26
# x = 10.23
# x = "hello"
# x = [1, 3, 5]
# x = {"jerry", 456, 56.7}
# x = {
#     "Name" : "Jerry",
#     "Age" : 26
# }
# x = (1, 2, 3, 4)
# x = None
# x = 0 + 9j
# x = False
# x = range(55)
# print(type(x))

# # LEC 2 |
# # Operators
# x = [10, 20, 30, 40, 50]
# print(10 in x)
# print(100 in x)
# print(10 not in x)
# print(100 not in x)
# # LEC 3 |
# # Arithmetic Operators
# x = int(input("Enter first number : "))
# y = int(input("Enter second number : "))
# a = x + y
# b = x - y
# c = x * y
# d = x / y
# e = x % y
# print ("additon :", a)
# print ("subtraction :", b)
# print ("multiplication :", c)
# print ("division :", d)
# print ("modulus :", e)

# # Decision Structure
# age = int(input("Enter your age : "))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# sp = int(input("Enter the shopping price:"))
# if sp > 5000:
#      print("20 percent off")
#      cuttamount = sp / 100 * 20
#      payable = sp - cuttamount
#      print(payable)
# else:
#     print("no off" , sp)

# # GRADED TASK
# # Q 1
# x = int(input("Enter a number :"))
# if x % 2 == 0:
#      print("Even")
# else:
#      print("Odd")
# # Q 2
# num = int(input("Enter a number:"))
# if num > 0:
#      print("Positive")
# elif num < 0:
#      print("Negative")
# else:
#      print("Zero")
# # Q 3
# age = int(input("Enter your age : "))
# if age >= 18:
#      print("Eligible to vote")
# else:
#      print("Not eligible to vote")
# # Q 4
# x = int(input("Enter 1st number :"))
# y = int(input("Entert 2nd number :"))
# if x > y:
#      print(x, "is larger")
# elif y > x:
#      print(y, "is larger")
# else :
#      print("Both numbers are equal")
# # Q 5
# marks = int(input("Enter marks out of 100 :"))
# if marks >= 50:
#      print("Pass")
# else:
#      print("Fail")

# # LEC 4 |
# # if_elif_elif.....else
# m_marks = int(input("Enter your Matric Marks :"))
# i_marks = int(input("Enter your Inter Marks :"))
# et_marks = int(input("Enter your Entry Test Marks :"))
# total = m_marks + i_marks + et_marks
# per = total / 3000 * 100
# print("Your per is :", per)
# if per > 90:
#      print("Medical Dept")
# elif per > 80:
#      print("Engg Dept")
# elif per > 70:
#      print("CSS Dept")
# elif per > 60:
#      print("Arts Dept")
# else:
#      print("No Addmision in any Dept")

# # Match exp.
# print("Welcome to our Cafe!")
# ch = int(input("1.Coffee 2.Tea 3.Brownie :"))
# q = int(input("Enter your quantity:"))
# match ch:
#      case 1:
#           print("250 per q")
#           t = q * 250
#           print("Your total bill is :", t)
#      case 2:
#           print("200 per q")
#           t = q * 200
#           print("Your total bill is :", t)
#      case 3:
#           print("700 per q")
#           t = q * 700
#           print("Your total bill is :", t)
#      case _:
#           print("Invalid choice!!!")
 
# name = input("Enter your Name :")
# age = int(input("Enter your Age :"))
# cnic = int(input("Enter your CNIC :"))
# acc = cnic * age
# balance = 1000
# print("Your acc has been created :")
# ch = int(input("1.balance check 2.widthrawal 3.addbalance 4.profile :"))
# match ch:
#      case 1:
#           print("Your acc balance is :", balance)
#      case 2:
#           w_account = int(input("Enter the widthrawal amount :"))
#           if w_account > balance:
#                print("Insufficient Balance!!!")
#           else:
#                r_balance = balance - w_account
#                print("Amount widhrawal remaining balance is :", r_balance)
#      case 3:
#           addb = int(input("Enter Balance you want to add :"))
#           newb = balance = addb
#           print("Your new balance is :", newb)
#      case 4:
#           print("Your Account has been created :", acc , "Initial Balance is", balance , name , age , cnic)
#      case _:
#           print("Invalid Choice!!!")

# # LEC 5 |
# # Loop structure
# x = [10, 20, 30, 40, 50]
# for i in x:
#      print(i)
# # tuple ex.
# y = {10 , 20.45 , "abc"}
# for i in y:
#      print(i)
# # string ex.
# name = "New York"
# for i in name:
#       print(i)
# # range ex.
# for i in range(10, 20, 3):
#      print(i)
# # Dict ex.
# data = {
#      "name" : "ali",
#      "age" : 20,
#      "cgpa" : 3.6
# }
# for k , v in data.items():
#      print(k ,"--", v)
# # list ex.
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in x:
#      if i%2 == 0:
#           print(i)
# for i in x:
#      if i != 0:
#           print(i)
# # list ex.
# fruit = ["apple", "banana", "mango"]
# for i in fruit:
#      if "n" in i:
#           print(i)
# # list ex.
# colour = ["red", "black", "navy_blue", "gray"]
# colour.append("mehroon")
# print(colour)
# # list ex.
# sum = 0
# shopping = [500, 1500, 2000]
# for i in shopping:
#      sum = sum + i
#      print("Your Total price is :", sum)

# # GRADED TASK
# # List Functions
# # 1. Append
# subjects = ["Math", "Science"]
# subjects.append("English")
# print(subjects)                               #Add the element

# # 2. Remove
# subjects = ["Math", "Science", "English"]
# subjects.remove("Science")
# print(subjects)                               # remove element

# # 3. Insert
# subjects = ["Math", "English"]
# subjects.insert(1, "Urdu")
# print(subjects)                               # insert the element in output

# # 4. Pop
# subjects = ["Math", "Urdu", "English"]
# subjects.pop()
# print(subjects)                               # Removes last value

# # 5. Sort
# marks = [78, 45, 92, 60, 45]
# marks.sort()
# print(marks)                                  # in ascending order

# # 6. Reverse
# marks = [45, 60, 78, 92]
# marks.reverse()
# print(marks)                                  # Reverse the order 

# # 7. Extend
# cities = ["Lahore", "Karachi", "Islamabad"]
# cities.extend(["Multan", "Murree"]) 
# print(cities)                                  # Join all element

# # ASSIGNMENT
# # Question 1
# # ELECTRICITY BILLING SYSTEM
# name = input("Enter Customer Name: ")
# cust_id = input("Enter Customer ID: ")
# units = int(input("Enter Units Consumed: "))
# if units <= 100:
#     bill = units * 15
# elif units <= 200:
#     bill =(100 * 15) + (units - 100) * 20
# else:
#     bill = (100 * 15) + (100 * 20 ) + (units - 200) * 30
# print("___ Electricity Bill ___")
# print("Customer Name:", name)
# print("Customer ID: ", cust_id)
# print("Units Consumed: ", units)
# print("Total Bill: RS.", bill)
# # Question 2
# # Employee Salary Management System
# name = input("Enter Employee Name: ")
# emp_id = input("Enter Employee ID: ")
# basic_salary = float(input("Enter Basic Salary: "))
# experience = int(input("Enter Years of Experience: "))
# if experience <= 2:
#  bonus_percent = 0
# elif experience <= 5:
#  bonus_percent = 10
# elif experience <= 10:
#  bonus_percent = 20
# else:
#  bonus_percent = 30
# bonus = (bonus_percent / 100) * basic_salary
# net_salary = basic_salary + bonus
# print("\n--- Salary Slip ---")
# print("Employee Name:", name)
# print("Employee ID:", emp_id)
# print("Basic Salary:", basic_salary)
# print("Bonus:", bonus)
# print("Net Salary:", net_salary)
# print("You got", bonus_percent, "% bonus!")

# # LEC 6 |
# # List Comprehensive
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in x:
#     if i%2  == 0:
#         print(i)
# # Same Code in one line
# print([i for i in x if i%2 == 0])

# y = ["Ali", "Ahmad", "Umer"]
# for i in y:
#     if "a" in i:
#         print(i)
# # Same Code in one line  
# print([i for i in y if "a" in i])      

# for i in range(1,11,1):
#     print("2 X", i , " = ", 2*i)
# # Same Code in one line
#     print([2*i for i in range(1,11,1)])

# for i in range(1,7,1):
#     print(i*1)
# # Same Code in one line
# print(x*x for x in range(1,7,1))

# numbers = [1, 2, 3, 4, 5, 6]
# for i in numbers:
#     if i%2 == 0:
#         print("Even", i)
#     if i%2 != 0:
#         print("Odd", i)

# # Same Code in one line
# print(i for i in x if i%2 == 0)
# print(i for i in x if i%2 != 0)

# #  While Loop
# print("shope!!")
# cart = []
# cond = True
# while cond:
#     ch = int(input("1.i1 2.i2 3.i3 4.Exit"))
#     match ch:
#         case 1:
#             print("200 price")
#             q = int(input("Enter quantity :"))
#             t = q * 200
#             cart.append(t)
#         case 2:
#             print("300 price")
#             q = int(input("Enter quantity :"))
#             t = q * 300
#             cart.append(t)
#         case 3:
#             print("400 price")
#             q = int(input("Enter quantity :"))
#             t = q * 400
#             cart.append(t)
#         case 4:
#             cond = False
#         case _:
#             print("Invalid try again!!")
# sum = 0
# for i in cart:
#     sum = sum + i
# print("Total price is :" , sum)

# #  LEC 7 |
# # Functions
# def abc():
#     print("My first Function is called ")
#     print("My hometown is Lahore!!!")
# abc()
# # 2nd exp. 
# def sum(a,b):
#     c = a + b
#     print(f"The Sum of two number is : {c}")
# sum(89,98)
# # 3rd exp.
# def age_into_days(age):
#     days = age * 365
#     print(f"your age into days is: {days}")
# age_into_days(43)
# # 4th exp.
# d = {}
# def add_dict(key , value):
#     d.update({key : value})
#     print(d)
# add_dict("age" , 23)
# add_dict("cgpa" , 3.65)
# # 5th exp.
# def c_into_f(tem):
#     f = (tem * 1.8) + 32
#     print(f"Your {tem}C is equal to {f}F")
# c_into_f(32)
# # 6th exp.
# def predict_diabetes(bmi, bp, gl):
#     risk = (bmi * 0.5) + (bp * 0.5) + (gl * 0.5)
#     if risk >= 100:
#         print("Diabetic")
#     else:
#         print("Non Diabetic")
# predict_diabetes(5, 80, 80)

# Basic Python is done here NOW,
# OOP is started from here
# 1st exp.
class Car:
    def __int__(self , model , year):
        self.model = model
        self.year = year

    def start(self):
        print("Car Start!!!")

    def stop (self):
        print("Car Stop!!!")

    def gear_change(self):
        print("Gear change!!")
# 2nd exp.
class Employee:
    def __int__(self,n , s , d):
        self.name = n
        self.salary = s
        self.designation = d

    def duty_time():
        print("9 hours")

    def dept(self):
        print(self.name ,"IT dept")

    def break_hour():
        print(self.name , "only one hour")

ali = Employee