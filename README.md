
# passwords_generator

A Python library that generates passwords based on 3 parameters: name, age, and birth date (e.g., dd/mm/yyyy).

<img src="https://skillicons.dev/icons?i=python" />

## Table of contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Overview
The **passwords_generator** is a simple module that, given a full name, age, and birth date, generates password combinations between 6 and 18 characters, using case variations, reversal, and character substitutions (A→4, S→$, E→&).

## Installation

1. **Prerequisites**  
   - Python 3.6 or higher installed.
2. **Clone this repository**  
   ```bash
   git clone https://github.com/lucaspy-stack/passwords_generator.git
   cd passwords_generator
   ```

3. *(Optional)* Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

## Usage

There are three main scripts in the project:

1. **Password generator** (`Password_Generator.py`)  
   Runs an interactive prompt:

   ```bash
   python Password_Generator.py
   ```

   You will be asked to enter:

   * **Full name** (e.g., “Maria Silva”)
   * **Age** (e.g., “30”)
   * **Birth date** (e.g., “15/08/1994”)

   At the end, a `Pass_Generated.txt` file will be created with all the generated passwords.

2. **Password reader** (`Read_Passwords.py`)  
   To display generated passwords in the terminal:

   ```bash
   python Read_Passwords.py
   ```

3. **Using as a library**  
   In your own Python code, import the functions:

   ```python
   from Pass_Generated import pass_generator, save_to_txt

   full_name = "João da Silva"
   age = "25"
   birth_date = "10/05/1999"

   passwords = pass_generator(full_name, age, birth_date)
   save_to_txt(passwords, file_name="Pass_Generated.txt")
   ```

### Example output in the `pass_generated.txt` file

```
MariaSilva94
mariasilva94
M4r14$1lv4
... (more combinations)
```

## License

This project has no defined license. Feel free to use and adapt it as you wish.  
*Tip:* if you want to release it publicly, consider using a license like MIT or Apache 2.0.

## Contact

* **Email:** [lucas.workps@gmail.com](mailto:lucas.workps@gmail.com)  
* **GitHub:** [https://github.com/lucaspy-stack](https://github.com/lucaspy-stack)  
