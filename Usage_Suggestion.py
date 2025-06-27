# Just a suggestion for use
from Password_Generator import pass_generator, save_to_txt
from rich import print

full_name = input("Enter your full name: ")
age = input("Enter your age: ")
data = input("Enter your date of birth (dd/mm/yyyy): ")

passwords = pass_generator(full_name, age, data)
save_to_txt(passwords)

print(f"[bold green]{len(passwords)}[/] [cyan]senhas geradas e salvas com sucesso![/]")