"""0:In this Chapter we will learn more aboute string .hhmm ,so what's the string?
A string is a sequence of letters, special characters, spaces,
digits
• Strings are delimited by single ‘ ‘ or double “ “ quotes
• Strings can be stored in variables.
In our Python journal we will leaen more about it, let's beginn!!
"""
x="Mariam" 
x= 'Mariam'
""" that's How we define a String , but what's the defferent btween Single quotes and Double quotes?
"The only differences between single and double quotes in Python are purely visual and related to avoiding escape characters.
"""
# Using single quotes
s1 = 'I am happy'   # Single quotes

# Using double quotes
s2 = "I am happy"   # Double quotes (same meaning)

# Using double quotes to avoid escaping a single quote
s3 = "I'm happy"    # Easier: no need for escaping

# Using single quotes to avoid escaping a double quote
s4 = 'He said "Hello"'   # Easier: no need for escaping

# Using the same quote type inside requires escaping
s5 = "He said \"Hello\""  # Must escape the double quote
s6 = 'It\'s fine'         # Must escape the apostrophe
"""
Python does not distinguish between apostrophes, single quotes, or double quotes inside strings;
it only treats the outer matching quotes as the string delimiters,
interprets everything inside literally,
and that’s why:

If we want to include a quote that matches the outer delimiters,
we either:

1:Use a different type of quote for the string, or

2:Escape it with a backslash (\)

so Python knows it is part of the text.

In other words:
Python sees the outer quotes as the string boundary and everything inside as literal text,
unless told otherwise with escaping or by using a different quote type."
"""
#-----------------------------------------------------------------
#1:can compare strings with ==, >, < etc.
# len() is a function used to retrieve the length ofthe string in the parentheses 
Fun="Function"
print(len(Fun))

x= "Hahaha"
y="Shut upp x!"
if len(x)> len(y):
    print (True)
else:
    print(False)
"""Samply len function give us length of  x string and compare it with y , if x>y , will print True else flase .
because length of  y<x  we see false"""
#--------------------------------------------------------------------
# 2:input Function:
"""if we want to take input we use input function , it's only take a string .
we write it as input () if our input is a string we don't need to write the date type of the input .
if the input is a float, intger , else . we write the date type of it, like: int(input()).

Small note: We use () after a function because it tells the Python interpreter that we want to execute (call) the function.
If the function takes parameters, we provide them inside the parentheses.
We will discuss this more deeply in the Functions chapter. I hope you’re excited too!
"""
#--------------------------------------------------------------------

x = input()
print (x)
#3:String Operations
#A.Repetition
print("hi" * 3) #You will see: hihihi. In Python, string * number repeats the string that many times.

#B.Concatenation
X = "hello there" 
Y = "ANN"
greet = X + Y
greeting = X + " " + Y # + joins strings, adding a space if included.

#--------------------------------------------------------------------
#4: Formatted Printing
#A.Comma-separation:
p = 3
print("price =", p, "$")   # Output: price = 3 $
#B.Concatenation (+)
name = 'Ahmed'
print('welcome ' + name)   # Output: welcome Ahmed
# Note: Works only if all parts are strings
#---------------------------------------------------------------------
#5.Dynamic vs Static Text Output in Python
print("Price = 5")  # always prints 5

"""Old-style string formatting using % lets you insert variables (integers, floats, or strings
into text with specific formats like %d, %f, or %s."""
p = 5
print("Price = %d" % p)  # prints 5 from variable
#%d Integer.%f Float. %s String

"""Modern formatting (str.format() / f-strings)
Dynamic, automatic type handling More flexible, readable, and supports multiple variables
"""
p = 5
print("Price = {} $".format(p))  # str.format()
print(f"Price = {p} $")          # f-string
#-----------------------------------------------------------------------
#6.Casting (Type Conversion)




