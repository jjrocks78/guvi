n=int(input())
x=pow(2,n)
a=[]
for i in range(0,x):
    y=bin(i)
    y=y[2:]
    z=str(y)
    if len(z)==n:
        a.append(z)
    else:
        while len(z)!=n:
            z='0'+z
        a.append(z)
#print(a)
for j in range(0,n+1):
    for k in a:
        if k.count('1')==j:
            print(k)
            
            
            
