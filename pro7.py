import math as m
a=int(input())
for i in range(0,a):
    j=pow(2,i)
    if j>a:
        j=pow(2,i-1)
        break
b=a-j
print(b)
