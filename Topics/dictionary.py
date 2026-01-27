""" dictionary is a type of arraysin python ,it's used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates."""
test={"Mariam": 22, "Mohamed":26, "Esmail":23}
print(test)
test["Mohamed"]= 24
print(test)
print(test["Mariam"])
#----------------------------------------------
alien={}
alien["Color"]="green"
alien["Food"]="Pizza"
print(alien)
#--------------------------------------------
# A Dctionary of Samiar Objects:
fav_language={
"MARIAM":"java",
"Khaled":"Java",
"Mohamed":"Python"
}
language=fav_language["MARIAM"].title()
print(f"Mariam Fav Language is {language}.")
#We use "," To Start New line 
#We Make Poll using Dictionary

#-----------------------------------------------------
#Using get() to Access Values
# Using name of dictionary[KEY] . But if the KEY does not exit we will get in error
# You can se get()method to set a default value that will be returned if the requested key doesnot exist.
coffee={"you":"Calm", "Statue":"Fouce", "Mood":"nice"}
test=coffee.get("Fun", "No point value assigned")
print(test)
#------------------------------------------------------
#LOOPing through out the dictionary
sports={"football","vally","swimming"}
for x in sports:
  print(x)
#
sports={"football","vally","swimming"}
for x in sports.values():
  print(x)


#
sports={"football","vally","swimming"}
for x in sports.keys():
  print(x)

ports={"football","vally","swimming"}
for x in sports.items():
  print(x)
  