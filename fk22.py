n=int(input())
m=input()
o=m.split(" ")
a=[]
for i in o:
    a.append(int(i))
a.sort(reverse=True)
c=a[0]+a[1]
print(c)
