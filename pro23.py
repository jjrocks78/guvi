import turtle
wn=turtle.Screen()
wn.bgcolor("light blue")
jj=turtle.Turtle()
jj.goto(1,1)
x=jj.pos()
n=input()
k=[]
l=[]

for i in n:
    if i=='G':
        jj.forward(1)
    elif i=='R':
        jj.right(90)
    elif i=='L':
        jj.left(90)

jj.right(180)
y=jj.pos()
#print(x,y)
for j in x:
    k.append(round((j**2),2))
for P in y:
    l.append(round((P**2),2))
#print(k,l)
if l==k:
    print('yes')
else:
    print('no')
