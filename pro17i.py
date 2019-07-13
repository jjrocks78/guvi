n=input()
m=n.split(" ")
a=[]
c=0
for i in m:
    a.append(int(i))
p=input()
q=p.split(" ")
b=[]
for j in q:
    b.append(int(j))
for x in range(0,len(b)):
    for y in range(x+1,len(b)):
        if a[1]==b[x]+b[y]:
            print("yes")
            c=1

if c==0:
    print("no")
