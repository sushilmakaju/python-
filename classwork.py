#1
'''
user = input("enter your age")
user = int(user)
if user > 18:
    print("you are eligible to caste vote")
else:
    print("you are not eligible to caste vote")
'''
#2
'''
user = input("enter a number you want")
user = int(user)
if user%2 == 0:
    print("it is even number")
else:
    print("it is odd number")
'''

#3
'''
user = input("enter a number")
user = int(user)
if user%7 == 0:
    print("it is divisible by 7")
else:
    print("it is not divisible by 7")
'''

#4
'''
user = input("enter a number")
user = int(user)
if user%5 == 0:
    print("hello")
else:
    print("bye")
'''

#5
'''
def lastDigit(num):
   return num % 10

number = int(input("Please Enter any Number: "))

last_digit = lastDigit(number)

print("The Last Digit in a Given Number %d = %d" %(number, last_digit))
'''
'''
user = input("enter a number")
user = int(user)
last_number = user%10;
print(f"the last number is {last_number}")
'''
'''
user = input("enter a number")
user = int(user)
last_number = user%10
if last_number%3 == 0:
    print("it is divisible by 3")
else:
    print("it is not divisible by 3")
'''

#ex6
'''
year = int(input("enter year"))
if (year%4 == 0) or (year%400 == 0) and (year%100 != 0):
    print("The given year is leap year")
else:
    print("given year is not a leap year")
'''

#ex7
user = input("enter a number")
user = int(user)
if user == 1:
    print("Sunday")
elif user == 2:
    print("Monday")
elif user == 3:
    print("Tuesday")
elif user == 4:
    print("Wednesday")
elif user == 5:
    print("Thursday")
elif user == 6:
    print("Friday")
else:
    print("Invalid input")



