user = input("enter a number")
total = 0
i = 0
while i < len(user):
    total += int(user[i])
    i += 1
print(total)