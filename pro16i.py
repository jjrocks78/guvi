w=int(input())
n=input()
m=n.split(" ")
l=[]
for i in m:
    l.append(int(i))
l.sort()
count=0
#print(l)
b=1
res=0
z=[]
for j in range(0,w):
    for k in l:
        if not(k in z):
            if k>w:
                b=0
            else:
                z.append(k)
                count=l.count(k)
                res+=count*b
                b+=1
print(res)
