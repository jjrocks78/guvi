n=int(input())
o=input()
m=o.split(" ")
a=[]
st=""
for i in m:
    a.append(int(i))
a.sort(reverse=True)
for j in a:
    st+=str(j)

print(st)
