n=input()
b=0
for i in range(0,len(n)):
    for j in range(i,len(n)):
        if ord(n[i])<ord(n[j]):
            print(n[j:])
            b=1
            break
    if b==1:
        break
