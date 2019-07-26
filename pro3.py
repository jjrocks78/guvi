n=input()
m=n.split(" ")
x=list(m[0])
y=list(m[1])
c=0
while x!=y:

    if len(x)==len(y):
        #print("1")
        for i in range(0,len(x)):
            if x[i]!=y[i]:
                #print(i)
                c+=1
                x[i]=y[i]

        if x == y:
            break


    else:
        if len(x)>len(y):
            #print("2")
            a=len(x)-len(y)
            x=x[:a+2]
            #print(x)
            c+=a
        elif len(y)>len(x):
            #print("3")
            a = len(y) - len(x)
            y = y[:a+2]
            c+=a
            #print(y , c)

print(c)
