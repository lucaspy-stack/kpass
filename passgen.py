import itertools

# Dicionário de cifras para substituir letras
cifras = {"A": "4", "S": "$", "E": "&", "a": "4", "s": "$", "e": "&"}

# Função para aplicar cifra no texto
def aplicar_cifras(texto):
    return ''.join(cifras.get(char, char) for char in texto)

# Função para gerar senhas
def pass_generator(nome, idade, data_nascimento):
    dia, mes, ano = data_nascimento.split("/")

    nome_m = nome.lower().replace(" ", "")
    nome_M = nome.upper().replace(" ", "")

    partes_nome = nome.split()
    primeiro = partes_nome[0]
    meio = "".join(partes_nome[1:-1]) if len(partes_nome) > 2 else ""
    ultimo = partes_nome[-1] if len(partes_nome) > 1 else ""

    idade_invertida = idade[::-1]

    combinacoes_base = [
        nome_m, nome_M, primeiro, meio, ultimo,
        dia, mes, ano,
        idade, idade_invertida,
        aplicar_cifras(nome_m), aplicar_cifras(primeiro), aplicar_cifras(ultimo)
    ]

    # Remove strings vazias e duplicadas
    combinacoes_base = list(set(filter(lambda x: x.strip() != "", combinacoes_base)))

    senhas_possiveis = set()

    # Gera combinações de 2 até 4 elementos da base
    for i in range(2, 5):
        for combo in itertools.permutations(combinacoes_base, i):
            senha = "".join(combo)
            if 6 <= len(senha) <= 18:
                senhas_possiveis.add(senha)

    return list(senhas_possiveis)

# Função para salvar as senhas em arquivo
def save_to_txt(senhas, nome_arquivo="pass_generated.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for senha in senhas:
            arquivo.write(senha + "\n")
