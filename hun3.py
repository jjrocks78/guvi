i=int(input())
l=[]
b=0
for x in range(i):
    y=int(input())
    l.append(y)

for j in range(0,len(l)):
    if l[j]==j:
        print(l[j],end=" ")
        b+=1
if b==0:
    print("-1")
