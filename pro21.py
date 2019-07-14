from statistics import mean
n=int(input())
m=input()
p=m.split(" ")
q=[]
av1=0
av2=0
b=0
for i in p:
    q.append(int(i))
for j in range(1,len(q)):
    av1=sum(q[:j])/len(q[:j])
    av2= sum(q[j:]) / len(q[j:])
    #print(av1, av2)
    if int(av1)==int(av2):
        print("yes")
        b=1
if b==0:
    print("no")
