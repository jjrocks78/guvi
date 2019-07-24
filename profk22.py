import math
n=int(input())
m=input()
o=m.split(" ")
a=[]
count=0
for i in o:
    a.append(int(i))
a.sort(reverse=True)
for x in range(0,n-1):
    if a[x]==a[x+1]:
        count+=1
if count==n-1:
    c=math.ceil(n/2)
    print(c)
else:
    c=a[0]+a[1]
    print(c)
