
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
4. **Install dependencies**  
   There are no external libraries beyond the standard library, but to isolate dependencies if you want:

   ```bash
   pip install -r requirements.txt  # (no packages, the file might not even exist)
   ```
5. **Install as a local package** *(optional)*

   ```bash
   pip install .
   ```

## Usage

There are three main scripts in the project:

1. **Password generator** (`ksenhas.py`)  
   Runs an interactive prompt:

   ```bash
   python ksenhas.py
   ```

   You will be asked to enter:

   * **Full name** (e.g., “Maria Silva”)
   * **Age** (e.g., “30”)
   * **Birth date** (e.g., “15/08/1994”)

   At the end, a `pass_generated.txt` file will be created with all the generated passwords.

2. **Password reader** (`lersenhas.py`)  
   To display generated passwords in the terminal:

   ```bash
   python lersenhas.py
   ```

3. **Using as a library**  
   In your own Python code, import the functions:

   ```python
   from passgen import pass_generator, save_to_txt

   names = "João da Silva"
   age = "25"
   birth_date = "10/05/1999"

   passwords = pass_generator(names, age, birth_date)
   save_to_txt(passwords, file_name="my_passwords.txt")
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
* **LinkedIn:** [https://www.linkedin.com/in/lucaspy-stack/](https://www.linkedin.com/in/lucaspy-stack/)

