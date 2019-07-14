n=int(input())
x=pow(2,n)
for i in range(0,x):
    y=bin(i)
    y=y[2:]
    z=str(y)
    if len(z)==n:
        print(z)
    else:
        while len(z)!=n:
            z='0'+z
        print(z)
