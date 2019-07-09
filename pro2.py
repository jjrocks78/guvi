a=(input())
b=a.split(" ")
c=b[0]
l=len(c)
d=int(b[1])
st=""
count=0
if d!=0:
    for i in range(1,10):
        if str(i) in c:
            f=c.find(str(i))
            c=c[f:]
            st=st+str(i)
            count+=1
        else:
            pass
        if count==l-d:
            print(st)
            break
else:
    print(c)
