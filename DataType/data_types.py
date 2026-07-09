# String data type

# Literal assigment
first_name = "Laura"
last_name = 'Pinheiro'

# print(type (first_name))  # <class 'str'>
# print(type (last_name))   # <class 'str'>
# print(type(first_name) == str) # True
# print(isinstance(first_name, str)) # True 

# Constructor Function
# pizza = str("Pepperoni")
# print(type (pizza))   # <class 'str'>
# print(type(pizza) == str) # True
# print(isinstance(pizza, str)) # True

# Concatenation
# full_name = first_name + " " + last_name
# print(full_name)  # Laura Pinheiro

# full_name += " is a software engineer"
# print(full_name)  # Laura Pinheiro is a software engineer 

# Casting a number to a string
# age = str(29)
# print(type(age))  # <class 'str'>
# print(age)  # "29"  

# statement = "I am " + age + " years old"
# print(statement)  # I am 29 years old

# Multiple lines
multiline_string = '''
                      Hey, how are you doing?                         

I am doing well, thanks for asking!               
                      All good?         
'''
# print(multiline_string)

# Escape characters
# escaped_string = 'I\'m a software engineer and I love programming in Python. \n\nI also enjoy working with data and building applications.\n\nI\'m always looking for new challenges\t and opportunities to learn and grow in my career.'
# print(escaped_string)

#String Methods
# print(first_name)
# print(first_name.upper())  # LAURA
# print(first_name.lower())  # laura      
# print(first_name.title())  # Laura
# print(first_name.capitalize())  # Laura (first letter capitalized)

# print(multiline_string.title())  # First letter of each word is capitalized
# print(multiline_string.replace("doing", "feeling"))  # Replaces all occurrences of "doing" with "feeling"

# print(len(multiline_string))  
# multiline_string += "                          "
# multiline_string = "                                       "+ multiline_string
# print(len(multiline_string))  # 120

# print(len(multiline_string.strip()))  # Removes leading and trailing whitespace  
# print(len(multiline_string.lstrip()))  # Removes left side leading whitespace
# print(len(multiline_string.rstrip()))  # Removes right side trailing whitespace  

# Build a menu using string methods
# print(" ")
# title = "Welcome to the Restaurant".upper()
# print(title.center(50, "="))  # Center the title with a width of 50 and fill with "*"
# print("Coffee".ljust(20, "."), "$2.50".rjust(3))  # Left justify the item name with a width of 30 and fill with "."
# print("Muffin".ljust(20, "."), "$5.00".rjust(3))  # Left justify the item name with a width of 30 and fill with "."
# print("Cappuccino".ljust(20, "."), "$3.50".rjust(3))  # Left justify the item name with a width of 30 and fill with "." 

# String index values
print(first_name[0])  # L
print(first_name[-1])  # index -1 is the last character of the string 
print(first_name[2])  # u
print(first_name[3])  # r
print(first_name[4])  # a
print(first_name[1:4])  # aur index 1 to 3 (4 is not included) 
print(first_name[1:5])  # aura 

# Some methods return boolean values
print(first_name.startswith("L"))  # True
print(first_name.endswith("z"))  # False

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))  # <class 'bool'>
print(isinstance(myvalue, bool))  # True

#Numeric data types

#integer data type
price = 100
best_price = int(95)
print(type(price))  # <class 'int'>
print(isinstance(best_price, int))  # True

#float data type
pi = 3.14 
y = float(2.5)
print(type(pi))  # <class 'float'>
print(isinstance(y, float))  # True

#complex data type
comple_value = 2 + 3j
print(type(comple_value))  # <class 'complex'>
print(comple_value.real)  # 2.0
print(comple_value.imag)  # 3.0

# Built-in functions for numeric data types
print(abs(pi))  # 3.14
print(abs(pi * -1))  # 3.14
print(round(pi))  # 3
print(round(pi, 1))  # 3.1

import math
print(math.pi)  # 3.141592653589793
print(math.ceil(pi))  # 4
print(math.floor(pi))  # 3

#Casting a number to a string
zipcode = "40255020"
zipcode_value = int(zipcode)
print(type(zipcode_value))  # <class 'int'>
print(zipcode_value)  # 40255020

# Error if you attempt to cast a string that is not a number to an integer
# zipcode = int("Castro Neves")  # ValueError: invalid literal for int() with base 10: 'Castro Neves'
