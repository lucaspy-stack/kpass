# Just a suggestion for use

from Password_Generator import pass_generator, save_to_txt

name = input("Enter your full name: ")
age = input("Enter your age: ")
data = input("Enter your date of birth (dd/mm/yyyy): ")

passwords = pass_generator(name, age, data)
save_to_txt(passwords)

print(f"{len(passwords)} Passwords generated and saved successfully!")
