# Just to see the passwords in your terminal
import time 

with open("passwords_generator\\Pass_Generated.txt", "r", encoding="utf-8") as test:
    for line in test:
        print(line.strip())
        time.sleep(0.1)