i=int(input())
l=[]

k=input()
l=k.split(" ")
for m in l:
    if l.count(m)==1:
        print(m)
        break
