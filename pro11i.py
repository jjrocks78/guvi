import math
n=int(input())
res=1
if n%2==0:
    for i in range(n,2,-1):
        res=res*i
    res=res/2
    print(int(res))
else:
    for i in range(n-1,2,-1):
        res=res*i
    res=n*int(math.ceil(res/2))
    print(int(res))
