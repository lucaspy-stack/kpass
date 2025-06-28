# 🔐 kpass — Smart Password Generator & Evaluator

<p align="center">
  <img src="assets/kpass_icon.png" alt="kpass logo" width="100%"/>
</p>

**kpass** é uma toolkit em Python para **gerar**, **cipherizar** e **avaliar** senhas — voltado a cenários de **educação**, **testes** e **automação**.

---

## ✨ Funcionalidades

* **Geração** de centenas ou milhares de combinações de senha a partir de:

  * Nome completo
  * Idade
  * Data de nascimento
* **Leet-speak**: substituições como `A → 4`, `E → 3`, `S → $`
* **Avaliação de força** da senha por meio de:

  * Comprimento
  * Dígitos
  * Caracteres especiais
  * Mix de maiúsculas/minúsculas
  * Detecção de sequências numéricas
* **Exportação** automática para `.json`, `.csv` ou `.yaml` com barra de progresso via `rich`

---

## ⚠️ Aviso de Segurança

Este projeto **não** gera senhas seguras para sistemas reais.
Ele usa dados **previsíveis** (nomes, datas), por isso não deve ser usado em ambientes de produção.

---

## 🎯 Casos de Uso

* 🧠 **Conscientização em Cibersegurança**
  Entenda por que informações pessoais formam senhas fracas.

* 🧰 **Pentesting & Wordlists**
  Crie listas de senhas para testes éticos.

* 🧪 **Automação & Testes**
  Gere senhas de teste para scripts, bots e ambientes sandbox.

---

## 📦 Instalação

```bash
pip install kpass-gen
```

> Requer Python 3.6+

---

## 🚀 Exemplos de Uso

### 1. Gerar Senhas

```python
from kpass import generator

# gera senhas, avalia força e salva em pass_generated.json
generator(
    name="Lucas Paulino",
    age="17",
    birth_date="29/08/2007",
    file_type="json",      # opcional: json, csv, yaml ou yml
    file_name="minhas_senhas"  # opcional: nome do arquivo sem extensão
)
```

### 2. Aplicar Leet Cipher

```python
from kpass import apply_ciphers

leet = apply_ciphers("Panam Palmer")
print(leet)  # → "|D4|\|4/\/\ |D41/\/\312"
```

### 3. Salvar Listas de Senha Manualmente

```python
from kpass import save_to_file

passwords = ["2077!", "Johnny34@", "V24!23"]
scores    = [2, 4, 3]
verdicts  = ["#weak", "#good", "#mean"]

save_to_file(
    passwords,
    scores,
    verdicts,
    file_name="resultados",
    file_type="csv"    # gera resultados.csv
)
```

### 4. Verificar Força de Senha

```python
from kpass import verify

# retorna "#very_strong"
print(verify("J4ckw$$l190s"))

# retorna 6
print(verify("J4ckw$$l190s", want_verdict=False))
```

---

## 🔧 API Reference

| Função                                                            | Descrição                                                            |
| ----------------------------------------------------------------- | -------------------------------------------------------------------- |
| `generator(name, age, birth_date, file_type, file_name)`          | Gera combinações, avalia e salva em arquivo (`.json`/`.csv`/`.yaml`) |
| `apply_ciphers(text)`                                             | Substitui caracteres por leet-speak                                  |
| `save_to_file(passwords, scores, verdicts, file_name, file_type)` | Exporta listas de senhas+pontuação+veredito com barra de progresso   |
| `verify(password, want_verdict=True)`                             | Avalia força; retorna `int` ou `str` (#weak, #good, etc.)            |
| `check_sequences(password)`                                       | Detecta sequências numéricas ascendentes/descendentes                |
| `veredict(score)`                                                 | Converte `int` de força em string de veredito (`#weak`, `#good`…)    |

---

## ✅ Requisitos

* Python 3.6 ou superior
* [rich](https://pypi.org/project/rich/) para barras de progresso

---

## 📄 Licença

MIT License — use, modifique e compartilhe livremente.
