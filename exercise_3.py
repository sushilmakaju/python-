name, char = input("enter your name and character").split(",")
print(f"length of name is {len(name)}")
print(f"charcter count:{name.strip().lower().count(char.strip().lower())}")