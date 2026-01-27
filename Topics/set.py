"""Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets."""
Mai={"m", "a","i"}
print(Mai)
print("m" in Mai)# Chack item
for i in Mai:
     print(i)
     # accss items and oop through the set
# add: to add new item 
Mai.add("u")
print(Mai)
#update(): To add items from another set into the current set, use the update() method.
friends={"Mariam","Mai","Malak"}
friends_2={"Fatma", "Manar"}
friends.update(friends_2)
print(friends)
print(friends_2)
#Set remove duplicated items and print one of them only
food={'Pizza',"rice",'Pizza'}
print(food)
#remve method
foods={"Pizza", "Mariam", "rice"}
foods.remove("Mariam")
# discard():
foods.discard("rice")
#Note: If the item to remove does not exist, discard() will NOT raise an error.

foods.discard("Pasta")
#pop():You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
grades={45,67,100}
New_grades=grades.pop()
print(New_grades)

#Clear() method empties the set:
test={"Mariam",97, 87}
test.clear()
print(test)
#del():the del keyword will delete the set completely:
school={"CLASS","Students","Teachers"}
del school

#----------------------------------------------------------------
"""Join Sets
There are several ways to join two or more sets in Python.
The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates."""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# We can use | instead of union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1|set2
print(set3)
set4={5,6,7}
set3=set1|set2|set4
print(set3)
#Note union() method allows you to join a set with other data types, like lists or tuples.
food2=("Pizza","pasta")
food={"rice","burger"}
set_food= food.union(food2)
print(set_food)
#Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method
# We Can not insert into () sset must be tuple/ or else
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#Note: Both union() and update() will exclude any duplicate items.
"""ntersection
Keep ONLY the duplicates
The intersection() method will return a new set, that only contains the items that are present in both sets."""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1&set2
print(set3)

#intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection_update(set2) 
print(set3)
#or
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1&=set2
print(set1)




#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
#You can use the - operator instead of the difference() method, and you will get the same result.
#The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set6 = {"apple", "banana", "cherry"}
set7 = {"google", "microsoft", "apple"}

set8 = set6.difference_update(set7)

#Symmetric Differences: The symmetric_difference() method will keep only the elements that are NOT present in both sets.
#Use ^ to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#frozeset is immutable set
my_list = [1, 2, 3, 4]

f = frozenset(my_list)

print(f)
#-------------------------------------------------------

"""
Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
    """
