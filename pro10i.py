n=int(input())
m=input()
j=[]
sum1=[]
s=0
h=m.split(" ")
for i in h:
    j.append(int(i))
for k in range(len(j)):
    sum=0
    for l in range(0,k):
        if j[k]>j[l]:
            sum+=j[l]
        else:
            continue
    #print(sum)
    sum1.append(sum)
count=0
for z in sum1:
    count=count+z
print(count)
