'''
gerador de senhas com python

1 - receber 3 parâmetros como base ex: nome, idade, data de nascimento (xx/xx/xxxx)

2 - gerar as versões minúsculas e maiúscula do nome e recortar a data de nascimentos.


gerar cifras e permutações com esses parâmetros



'''

def pass_generator(nome, idade, data_de_nascimento):
    data_formatada = data_de_nascimento.split("/") #separa a data de nascimento por '/'
    dia, mes, ano = data_formatada[0], data_formatada[1], data_formatada[2] #salva o dia, mes e ano de nascença de acordo com o índice de 'data_formatada' que agora é uma lista
    
    nome_m = nome.lower().replace(" ", "") #gera a versão minúiscula do nome completo
    nome_M = nome.upper().replace(" ", "") #gera a versão minúscula do nome completo
    
    partes = nome.split() #separa a o nome para poder saber qual o primeiro nome, nome do meio, último nome

    primeiro_nome = partes[0] # fala que o primeiro nome é igual ao primeiro indice '0' da lista 'partes' que foi criada a cima
  
    nome_do_meio = " ".join(partes[1:-1]) if len(partes) > 2 else "" # Se tiver mais de dois nomes, o meio é tudo entre o primeiro e o último
    ultimo_nome = partes[-1] if len(partes) > 1 else "" #salva o ultimo nome

    idade_ = idade #reatribuição a variável idade, para melhor usabilidade posteriormente

    senha_teste = "" #As senhas geradas serão salvas aqui


  #em dev
    for caractere in nome_m:
        senha_teste += caractere
        for caracteres in nome_m:
            if caracteres not in senha_teste:
                senha_teste += caracteres
    else:
        print(senha_teste)
  #em dev

pass_generator("Lucas Paulino da silva", 17, "29/08/2007") #testa passando os parametreos

import os #importa a biblioteca os (mexer com o sistema)

def save_to_txt(senhas):
  if not os.path.exists("pass.txt"): #se o arquivo "pass.txt" não existir, cria um
    with open("pass.txt", "w", encoding = "utf-8-sig") as senhas: #abre o arquivo e escreve as senhas 
      conteudo = f"{senha_teste}\n"
      senhas.write(conteudo)
      
  

