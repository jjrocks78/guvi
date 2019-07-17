n=int(input())
t=n
k=n
c=0
a=0
count=0
b=0
d=[]
while k!=0:

    k=k//10
    #print(k)
    c+=1
#print(c)

for i in range(100000000,n):
    z=i
    b=0

    while z>0:

        j=z%10
        b+=j
        z = z // 10
        #print (i,j,"hi",b)
    if i+b==n:
        count+=1
        d.append(i)

print(count)
for v in d:
    print(v)

