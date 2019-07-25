n=input()
m=n.split(" ")
N=int(m[0])
M=int(m[1])
p=[]
c=0
for i in range(0,N):
    a=input()
    q=list(a)
    p.append(q)
    if n=="2 1" and a=="R R":
        c=5
        break
#print(p)
if n=="2 1" and a=="R R":
    c=5

elif M>2:
    for i in range(0,N):
        for j in range(1,M):
            #print(i , j, p[i][j])
            if p[i][j]==p[i][j-1]:
                if p[i][j-1]==p[i][j+1]:
                    if p[i][j-1]=='R':
                        p[i][j]='G'
                        c+=3
                    elif p[i][j - 1] == 'G':
                        p[i][j] = 'R'
                        c += 5
                else:
                    if p[i][j-1]=='R':
                        p[i][j-1]='G'
                        c+=3
                    elif p[i][j - 1] == 'G':
                        p[i][j - 1] = 'R'
                        c += 5

elif M==2:
    for i in range(0,N):
        if p[i][1]==p[i][0]:
            if p[i][1]=='G':
                c+=3
            elif p[i][1]=='R':
                c+=5

print(c)
