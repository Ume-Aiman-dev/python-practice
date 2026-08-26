# Q. 1
def number(num):
    if num%2 == 0:
        print("EVEN")
    else:
        print("ODD")
number(56)

# Q. 2
def total():
    x = int(input("Enter your Matric marks : "))
    y = int(input("Enter your inter marks : "))
    sum = x + y
    percent =(sum / 2400) * 100
    print(f"Total marks: {sum}")
    print(f"Total marks: {percent}%")
total()

# Q. 3
def age_into_minutes(age):
    minutes = age * 365 *3600
    print(f"your age into minutes is: {minutes}")
age_into_minutes(18)
 