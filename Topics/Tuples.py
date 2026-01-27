"""Ohh we start a new chapter to explor Python more and more , enjoy:)
Lists works well for storing collections of items that can change throughout the life of a  program.
But sometimes you'll want to creat a list of items connot change.
Tuples allw you to do just that.
Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
Defining a  tuple:
A tuple looks just like a list , expcept use parentheses->() instead of square brackets -> [].
Once you define a tuple, you can access individual elements by using  each item's index, just as you would fora list.
"""
# For example:
Food=("Pizza","Pasta")
print(Food[0])
print(Food[1])
# We define the tuple Food ,and print each element in the tuple individually, using the same syntax we've been using to access elements in a list.
# if we try to change value from the tuple we will get error 
Food[0]="rice"
#You will find TypeError
"""Note:Tuples are technically define by presence of a comma; the parentheses make them look neater and more readable.
if you want to define a tuple with one element, you need to include a trailing comma:
"""
num=(1,)
#It doen't often make sense to build tuple with one element, but this happen when tuples are generated automatically

#-----------------------------------------------------------------------------------------------------------------------
#1: Looping Through All Values in a Tuple
#you can loop over all the values in a tuple using for loop or while , but the comman is using for loop.
Name=("Mariam","Manar")
for i in Name:
    print(Name)
 #--------------------------------------------------------------------------------------------------------------------------
 #Writing over a Tuple:
"""Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple so the varible will presant a new tuple or
turn the tuple to list and modify if.
Note:Modify means to make a small change or improvement to something.
It does not mean to completely replace it — just to adjust or update part of it.

Examples:

Modify the code = change or improve a small part of the code

Modify the plan = adjust the plan a little

Modify the settings = change some options
 """
