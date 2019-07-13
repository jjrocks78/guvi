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
for x in range(1,len(b)):
    if b[x]==b[x-1] and a[1]==2*b[x]:
        print("yes")
        c=1

if c==0:
    print("no")
