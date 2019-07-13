n=input()
m=n.split(" ")
M=int(m[1])
o=input()
p=o.split(" ")
q=[]
for i in p:
    q.append(int(i))
q.sort(reverse=True)
count=0
for j in range(0,len(q)):
    if M>=q[j]:
        a=M//q[j]
        M=M-a*q[j]
        count+=a

print(count)
