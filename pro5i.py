z=(input())
l=[]
l=z.split(" ")
n=int(l[0])
a=int(l[1])
b=int(l[2])
i=0
c=0
while i<=n:
    for j in range(0,n):
        for k in range(0,n):
            i=(a*j+b*k)*2
            if i==n:
                print("YES")
                c=1
                break
        if c==1:
            break
    if c==0:
        print("NO")
        break
    else:
        break
