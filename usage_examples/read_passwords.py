# Just to see the passwords in your terminal
import time 

with open("pass_generated.txt", "r", encoding="utf-8") as test:
    for line in test:
        print(line.strip())
        time.sleep(0.1)
