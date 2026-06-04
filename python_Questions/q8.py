"""Write a program to print the following pattern using 2 inputs (X,Y) from the user.
Hint: assume a 2D matrix of X raws and Y columns (Where X: number of raws, Y:
number of columns).The element value in the i-th row and j-th column of the array
should be i*j.
Input:
3,5
Expected output:
0 0 0 0 0
0 1 2 3 4
0 2 4 6 8
"""
x=int(input())
y=int(input())
for i in range(x):
    for j in range (y):
      print(i*j, end=' ')
    print()
