num=int(input())
mn=input()
a=mn.split(" ")
p=[]
for i in a:
    p.append(int(i))
q=[]
c=1
for j in range(0,num-1):
    if p[j]<p[j+1]:
        c+=1
    else:
        q.append(count)
        #print(q)
        c=1
    #print(j,count)
q.append(c)
print(max(q))

