winning_number = 14
user = input("enter the number you have guessed : ")
user = int(user)
if user == winning_number:
    print("congratulations you win")
else:# nested if else
   if user<14:
       print("too low")
   else:
       print("too high")