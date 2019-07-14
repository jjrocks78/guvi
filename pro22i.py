import math
n=int(input())
m=input()
o=m.split(" ")
q=[]
for i in o:
    q.append(int(i))

t=[]
for i in q:
    t.append(i)

s=0
res=[]

count=0
for x in range(0,n-1):
    if q[x]==q[x+1]:
        count+=1
if count==n-1:
    s=math.ceil(n/2)
else:
    k = q.index(max(q))
    res.append(k)
    c = 0
    q[k] = 0
    # print(k,res)
    for y in range(0,n):
        while k!=0:
            k = q.index(max(q))
            for j in range(0,len(res)):
                #print(j,k,res[j]+1,res[j]-1,len(res))
                if (k==int(res[j]-1)) | (k==int(res[j]+1)):
                    c=1
                    break
            #print(c)
            if c==0:
                res.append(k)
                #print(k, q)
                #print(res)
            q[k] = 0


    for z in res:
        s+=t[z]
print(s)
