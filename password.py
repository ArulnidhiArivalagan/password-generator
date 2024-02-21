#password generator!!
import random
a=int(input("how many letter u want in ur password?\n"))
# print(a)
b=int(input("how many symbols??\n"))
c=int(input("how many nubers u want??\n"))
letter=['a', 'b', 'c', 'd', 'e', 'f', 
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n','o', 'p', 'q','r', 's', 't', 'u', 
         'v', 'w', 'x', 'y', 'z','A','B','C']

numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*']
password=[]
for i in range(1,a+1):
    char=random.choice(letter)
    password+=char
for i in range(1,b+1):
    char=random.choice(numbers)
    password+=char
for i in range(1,c+1):
    char=random.choice(symbols)
    password+=char
print(password)
random.shuffle(password)
print(password)
s=''
for char in password:
    s+=char
print(s)
