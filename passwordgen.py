import random
print('if you want 6 digit as password type yes')
option=input('yes/no: ')
if option=='yes':
    x=random.randrange(100000,999999)
    print('your password is: ',x)
else:
    passlen = int(input("enter the length of password: "))
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p = "".join(random.sample(s,passlen ))
    print('your password is: ',p)
