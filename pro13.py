n=input()
m=n.split(" ")
x=input()
N=x.split(" ")
p={}
q=[]
for i in range(0,int(m[1])):
    o=input()
    p[i]=o.split(" ")
for j in range(0,int(m[1])):
    for k in range(int(p[j][0]),int(p[j][1])+1):
        q.append(int(N[k-1]))
    y=min(q)
    q=[]
    print(y)
print()
