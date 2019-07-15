n=int(input())
m=input()
o=m.split(" ")
p=[]
for i in o:
    p.append(int(i))
q=[]
count=1
for j in range(0,n-1):
    if p[j]<p[j+1]:
        count+=1
    else:
        q.append(count)
        #print(q)
        count=1
    #print(j,count)
q.append(count)
print(max(q))

