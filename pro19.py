k=int(input())
p=[]
r=[]
for i in range(0,k):
    q=input()
    p.append(q)
for i in p:
    j=i.split(" ")
    for a in j:
        r.append(int(a))
r.sort()
for z in r:
    print(z,end=" ")
