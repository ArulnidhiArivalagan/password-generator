#program to cal average height from list of heights
#use for loop and user input function has to be used

# a=input().split()
# # print(a)1
# count=0
# for x in a:
#     count+=1
# print(count)
# for i in range(count):
#     a[i]=int(a[i])
# # print(a)
# total=0
# for person in a:
#     total+=person

# avg=total/count
# print(round(avg))


# num=input()
# num_list=num.split()
# count=0
# for i in num_list:
#     count+=1
# print(count)

# for i in range(0,count):
#     num_list[i]=int(num_list[i]) # type: ignore
# max_number=num_list[0]
# for i in num_list:
#     if i>max_number:
#         max_number=i
# print(max_number)

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

