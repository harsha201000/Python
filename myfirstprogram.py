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
#Student_name_in_grade_8.append("Lilly")
#print(Student_name_in_grade_8)


