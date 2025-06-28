# kpass

<p align="center">
  <img src="assets/kpass_icon.png" alt="kpass logo" width="100%"/>
</p>

**kpass** is a Python library that:

1. Generates hundreds (or thousands) of password combinations based on a person’s full name, age, and date of birth.  
2. Applies “leet”-style substitutions (e.g., A → 4, S → $, E → 3).  
3. Calculates **password strength** based on length, digits, special characters, casing, and numeric sequence patterns.  
4. Automatically saves generated passwords to a `.txt` file, with progress bars powered by the `rich` library.

---

## ⚠️ Disclaimer on Security

This library is **not intended for generating secure passwords** for real-life accounts or authentication systems.

kpass creates combinations based on **publicly guessable data** (like names and dates), making it predictable and unsuitable for real-world password security.

---

## 🎯 Use Cases

- 🔐 **Cybersecurity education**  
  Understand why personal info makes weak passwords.

- 📁 **Custom wordlist generation**  
  Build dictionaries for ethical hacking or pentesting contexts.

- ⚙️ **Scripting, automation & testing**  
  Create non-sensitive passwords for internal tools, bots, or sandbox projects.

- ⚠️ **Do not use for production login systems**

---

## 📦 Installation

```bash
pip install kpass-gen
```

---

🚀 Example Usage

1. Generating Passwords

```python
from kpass import generator

generator(
    name="Johnny Silverhand",
    age="34",
    birth_date="16/11/1988"
)
```

> Creates pass_generated.txt with valid passwords (6–18 chars) and a terminal progress bar.




---

2. Leet-Style Substitution

from kpass import aplly_ciphers

leet = aplly_ciphers("Panam Palmer")
print(leet)  # → "|D4|\|4/\/\ |D41/\/\312"


---

3. Saving Custom Passwords

```python
from kpass import save_to_txt

passwords = ["2077!", "Johnny34@", "V24!23"]
save_to_txt(passwords, file_name="my_passwords.txt")
```

---

### 4. Password Strength Check

```python
from kpass import verify

score = verify(password="J4ckw$$l190s", want_verdict=False)
print(score)  # → 6

label = verify(password="J4ckw$$l190s", want_verdict=True)
print(label)  # → "#very_strong"
```

Score	Verdict	Description

0	#very_weak	Very weak
1–2	#weak	Weak
3	#mean	Average
4	#good	Good
5	#strong	Strong
6	#very_strong	Very strong


> ⚠️ While this method is useful for checking password complexity (length, variation, common patterns), it is not a replacement for secure password handling. Always store passwords using proper hashing algorithms (e.g., bcrypt) and enforce policies on the backend for real authentication systems.



---

🔧 API Reference

generator(name: str, age: str, birth_date: str) -> None

Generates and saves password combinations to pass_generated.txt.

aplly_ciphers(text: str) -> str

Transforms text using internal leet-style substitution rules.

save_to_txt(passwords: list[str], file_name: str = "pass_generated.txt") -> None

Saves the password list to a text file with progress indication.

verify(password: str, want_verdict: bool = True) -> int | str

Returns a numeric score or a text-based verdict (#strong, etc).


---

✅ Requirements

Python 3.6 or higher

rich



---

📄 License

MIT License — free to use, modify and share.

---