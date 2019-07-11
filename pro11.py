def fact(a):
    fact=1
    while a>1:
        fact=fact*a
        a-=1
    return fact

n=int(input())
m=fact(n-1)
print(m)
