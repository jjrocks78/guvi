n=input()
m=n.split(" ")
x=input()
N=x.split(" ")
p={}
for i in range(0,int(m[1])):
    o=input()
    p[i]=o.split(" ")
for j in range(0,int(m[1])):
    sum=0
    for k in range(int(p[j][0]),int(p[j][1])+1):
       #print(N[k-1],end="")
        sum+=int(N[k-1])
    print(sum)
