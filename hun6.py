a=int(input())
b=input()
c=b.split(" ")
d=[]
for i in range(0,a):
    if c[i]  in d:
        print(c[i])
        break
    else:
        d.append(c[i])

