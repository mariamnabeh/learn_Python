"""Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a
program to arrange the characters of a string so that all lowercase letters should come
first.
Input:
str1 = PyNaTive
Expected Output:
yaivePNT"""

str1 = "PyNaTive"
str2=""
str3=""
for i in str1:
    if i.islower():
       str3+=i
    else:
        str2+=i
new=str2+str3.rstrip(" ")
print(new)