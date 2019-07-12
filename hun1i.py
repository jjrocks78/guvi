n=int(input())
m=input()
o=m.split(" ")
p=[]
q=[]
for i in o:
    p.append(int(i))
for j in range(0,len(p)):
    for k in range(j+1,len(p)):
        if p[j]==p[k] and not(p[j] in q) :
            q.append(p[j])
q.sort()
for l in q:
    print(l,end=" ")
