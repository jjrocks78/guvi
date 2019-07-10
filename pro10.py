n=int(input())
m=input()
j=[]
sum1=[]
s=0
h=m.split(" ")
for i in h:
    j.append(int(i))
for k in j:
   for l in range(0,k):
       s+=l
print(s)
