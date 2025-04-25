from passgen import pass_generator, save_to_txt

nome = input("Digite seu nome completo: ")
idade = input("Digite sua idade: ")
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

senhas = pass_generator(nome, idade, data)
save_to_txt(senhas)

print(f"{len(senhas)} senhas geradas e salvas com sucesso!")
