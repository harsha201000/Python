# Python Demo Code

# Hello World Program in Python 3
print("Hello World")
print("Welcome to Python")
print("Harsha First Python Program")

#Comparing two numbers
a = 1
b = 2
print("a = {}, b = {}".format(a, b))
if b > a:
    print("{} is greater than {}".format(b,a))
else:
    print("{} is greater than {}".format(a,b))
	
# Arithmetic Operations

print("Program Start")
x = 13
y = 10

print("x = {}, y = {}".format(x, y))

#Addition
z = x + y
print("Addition {}".format(z))

#Subtraction
z = x - y
print("Subtraction {}".format(z))

#Multiplacation
z = x * y
print("Multiplacation {}".format(z))

#Division
z = x / y
print("Division {}".format(z))

#Modulus
z = x % y
print("Modulus {}".format(z))

#Exponentation
z = x ** y
print("Exponentation {}".format(z))

#Floor Division
z = x // y
print("Floor Division {}".format(z))

Name = "Harsha"
print(Name)

Name = input("Enter your Name: ")
print(Name)

# Casting or type casting
#If you want to specify the data type of a variable, this can be done with casting. int() float() str()

Number = 1 
print(int(Number))
print(float(Number))
print(str(Number))

# Addition of two integers 
a = 10 
b = 20 
print(a+b)
# Addition of two float
a_f = 10.57 
b_f = 20.66 
print(a_f+b_f)
# Addition of two string
a_s = "10.57" 
b_s = "20.66" 
print(a_s+b_s)
a_a = "A"
b_b = "B"
print(a_a + b_b)

#How to check the type of data we have.command:  type() 
print(type("Hello"))
print(type(10))
print(type(12.10))

#Variables are case sensitive : The variable name needs to be exaclty the same when declared multiple times. 

a1 = 10 
#print(A1+2) will give you an error A1 is not same as a1
print(a1 + 2)

#Rules for Variable name
#Variable Names
#A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables.
x = 10
age = 13
print(age)
#A variable name must start with a letter or the underscore character
_age = 29 
print(_age)
#A variable name cannot start with a number
#1a = 20  - output is an error 

#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Name_1 = "John"
#a$ = 10 
#print(a$) special charcter are not allowed

#Variable names are case-sensitive (age, Age and AGE are three different variables)

#A variable name cannot be any of the Python keywords.

#int = 10 - output is an error because int is a python command / keyword

help("keywords")

#Note : During a problem statement based python program , no two variable has to have a same name.

#Declaring multiple variable with different value 
x1,y1,z1 = "Harsha" , "Sam" , "Jack"
print(x1)
print(y1)
print(z1)
#Declaring multiple variable with single value 
x2 = y2 = z2 = " Hello "
print(x2)
print(y2)
print(z2)

#Built-in Data Types
#In programming, data type is an important concept.

#Variables can store data of different types, and different types can do different things.

#Python has the following data types built-in by default, in these categories:

#1 .Text Type:	str
#2. Numeric Types:	int, float, complex
#3. Sequence Types:	list, tuple, range
#4. Mapping Type:	dict
#5. Set Types:	set, frozenset
#6. Boolean Type:	bool
#7. Binary Types:	bytes, bytearray, memoryview
#8. None Type:	NoneType 

# Sequence Types:	list, tuple, range
Numbers = range(0,10)
print(Numbers)

#List : It collection of data. 
#Rule 1 = [ ]
Student_name_in_grade_7 = ["Harsha" ,"John" ,"Sam"]
print(Student_name_in_grade_7)
#Rule 2 = Multiple types of data is possible in list 
Stduent_info = ["Harsha" , 8 , 9.2]
#Assigning of value after declaration is possible 
Student_name_in_grade_7 = ["Harsha" ,"John" ,"Sam"]
# to add value , we used append 
Student_name_in_grade_7.append("Lilly")
print(Student_name_in_grade_7)
#Tuple : It is collection of data, once declared , you cannot change. 
#Rule 1 = ( )
Student_name_in_grade_8 = ("Deo" ,"Drake" ,"Steve")
print(Student_name_in_grade_8)
#Rule 2 = Multiple types of data is possible in tuple
Stduent_info_t = ("Harsha" , 8 , 9.2)
#Assigning of value after declaration is not possible 
#Student_name_in_grade_8 = ("Deo" ,"Drake" ,"Steve")
#Student_name_in_grade_8.append("Drew")
#print(Student_name_in_grade_8)


Number = 2
if Number == 2:
    print("The Number value is equal to 2")

Number1 = 3
if Number1 == 2:
    print("The Number value is equal to 2")

Number2 = 3
if Number2 == 3:
    print("The Number value is equal to 3")
else:
    print("The Number value is not equal to 3")

rule1 = input("if you have a student representative card: Type Yes.: ")
rule2 = input("if you have a student unique test id number: Type Yes.: ")
if (rule1 == "Yes") and (rule2 == "Yes"):
    print("Eligible for the test")
else:
    print("Not Eligible for the test")

age = 18
if age>17 and age<25:
    print("Eligible")
else:
    print("Not Eligible")

yellow = True
red = True

if (yellow == True) ^ (red == True):
    print("Eligible")
else:
    print("Not Eligible")

A = 10

if not A == 10:
    print("A is not equal to 10")


#List : Negative Indexing
value1 = [10, 20, 30, 40]
#Total length of the list
print(len(value1))
#positive indexing
print(value1[0])
print(value1[1])
print(value1[2])
print(value1[3])
#negative indexing
print(value1[-4])
print(value1[-3])
print(value1[-2])
print(value1[-1])
#updating values
value1.append(56) #can add only one value at the end
print(value1)
value1.extend([46, 89, 79]) #can add multiple value at the end
print(value1)
value1.insert(2,89) # add value at particular location
print(value1)
#update value
value1[2] = 95
print(value1)

#Exercise 1: Reverse the list in python
numbers = [10, 20, 30]
numbers.reverse()
print(numbers)

#Exercise 2: Concatenate two lists index-wise using zip()
message1 = ["M", "na", "i", "Har"]
message2 = ["y", "me", "s", "sha"]
message3 = [i+j for i , j in zip(message1,message2)]
print(message3)

#Exercise 3: Concatenate two lists
message4 = ["M", "na", "i", "Har"]
message5 = ["y", "me", "s", "sha"]
message6 = message4 + message5
print(message6)

#Exercise 4: Turn every item of a list into its square
list_numbers = [10, 20, 50, 100]
square_list = []
for i in list_numbers:
    square = i*i
    square_list.append(square)
print(square_list)

#Exercise 5: Remove all occurance of specific value in list
#remove number 100 from the list
repeat_list = [10, 20, 50, 100]
for i in repeat_list:
    if i == 100:
        repeat_list.remove(100)
print(repeat_list)


#Summation of natural number 5 : 5 + 4 + 3 + 2 + 1
Number = int(input("Enter the natural number for summation: "))
Sum1 = 0
for i in range(Number,0,-1):
    print( Sum1 , " + " ,i)
    Sum1 = Sum1 + i
    print("The count value is " , i)
    print("The sum value is " , Sum1)
print("----------------------")
print("The sum of n natural number : " , Sum1)

# Factorial of a natural number : 5! = 5 x 4 x 3 x 2 x 1
# Factorial of a natural number : 11! = 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1

Number1 = int(input("Enter the product of natural number : "))
product1 = 1
for i in range(Number1,0,-1):
    print( product1 , " x " ,i)
    product1 = product1 * i
    print("The count value is " , i)
    print("The product of n natural number is " , product1)
print("----------------------")
print("The product of n natural number : " , product1)

#Typecasting : Converting a data from one data type to the other data type.

#How to find the type of data you have.
value = 10
print(type(value))

#Convert a string into integer , float, list, tuple, set
n1 = "1"
print(type(n1))
n1_i = int(n1)
print(n1_i)
print(type(n1_i))
n1_f = float(n1)
print(n1_f)
print(type(n1_f))
n1_l = list(n1)
print(n1_l)
print(type(n1_l))
n1_t = tuple(n1)
print(n1_t)
print(type(n1_t))
n1_s = set(n1)
print(n1_s)
print(type(n1_s))

# Index : It is a position value of data inside a list,tuple,dict
fruits = ["Apple", "Mango" ,"Grapes"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

#String datatypes and it's methods
#len() : Its total char with space
message = "Hello World"
#length of message
print(len(message))
#index of string
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])
print(message[6])
print(message[7])
print(message[8])
print(message[9])
print(message[10])
#To check if World is present in message or not
print("World" in message)
print("Happy" in message)
#To check if Happy is not present in message
print("Happy" not in message)
#Slicing: To extract a part of the data value
#Variable_name[start_number : end_number +1 ]
#Value represented from count start_number to the end_number
print(message[1:4])
print(message[5:7])
#Value represented from count 0 to the end_number
#Variable_name[:end_Number + 1]
print(message[:7])
#To convert a string into a uppercase letter
All_letter_cap = message.upper()
print(All_letter_cap)
#To convert a string into a lowercase letter
All_letter_small = message.lower()
print(All_letter_small)
#To convert a string into a Cap the first letter
All_letter_cap = message.capitalize()
print(All_letter_cap)
#To remove white space and convert it into a list
All_white_space_remove = message.split()
print(All_white_space_remove)
#String Concatentation is to add two string(data types) using a + symbol
message1 = "Hello, Welcome to Codeyoung"
message2 = "You have successfully enrolled into Python classes"
print(message1 + " " + message2)
#format operator
age = "you are 13 years old"
info = "Hello , Harsha " + age
print(info)
info1 = "Hello , Harsha , welcome to {}"
print(info1.format("Codeyoung"))
name = "Harsha"
age1 = 13
print("Hello {} , Welcome to Codeyoung. You are {} years old ".format(name, age1))
#Python program to demonstrate the use of swapcase method
string = "gEEksFORgeeks"
#prints after swapping all cases
print(string.swapcase())
string = "geeksforgeeks"
print(string.swapcase())
string = "GEEKSFORGEEKS"
print(string.swapcase())
str = "I love Geeks for geeks"
print(str.partition("for"))
string = "grrks FOR grrks"
#replace all instances of 'r'(old) with 'e'(new)
new_string = string.replace("r","e")
print(string)
print(new_string)
my_string = "Hello World!"
stripped_string = my_string.strip()
print(stripped_string)
str = '-'.join('hello')
print(str)

#Number Systems
#The numbers we deal with everyday are of the decimal(base 10)number system but computer programmers need to work with binary(base 2), hexadecimal(base 16) and octal(base 8) number systems.
#In Python, we can represent these numbers by appropriately placing a prefix before that number. The following table lists these prefixes.

#Number System   Prefix
#Binary 0b or 0B
#Octal 0o or 0O
#Hexadecimal 0x or 0X

print(0b1101011) #prints 107
print(0xFB + 0b10) #prints 253
print(0o15) #prints 15

#Explicit Type Conversion
#We can also use built-in functions like int(),float(), and complex() to convert between types explicitly. These functions can even convert from strings.

num1 = int(2.3)
print(num1) #prints 2

num2 = int(-2.8)
print(num2) #prints -2

num3 = float(5)
print(num3) #prints 5.0

num4 = complex('3+5j')
print(num4) #prints (3 + 5j)

#Math Module
import math

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))

import random
#modulename.builtinfunction()
s = random.seed(2)
print(s)

#random : prints value raging from 0 to 1 only
a = random.random()
print(a)
b = random.random()
print(b)

#getstate() Returns the current internal state of the random number generator
print(random.getstate())
#The setstate() method is used to restore the state of the random number generator back to the specified state Use the getstate() method to capture the state
set_state_value = random.getstate()
print(random.setstate(set_state_value))
#random.randrange(start,end) Returns the value from start number to end number, the value can be a decimal or integer.
c = random.randrange(1,10)
print(c)
#random.randint(start,end) Returns the value from start number to end number, the value is a integer.
d = random.randint(1,10)
print(d)
#choice : It will help you to select a value from a list
fruits = ['apple', 'mango', 'pear']
choice_value = random.choice(fruits)
print(choice_value)
#choices : It will help you to select a value from multiple list.
choice_value_multiple = random.choices(fruits, weights = [10, 1, 1], k = 14)
print(choice_value_multiple)

random.shuffle(fruits)
print(fruits)

# for loop will perform a task at once for a number of time.
for i in range(1, 10):
    print("Hello World")
# Function : it is a block of code. You will write a code only once. But during programming you will use it multiple times.

#step1: To create a code block
def welcome():
    print("Hello World")

#step2: To call the function using the name of the function. If you do not call the function, the code will be at rest.
welcome()

#second time
welcome()

#Why we need function:
#Standard Function: The block code is already present in python file. You simply call the name of the function.
#input()
#int()
#float()

#file name = time
#inside time file
#commands present inside a file called time
#date()
#time()
#time.sleep()

#The terminal is not activated for library files
#tell computer to conside time file and activate it. by using import filename.
#import random

wake_up_time = 0
breakfast_time = 0

#robot_command function
def robot_command():
    print("Wake Up Time: ", wake_up_time)
    print("Wake up Harsha")
    print("Breakfast Time: ", breakfast_time)
    print("Time for breakfast Harsha")

#regular code
day_count = int(input("Enter the day count: "))
wake_up_time = input("Set the time: ")
breakfast_time = input("Set the time: ")
for day in range(1, day_count + 1):
    print("Day ", day)
    robot_command()

# Types of functions in python
# global variable : variable declared outside a def block
num1 = 10
num2 = 20

def add():
    sum = num1 + num2
    print("Addition: {}".format(sum))
add()
# global variable can be accessed by multiple functions
def subtract():
    difference = num2 - num1
    print("Subtraction: {}".format(difference))
subtract()
# local variable : variable declared inside a def block

def addition():
    a = 10
    b = 20
    addition_result = a + b
    print("Addition : {}".format(addition_result))
addition()
#local variable can not be used in multiple def block
def subtraction():
    a = 10
    b = 20
    subtraction_result = b - a
    print("Subtraction : {}".format(subtraction_result))
subtraction()

#type of def function
#arguments and parameters
def welcome(first_name,last_name):
    print("Hello {} {}, Welcome to Codeyoung".format(first_name, last_name))
welcome("Harsha", "Malipeddi")

#functions with value assigned in def.

def grade(name,section=8):
    print("Name : {} Grade : {}".format(name, section))
grade("Harsha")

#functions with value assigned in def.

def grade(name="Harsha",section=8):
    print("Name : {} Grade : {}".format(name, section))
grade()

#functions with value assigned in def.

def value(*i):
    print(i)

value([1,2,3,4,5])
value(1,2,3,4,5)

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 9
print("The factorial of {} is {}".format(num,factorial(num)))

# Pass : the keyword is used when you want to leave a block empty
def a():
    pass
a()
for i in range(0,10):
    pass
if (a == 10):
    pass
print("_______________________")
for i in range(0,10):
    if i == 5:
        continue
    print(i," sec")
print("________________________")
for i in range(0,10):
    if i == 5:
        print("Ring")
        continue
    print(i," sec")
print("________________________")
for i in range(0,10):
    if i == 5:
        print("Ring")
        break
    print(i," sec")
	
# two inputs: number 1 and number 2 as input
# addition
num1 = 10
num2 = 20
sum = num1 + num2
print("Sum: {}".format(sum))

difference = num1 - num2
print("Difference: {}".format(difference))

product = num1 * num2
print("Product: {}".format(product))

quotient = num1 / num2
print("Quotient: {}".format(quotient))

# class programming language
class calculate:
    # instantation : input and output variable
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    # method : task function
    def add(self):
        result = self.num1 + self.num2
        print("Sum: {}".format(result))
    def subtract(self):
        result = self.num1 - self.num2
        print("Difference: {}".format(result))
    def multiply(self):
        result = self.num1 * self.num2
        print("Product: {}".format(result))
    def divide(self):
        result = self.num1 / self.num2
        print("Quotient: {}".format(result))

# create an object
object = calculate(50,100)
object.add()
object.subtract()
object.multiply()
object.divide()

class greet:
    def __init__(self,name):
        self.name = name
    def greeting(self):
        print("Welcome to codeyoung {}".format(self.name))
codeyoung = greet("Harsha")
codeyoung.greeting()

class Animal:

    # attrbute and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")

# inherit from Animal class
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is {}".format(self.name))

# create an object of the subclass
dog = Dog()

# access superclass attribute and method
dog.name = "Rohit"
# call subclass method
dog.display()
dog.eat()

#parent class
class login_id: #super class
    def login(self):
        name = input("Create a username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        print("Name {}".format(name))
        print("Email {}".format(email))
        print("Successfully registered")

class Sandbox(login_id): #sub class : 
    def login(self):
        super().login()
        print("Home / Workbench / Files / Learning Content / Exercises")

class teacher_login(login_id): #sub class:
    def login(self):
        super().login()
        print("Home / Workbench / Files / Learning Content / Exercises / Tracker")

print("Student Portal - Sandbox")
codeyoung = Sandbox()
codeyoung.login()

class SuperClass:
    def super_method(self):
        print("Super class method called")

# define class that derive from SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):
    def derived2_method(self):
        print("Derived class 2 method called")

# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()

d2.derived1_method()

d2.derived2_method()

class SuperClass1:
    def info(self):
        print("Super class 1 method called")

class SuperClass2:
    def info(self):
        print("Super class 2 method called")

class Derived(SuperClass1, SuperClass2):
    pass

d1 = Derived()
d1.info()

class grandparents:
    def brown_skin(self):
        print("Brown skin - Grandparents")

class parents(grandparents):
    def mom(self):
        print("Curly Hair Mom")

class child(parents):
    def age(self):
        print("13 year old")

# Harsha has access to super and derived class
harsha = child()
harsha.brown_skin()
harsha.mom()
harsha.age()
#parents
p1 = parents()
p1.mom()
p1.brown_skin()

import datetime
from datetime import date
from datetime import time


# get the current date and time
now = datetime.datetime.now()

print(now)

# get current date
current_date = datetime.date.today()

print(current_date)

print(dir(datetime))

d = datetime.date(2010, 4, 19)
print("My date of birth is {}".format(d))

#today() to get the current date 
todays_date = date.today()
print("Todays date is {}".format(todays_date))

timestamp = date.fromtimestamp(1326244364)
print("Date = {}".format(timestamp))

# date object of today's date
today = date.today()

print("Current year: {}".format(today.year))
print("Current month: {}".format(today.month))
print("Current day: {}".format(today.day))

# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time(hour, minute, and second)
b = time(10, 9, 23)
print(b)

# time(hour, minute, and second)
c = time(hour = 10, minute = 9, second = 23)
print(c)

# time(hour, minute, second, microsecond)
d = time(10, 9, 33, 234566)
print(d)

a = time(5, 0, 0)

print("Hour: {}".format(a.hour))
print("Minute: {}".format(a.minute))
print("Second: {}".format(a.second))
print("Microsecond: {}".format(a.microsecond))

from datetime import datetime

# datetime(year, month, day)
a = datetime(2022, 9, 12)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2023, 9, 18, 5, 42, 59, 234567)
print(b)

c = datetime(2010, 4, 19, 10, 20, 1, 324567)

print("Year: {}".format(a.year))
print("Month: {}".format(a.month))
print("Hour: {}".format(a.hour))
print("Minute: {}".format(a.minute))
print("Timestamp: {}".format(a.timestamp()))

# using date()
t1 = date(year = 2020, month = 5, day = 20)
t2 = date(year = 2015, month = 12, day = 7)

t3 = t1 - t2
print("t3 = {}".format(t3))

# using datetime()
t4 = datetime(year = 2023, month = 7, day = 21, hour = 10, minute = 30, second = 50)
t5 = datetime(year = 2017, month = 12, day = 12, hour = 7, minute = 12, second = 55)

t6 = t4 - t5
print("t6 = {}".format(t6))

print("Type of t3 = {}".format(type(t3)))
print("Type of t6 = {}".format(type(t6)))

