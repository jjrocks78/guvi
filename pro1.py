s=[]
b=int(input())
for k in range(0,b):
    n=input()
    s.append(n)
st=""
count=0
t=[]

for l in s:
    t.append(len(l))
t.sort()
m=t[0]
z=0

for j in range(0,m):
    count=0
    for i in range(1,b):

        if s[i-1][j]==s[i][j]:
            count+=1
        else:
            z=1
            break
        if count==b-1:
            st=st+(s[i][j])
    if z==1:
        break
print(st)

