def fact(a):
    fact=1
    while a>1:
        fact=fact*a
        a-=1
    return fact

n=int(input())
if n %2==0:
    m=fact(n-1)
elif n%2==1:
    m= n
print(m)
