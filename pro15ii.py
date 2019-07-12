import math
o=input()
n=input()
m=n.split(" ")
p=[]
for i in m:
    p.append(int(i))
q=max(p)
s=int(math.ceil(q**0.5))
#print(q, s)
for j in range(s,0,-1):
    for k in range(1,s):
        if pow(2,j)-k in p:
            print(pow(2,j)-k)
for l in range(s,0,-1):
    if pow(2,l) in p:
        print(pow(2,l))
if pow(2,0) in p:
    print(pow(2,0))
