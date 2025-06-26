
# passwords_generator

Uma biblioteca em Python que gera senhas com base em 3 parâmetros: nome, idade e data de nascimento (ex: dd/mm/aaaa).

<img src="https://skillicons.dev/icons?i=python" />

## Table of contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Overview
O **passwords_generator** é um módulo simples que, dado um nome completo, idade e data de nascimento, gera combinações de senhas entre 6 e 18 caracteres, usando variações de caixa, inversão e substituições de caracteres (A→4, S→$, E→&).

## Installation

1. **Pré-requisitos**  
   - Python 3.6 ou superior instalado.
2. **Clone este repositório**  
   ```bash
   git clone https://github.com/lucaspy-stack/passwords_generator.git
   cd passwords_generator
   ```

3. *(Opcional)* Crie e ative um virtualenv:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
4. **Instale dependências**  
   Não há bibliotecas externas além da stdlib, mas se quiser isolá-las:

   ```bash
   pip install -r requirements.txt  # (nenhum pacote, o arquivo pode nem existir)
   ```
5. **Instale como pacote local** *(opcional)*

   ```bash
   pip install .
   ```

## Usage

Há três scripts principais no projeto:

1. **Gerador de senhas** (`ksenhas.py`)  
   Executa um prompt interativo:

   ```bash
   python ksenhas.py
   ```

   Você será solicitado a informar:

   * **Nome completo** (ex: “Maria Silva”)
   * **Idade** (ex: “30”)
   * **Data de nascimento** (ex: “15/08/1994”)

   Ao final, será criado o arquivo `pass_generated.txt` com todas as senhas geradas.

2. **Leitor de senhas** (`lersenhas.py`)  
   Para exibir no terminal as senhas já geradas:

   ```bash
   python lersenhas.py
   ```

3. **Uso como biblioteca**  
   No seu próprio código Python, importe as funções:

   ```python
   from passgen import pass_generator, save_to_txt

   nomes = "João da Silva"
   idade = "25"
   data = "10/05/1999"

   senhas = pass_generator(nomes, idade, data)
   save_to_txt(senhas, nome_arquivo="minhas_senhas.txt")
   ```

### Exemplo de saída no arquivo `pass_generated.txt`

```
MariaSilva94
mariasilva94
M4r14$1lv4
... (mais combinações)
```

## License

Este projeto está sem licença definida. Sinta-se à vontade para usar e adaptar como preferir.  
*Dica:* se quiser liberar para uso público, considere usar uma licença como MIT ou Apache 2.0.

## Contact

* **Email:** [lucaspy-stack@gmail.com](mailto:lucaspy-stack@gmail.com)  
* **GitHub:** [https://github.com/lucaspy-stack](https://github.com/lucaspy-stack)  
* **LinkedIn:** [https://www.linkedin.com/in/lucaspy-stack/](https://www.linkedin.com/in/lucaspy-stack/)

