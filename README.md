# 🔐 kpass — Smart Password Generator & Evaluator

<p align="center">
  <img src="assets/kpass_icon.png" alt="kpass logo" width="100%"/>
</p>

**kpass** is a Python toolkit for **generating**, **ciphering** and **evaluating** passwords—designed for **educational**, **testing** and **automation** scenarios.

---

## ✨ Features

* **Generate** hundreds or thousands of password combinations from:

  * Full name
  * Age
  * Birth date
* **Leet‑speak** substitutions like `A → 4`, `E → 3`, `S → $`
* **Strength evaluation** based on:

  * Length
  * Digits
  * Special characters
  * Mixed case
  * Numeric sequence patterns
* **Export** automatically to `.json`, `.csv` or `.yaml` with a progress bar powered by **rich**

---

## ⚠️ Security Disclaimer

This project **does not** produce secure passwords for production systems.
It uses **predictable** inputs (names, dates) and should **not** be used for real authentication.

---

## 🎯 Use Cases

* 🧠 **Cybersecurity Awareness**
  Learn why personal info makes weak passwords.

* 🧰 **Pentesting & Wordlist Creation**
  Build custom dictionaries for ethical hacking.

* 🧪 **Automation & Testing**
  Generate dummy passwords for scripts, bots or sandbox environments.

---

## 📦 Installation

```bash
pip install kpass-gen
```

> Requires Python 3.6+

---

## 🚀 Quick Start

### 1. Generate Passwords

```python
from kpass import generator

# Generates passwords, evaluates strength, and saves to pass_generated.json
generator(
    name="Lucas Paulino",
    age="17",
    birth_date="29/08/2007",
    file_type="json",        # optional: json, csv, yaml or yml
    file_name="my_passwords" # optional: filename without extension
)
```

### 2. Apply Leet Cipher

```python
from kpass import apply_ciphers

leet = apply_ciphers("Panam Palmer")
print(leet)  # → "|D4|\\|4/\\/\\ |D41/\\/\\312"
```

### 3. Save Custom Password Lists

```python
from kpass import save_to_file

passwords = ["2077!", "Johnny34@", "V24!23"]
scores    = [2, 4, 3]
verdicts  = ["#weak", "#good", "#mean"]

save_to_file(
    passwords,
    scores,
    verdicts,
    file_name="results",
    file_type="csv"    # outputs results.csv
)
```

### 4. Check Password Strength

```python
from kpass import verify

# returns "#very_strong"
print(verify("J4ckw$$l190s"))

# returns 6
print(verify("J4ckw$$l190s", want_verdict=False))
```

---

## 🔧 API Reference

| Function                                                          | Description                                                                 |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `generator(name, age, birth_date, file_type, file_name)`          | Generates permutations, evaluates strength, and saves to a file             |
| `apply_ciphers(text)`                                             | Applies leet‑speak substitutions                                            |
| `save_to_file(passwords, scores, verdicts, file_name, file_type)` | Exports password list + scores + verdicts with a progress bar               |
| `verify(password, want_verdict=True)`                             | Evaluates strength; returns an `int` score or `str` verdict (`#good`, etc.) |
| `check_sequences(password)`                                       | Detects ascending/descending numeric sequences                              |
| `veredict(score)`                                                 | Maps numeric score to verdict string (`#weak`, `#strong`, etc.)             |

---

## ✅ Requirements

* Python 3.6 or higher
* [rich](https://pypi.org/project/rich/) for progress bars

---

## 📄 License

MIT License — free to use, modify and share.