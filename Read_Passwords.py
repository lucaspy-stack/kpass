# Just to see the passwords in your terminal

with open("pass_generated.txt", "r", encoding="utf-8") as test:
    for line in test:
        print(line.strip())
