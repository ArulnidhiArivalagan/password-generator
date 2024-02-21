# range function in detail
#syntax
#range(start,stop,step_size)  by default step size is 1


# n=input().split()

# count=0
# for i in range(1,101):
#     if i%2==0:
#         count+=i
# print(count)

#fizzbuzz 


for i in range(1,11):
    if i%3==0 and i%5==0:
        print("fizzbuz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)


