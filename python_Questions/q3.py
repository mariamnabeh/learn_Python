"""Write a program to calculate the sum of series up to n term. For example, if n =5 the
series will become 2 + 22 + 222 + 2222 + 22222 = 24690
Input:
number of terms = 5
Expected output:
24690"""
n=int(input())
num = 0
output = 0
series = []  

for _ in range(n):
    num = num * 10 + 2
    series.append(str(num)) 
    output += num

print(" + ".join(series), "=", output)
