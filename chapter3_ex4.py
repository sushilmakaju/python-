user = input ("enter your name")
i = 0
tem_var = ""
while i<len(user):
    if user[i] not in tem_var:
        tem_var += user[i]
        print(f"{user[i]} : {user.count(user[i])}")
        i+=1


