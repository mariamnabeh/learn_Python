"""tipes about How  to use this file. 
1: read  every note and understand it will
2: Try the code by yourself with diffrent examples
3:Don't take any thing copy , past . just try to write it and learn from your mistakes
and understand the errors.

Let's Start This Chapterr!!

 """

# Data types and Variables:
# In python we have diffrent data types like: int, float, str, bool
x = 10          # int (integer number)
y = 3.14        # float (decimal number)
name = "mariam" # str (string/text)
is_active = True# bool (boolean: True or False)

print(name)
print(type(x)) # type() function tells us what data type is inside the varible

#---------------------------------------
# String Concatenation & Errors:
# We can combine strings together, but we CANNOT combine string with integer directly!

# print("Age is: " + x) # remove # and try it -> TypeError: can only concatenate str (not "int") to str

# To fix this error we use str() to change int to string, or use comma / f-string:
print("Age is: " + str(x))
print("Age is:", x)
print(f"My name is {name.title()} and x value is {x}")

#---------------------------------------
# User Input and Casting:
# input() function always take input as string (str)
# So if we need to do math operations we MUST convert it (Casting)

age = "20" # assume this came from input()
# print(age + 1) # TypeError: can only concatenate str (not "int") to str

real_age = int(age) # convert str to int
print("Next year age will be:", real_age + 1)

#---------------------------------------
# If Statements & Conditions:
# We use if statements to make decisions in code
# Syntax: if condition :

score = 85
if score >= 90:
    print("Excellent! Grade A")
elif score >= 75:
    print("Very Good! Grade B")
else:
    print("Keep working hard!")

#---------------------------------------
# Logical Operators: and , or , not
# and -> all conditions must be True
# or  -> at least one condition is True

has_id = True
age = 18

if age >= 18 and has_id:
    print("You can enter the exam")
else:
    print("Access Denied")

#---------------------------------------
# Avoid Errors in Conditions:

# 1: Using = instead of ==
# = is for assigning value to variable
# == is for checking if two values are equal
num = 5
# if num = 5: # SyntaxError: invalid syntax
if num == 5:
    print("Number is 5")

# 2: Forgetting Colon : at the end of if/elif/else
# if num > 2 # remove # -> SyntaxError: expected ':'
if num > 2:
    print("Greater than 2")

# 3: Indentation Errors inside if block
if num > 0:
#print("Positive") # IndentationError: expected an indented block
    print("Positive number")

# 4: Check if item exists in list using 'in'
users = ["mariam", "ahmed", "ali"]
current_user = "mariam"

if current_user in users:
    print(f"Welcome back, {current_user.title()}")
else:
    print("User not found!")

# 5: Check if list is empty
items = []
if items:
    print("List has items inside it")
else:
    print("List is empty!")

"""Don't feel bad when a small fix takes a long time to find ; Tou are not alone in this experience."""
#The mission and I are done… we’re finished…