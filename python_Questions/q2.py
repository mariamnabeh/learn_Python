"""Write a program to calculate the sum of series up to n term. For example, if n =5 the
series will become 2 + 22 + 222 + 2222 + 22222 = 24690
Input:
number of terms = 5
Expected output:
24690"""
n=int(input())
for i in range(1,n+1):
    print('*'*i)
for i in range(n-1,0,-1):
     print('*'*i)