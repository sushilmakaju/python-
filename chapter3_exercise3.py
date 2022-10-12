#sum of n natural of numbers

"""x = 0
i = 1
while x<=100:
    x=x+i
    i=i+1
    print(x)"""


user = input("enter a natural number")
user = int(user)
total = 0
i = 1
while i<=user:
    total = total+i
    i=i+1
    print(total)