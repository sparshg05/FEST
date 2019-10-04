import random
n=int(input('enter the length of password: '))
password=''
for i in range(n):
    m=random.randint(0,n)
    print('m is',m)
    if m==0:
        password=password+chr(random.randint(65,90))#A-Z
    elif m==1:
        password=password+chr(random.randint(97,122))#a-z
    elif m==2:
        password=password+chr(random.randint(48,57))#0-9
    else:
        password=password+chr(random.randint(35,38))#special char

print('password is',password)

x=input()
