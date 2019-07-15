num=int(input())
mn=input()
a=mn.split(" ")
p=[]
for i in a:
    p.append(int(i))
q=[]

for j in range(0,num):
    c = 1
    for k in range(j+1,num):
        if p[j]<p[k]:
            c+=1
            p[j]=p[k]


        #print(j,k,c,p)
    q.append(c)

print(max(q))
