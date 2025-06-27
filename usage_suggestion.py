# Just a suggestion for use
from generator import generator
from rich import print

full_name = input("Enter your full name: ")
age = input("Enter your age: ")
data = input("Enter your date of birth (dd/mm/yyyy): ")

passwords = pass_generator(full_name, age, data)

print(f"[bold green]{len(passwords)}[/] [cyan]senhas geradas e salvas com sucesso![/]")
