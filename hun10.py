n=input()
m=n.split(" ")
a=input()
b=a.split(" ")
c=input()
d=c.split(" ")
x=[]
y=[]
z=0
for i in b:
    x.append(int(i))
for j in d:
    y.append(int(j))
if (set(y).issubset(set(x))):
    z=1
if z==1:
    print("YES")
else:
    print("NO")
