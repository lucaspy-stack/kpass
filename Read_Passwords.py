# Just to see the passwords in your terminal

with open("passwords_generator\\Pass_Generated.txt", "r", encoding="utf-8") as test:
    for line in test:
        print(line.strip())
