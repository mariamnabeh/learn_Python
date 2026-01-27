""""
In this chapter, we will learn more about lists and some useful functions that can be used in various situations.
Let us begin exploring lists and their useful functions.

What is a list or an array in other languages?
A list is a collection of items in a particular order

That's the academic meaning, but what is a list in practice?
 If you want to reserve space for multiple pieces of data in memory so you can use them
 for calculations, processing, or any operations you need, you can use a list for that!

"""
List=[10,7,8]
print(List[0])
#That's a list and To print the index (postion of some value) we use : print (to print),list name and [postion like: 0,1,-1] , so we can call list to came And print it :)
# # we sort index with 0 from right and with -1 from left

#--------------------------------------------------------------
name=[2,7,9,8]
name.append(0) #SWITCH VALUE
del name[1] #delet value with postion
name.pop (2) # delete the last postion 
# the diffrence detween pop VS del is: pop delete and save the value so we can use it agin, but del is not just delete
name.remove (9)
#we use remove if we know the value not postion
name.insert(3,1) # switch to values
print(name)
name.clear() # print impty list
#-----------------------------------------------------------
mariam=["m","a","b","c"]
mariam.sort()
print(mariam)
#make it sorted by alphabeti
#-----------------------------------------------------------

doaa=["a","a","o","d"]
doaa.sort (reverse=True)
print(doaa) # sorted reverse alpbeti
doaa.reverse() # it will not work bec we use sort in the same code
print(doaa)
#reversethe list
print(len(doaa)) # lenth of the words
print(doaa.index("o"))# postion
print(doaa.count(doaa)) #count 

#------------------------------------------------------------
m=["O","N"]
m.reverse()
print(m)
# it will works!
# To print it without [] , USE JOIN
print("".join(m))
#------------------------------------
# if you wanne use reverse and sort in the same code:
samer = ["r", "a", "m", "e", "s"]

# بنعمل نسخة مرتبة عشان نستخدمها لوحدها
sorted_list = sorted(samer)       # بترتب من a لـ z
reversed_list = list(reversed(samer))  # بتقلب الأصلية بس

print( samer)
print( sorted_list)
print( reversed_list)
#-----------------------------------------------------------------------------------------------------
#List Operations
L=[1,2]
[1] * 3 # Will double 1 three times
L = [2, 10, 5, 1]
max (L)
min (L)
# PRINT THE MAX && MAN
#----------------------------------------
#LISTOperations: Slicing
grades = [60, 70, 50, 80, 100]
grades [1:3]
[ 70, 50]
grades [2: ]
[50, 80, 100] 
grades [ :4:2]
[60, 50]
grades[-1:-5:-1]
[100, 80, 50, 70]
# varible name [START:STEP: END], IF YOU DON'T INSERT VALUE TO: START WILL START WITH 0 , STEP WITH 1, END TO LAST VALUE
# END always = num-1 , so if you wanna end in postion  3 , make end num = 4 
#--------------------------------------------------------------------------







