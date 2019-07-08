i=int(input())
l=[]
for j in range(0,i):
    k=int(input())
    l.append(k)
for m in l:
    if l.count(m)==1:
        print(m)
        break
