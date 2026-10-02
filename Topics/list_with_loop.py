"""tipes about How  to use this file. 
1: read  every note and understand it will
2: Try the code by yourself with diffrent examples
3:Don't take any thing copy , past . just try to write it and learn from your mistakes
and understand the errors.

Let's Start This Chapterr!!

 """
l=["Ali","ahmed", "mariam"]# define list
for x in l:
    print(x) 
    # List name =[items]
    # for (temporary varible name) in (list name) "" #
# note if we print list name instead of varible name we will see the list printed 3 times or lenth of list
l=["Ali","ahmed", "mariam"]
for x in l:
    print(l) 
#------------------------------------
# if we want to print if without [] , we will use: 
for x in l:
    print("".join(l)) # define list"".join(list name)
# you will note that: all list looped without space so we will  add space in "" to be-> " "
for x in l:
    print(" ".join(l))
#---------------------------------------
name=["mariam", "menna","Ali", "Khaled"]
for l in name:
    print (f"{l.title()}, Study hard")
# That app actullay take the items from list, print it with capitla litter as title , and with some sentance :)

# also we can make the sentane in the firt by:
name=["mariam", "menna","Ali", "Khaled"]
for l in name:
    print (f"Study hard, {l.title()}\n")
#---------------------------------------
name=["mariam", "menna","Ali", "Khaled"]
for l in name:
    print (f"Study hard, {l.title()}\n")
print ("Thank you all")
"""why the last print doen't repeat list items ? because we out of for scope and we didn't call the list and that called:
 indentation Errors"""
#---------------------------------------
# Avoid indentation Errors
"""python's use of indentation makes codevery easy to ready .
Bascally, We use withspace to force you to write neatly formatted code with a clear visual structure.
Let's examine some of the more commen indentstion errors"""
# 1:Forgetting indent
num=[1,2,3]
for n in num:
#print("num is", n) That's wrong
  print("num is", n)  # with whaitspace


# 2 : Forgetting Indent Additional Lines
""" Sometimes you loop will run wihout any errors but won't produce the expected result . This can happen when you're trying
to do several tasks , like the program doenot print last print as i mention before . anthor example"""
Student=  ["mariam", "Mohammed","maner" , "menna"]
for i in Student :
    print(f"{i.title()} , Well done ")
print(Student, "Study hard")
"""we will find the list print but for doen't loop in it . This ia a logical error. 
 The Syntax is valid Python code, but the code not produse the desired result"""


#3: Indenting Unnecessarily
"""If you accidentally indent a line that doesn't need to be indented , python informs you about the unexpected indent """
# for example:
Massage="Hello python world"
  #print(Masseage) remove # and try it :) 
# You will find that massage : IndetationnError: unexpected indent .But in red line :) , I know bad joke .

#4:Indenting Unnecessarily After the Loop
Student=  ["mariam", "Mohammed" ,"maner" , "menna"]
for i in Student :
     print(f"{i.title()} ,that was a great trick! ")
     print(f"i can't wait to see your next trick , {i.title()} ")
     print(f"Thank you, {(i)}")
     print("Thank you")

     print("Thank you everyone")
""" Because the last line is indented , it's printed once"""

#5: Forgetting the Colon
"""The colon at the end of a for statment tells Python to interpret the next line as the start 
of a loop"""
Mariam=["M", "a","r","i","a","m"]
for i in Mariam :
     print("Letter of Mariam is:", i)

#6: Start your list with whitspace
#Try it with yourself :)

# 7: Forgetten to add comma after using to diffrent date type in print function

#for i in Mariam :
     #print("Letter of Mariam is:" i) remove # and try it

"""Don't feel bad when a small fix takes a long time to find ; Tou are not alone in this experience."""
#---------------------------------------
# Making Numerical List :
"""Many reasons exist to store a set of numbers. We will have alotof examples.
# Using the range() Function in Python is used to create a sequence of numbers . It often used in loops or to make numerical lists
How it works:
range(start, stop, step)

start → the first number in the sequence (default is 0)

stop → the number where the sequence ends (not included)

step → the difference between each number (default is 1)

Difference:
range() doesnot create all numbers at once — it generates them one by one when needed, which saves memory.
To turn it into a full list, you can use list(range(...)).
"""
for number in range(1, 6):
    print(number)
# We can skip items form list by change the steps

even_numbers = list(range(2,11,2)) 
print(even_numbers)
 #You can do oprations with list , like:
Square=[]
for value in range(1,11):
    i= value**2
    Square.append(i)
print(Square)
 # we can writ it also like:
Square=[]
for value in range(1,11):
    Square.append(value**2)
print(Square)

#or:
sqares =[value**2  for value in range (1,11)]
print(sqares)
#--------------------------------------------------------------------------
#coping a list:
my_food=["pizza","Burger","pasta","falafel"]
friends_food=my_food[:]
print(friends_food)
# thats meaning add all Items in list one to the secand List .[:] that means start with index  0 to last item i the list
#To prove that we actually have two separate lists,we'll add a new food to each list and print them:
my_food.append("ice cream")
friends_food.append("rice")
print(my_food)
print(friends_food)
#As we see from the output the result of list one not equal list two  
#Thatis doesn't work:
friends_food=my_food
"""Instead of assigning a copy ofmy foods to friends_food, we set friends_food
equal to my_foods.This syntax tells python assciate the new varible friends_food with the listis already associated  with my_food 
, so now both to the same list .As result the interpranter treat them as one list.
If you try to add itemm to my_food , the same item will added to friends_food!"""
#The mission and I are done… we’re finished…




