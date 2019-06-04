c=input()
d=ord(c)
if (d>=97 and d<=122) or (d>=65 and d<=90):
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u'or c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
        print('Vowel')
    else:
        print('Consonants')
else:
    print('invalid')
