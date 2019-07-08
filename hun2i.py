n2=int(input())
l=[]
for i in range(n2):
    m=input()
    l.append(m)
l.sort(reverse=True)
k=set(l)
o=list(k)
if len(o)==1:
    if o[0]=='0':
        print('0')
else:
    for j in l:
        print(str(j), end="")
