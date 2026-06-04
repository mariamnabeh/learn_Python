"""7. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
array. (Where X: number of raws, Y: number of columns).The element value in the i-th
row and j-th column of the array should be i*j.
Input:
3,5
Expected output:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]"""

x = int(input("Enter number of rows: "))
y = int(input("Enter number of columns: "))
array=[]
for i in range(x):
    row=[]
    for j in range (y):
        row.append(i*j)
    
    array.append(row)
print(array)