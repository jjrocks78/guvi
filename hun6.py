a=int(input())
b=input()
c=b.split(" ")
d=[]
x=0
for i in range(0,a):
    if c[i]  in d:
        print(c[i])
        x=1
        break
    else:
        d.append(c[i])

if x==0:
    print("unique")
