n=input()
m=n.split(" ")
M=[]
for a in m:
    M.append(int(a))
N=M[0]
W=M[1]
o1=input()
p1=o1.split(" ")
q1=[]
for b in p1:
    q1.append(int(b))
o2=input()
p2=o2.split(" ")
q2=[]
for c in p2:
    q2.append(int(c))
q3=[]
for c in range(0,N):
    q3.append(q1[c]*q2[c])
k=0
s1=0
sum=0
#print(q3)
while sum<=W:
    sum+=q1[k]

    if sum>W:
        sum=k
        for z in range(0,k):
            s1+=q2[z]
        break
    k+=1
print(s1)
