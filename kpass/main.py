import itertools
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn
import re
import string

# -----------------------------------------------------------------------------
# Ciphers dictionary to replace letters with leetspeak equivalents
# Each key is a character and the corresponding value is its cipher substitution
# -----------------------------------------------------------------------------

ciphers = {
    "A": "4", "a": "4", "Á": "4", "á": "4", "@": "4",
    "B": "8", "b": "8",
    "C": "(", "c": "(",
    "D": "[)", "d": "[)",
    "E": "3", "e": "3", "É": "3", "é": "3", "&": "3",
    "F": "#", "f": "#",
    "G": "6", "g": "6",
    "H": "#", "h": "#",
    "I": "1", "i": "1", "Í": "1", "í": "1", "!": "1",
    "J": "_|", "j": "_|",
    "K": "|<", "k": "|<",
    "L": "1", "l": "1",
    "M": "/\\/\\", "m": "/\\/\\",
    "N": "|\\|", "n": "|\\|",
    "O": "0", "o": "0", "Ó": "0", "ó": "0",
    "P": "|D", "p": "|D",
    "Q": "0_", "q": "0_",
    "R": "12", "r": "12",
    "S": "$", "s": "$", "Š": "$", "š": "$",
    "T": "7", "t": "7",
    "U": "(_)", "u": "(_)",
    "V": "\\/", "v": "\\/",
    "W": "\\/\\/", "w": "\\/\\/",
    "X": "%", "x": "%",
    "Y": "`/", "y": "`/",
    "Z": "2", "z": "2"
}

# -----------------------------------------------------------------------------
# Function: aplly_ciphers
# Description:
#   Transforms input text by replacing each character according to the ciphers dict
# Parameters:
#   text (str): The original text to be ciphered
# Returns:
#   str: The transformed text with cipher substitutions
# -----------------------------------------------------------------------------

def aplly_ciphers(text: str) -> str:
    return ''.join(ciphers.get(char, char) for char in text)

# -----------------------------------------------------------------------------
# Function: save_to_file
# Description:
#   Writes a list of passwords to a text file, showing progress in the console
# Parameters:
#   passwords (list[str]): List of password strings to save
#   file_name (str): Output filename (default: 'pass_generated.txt')
# Returns:
#   None
# -----------------------------------------------------------------------------

def save_to_file(
        passwords: list[str],
        scores: list[int],
        veredicts: list[str],
        file_name: str | None = "pass_generated",
        extension: str | None = "json"        
) -> None:
    with open(f"{file_name}.{extension}", "w", encoding="utf-8-sig") as file:
        lista = []
        minu = extension.lower()
        maxin = extension.upper()
        
        match (extension.lower()):
            case "json" | ".json":
                with Progress(
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TimeElapsedColumn(),
                ) as progress:
                    tarefa = progress.add_task("[cyan]Saving passwords...", total=len(passwords))
                    for pwd, score, veredict_ in zip(passwords, scores, veredicts):
                        file.write(base_files_architeture(pwd, score, veredict_, extension))
                        progress.update(tarefa, advance=1)
            
            case "csv" | ".csv":
                with Progress(
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TimeElapsedColumn(),
                ) as progress:
                    tarefa = progress.add_task("[cyan]Saving passwords...", total=len(passwords))
                    for pwd, score, veredict_ in zip(passwords, scores, veredicts):
                        file.write(base_files_architeture(pwd, score, veredict_, extension))
                        progress.update(tarefa, advance=1)

            case "yaml" | ".yaml" | "yml" | ".yml":
                with Progress(
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TimeElapsedColumn(),
                ) as progress:
                    tarefa = progress.add_task("[cyan]Saving passwords...", total=len(passwords))
                    for pwd, score, veredict_ in zip(passwords, scores, veredicts):
                        file.write(base_files_architeture(pwd, score, veredict_, extension.upper()))
                        progress.update(tarefa, advance=1)

            case _:
                return print("#file type is not supported")    

        # with Progress(
        #     TextColumn("[progress.description]{task.description}"),
        #     BarColumn(),
        #     TimeElapsedColumn(),
        # ) as progress:
        #     tarefa = progress.add_task("[cyan]Saving passwords...", total=len(passwords))
        #     for pwd in passwords:
        #         file.write(pwd + "\n")
        #         progress.update(tarefa, advance=1)

# -----------------------------------------------------------------------------
# Function: generator
# Description:
#   Builds possible password permutations based on user info and ciphers,
#   filters by length, and saves them using save_to_txt()
# Parameters:
#   name (str): Full name input for generating bases
#   age (str): Age string (e.g., '25')
#   birth_date (str): Birth date in 'DD/MM/YYYY' format
# Returns:
#   None (calls save_to_txt internally)
# -----------------------------------------------------------------------------

def base_files_architeture(password, score, veredict_, file_type):
    if file_type.lower() in ("json", ".json"):
        return (
            '{\n'
            f'  "password": "{password}",\n'
            f'  "score": "{score}",\n'
            f'  "veredict": "{veredict_}"\n'
            '}'
        )
    
    if file_type.lower() in ("csv", ".csv"):
        return (
        f'"password","{password}",\n'
        f'"score","{score}",\n'
        f'"veredict,"{veredict_}"\n'
        )

    
    if file_type.lower() in ("yaml", ".yaml", "yml", ".yml") or file_type.upper() in ("YAML", ".YAML", "YML", ".YML"):
        return (
        f'"password": "{password}"\n'
        f'"score": "{score}"\n'
        f'"veredict: "{veredict_}"\n'
        )

def generator(name: str, age: str, birth_date: str, fyle_type: str | None = "json", fyle_name: str | None = "pass_generated") -> None:
    # Split birth_date into components
    day, month, year = birth_date.split("/")

    # Normalize variants of the name
    name_tiny = name.lower().replace(" ", "")
    name_capital = name.upper().replace(" ", "")

    parts = name.split()
    first = parts[0]
    middle = "".join(parts[1:-1]) if len(parts) > 2 else ""
    last = parts[-1] if len(parts) > 1 else ""

    # Reverse age string for variation
    age_reversed = age[::-1]

    # Base building blocks for passwords
    base_combinations = [
        name_tiny, name_capital, first, middle, last,
        day, month, year,
        age, age_reversed,
        aplly_ciphers(name_tiny), aplly_ciphers(first), aplly_ciphers(last)
    ]

    # Remove duplicates and empty strings
    base_combinations = list({item for item in base_combinations if item.strip()})

    possible_passwords = set()
    possible_scores = set()
    possible_veredicts = set()

    # Calculate total permutations for progress bar
    total = sum(len(list(itertools.permutations(base_combinations, i))) for i in range(2, 5))

    with Progress(
        TextColumn("[cyan]Generating passwords..."),
        BarColumn(),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("passwords", total=total)
        for length in range(2, 5):
            for combo in itertools.permutations(base_combinations, length):
                pwd = "".join(combo)
                if 6 <= len(pwd) <= 18:
                    possible_passwords.add(pwd)
                progress.update(task, advance=1)

        scores = [verify(password, False) for password in possible_passwords]
        veredicts = [verify(password) for password in possible_passwords]
        
        task2 = progress.add_task("scores", total=len(veredicts) - 1)
        for length in range(2, 5):
            for combo in itertools.permutations(base_combinations, length):
                veredicts_list = "".join(combo)
                if 6 <= len(veredicts_list) <= 18:
                    possible_veredicts.add(pwd)
                progress.update(task2, advance=1)
        
        task3 = progress.add_task("scores", total=len(scores) - 1)
        for length in range(2, 5):
            for combo in itertools.permutations(base_combinations, length):
                scores_list = "".join(combo)
                if 6 <= len(scores_list) <= 18:
                    possible_scores.add(pwd)
                progress.update(task2, advance=1)

        

    # Save results to file
    save_to_file(list(possible_passwords), list(possible_scores), list(possible_veredicts), fyle_name, fyle_type)

# -----------------------------------------------------------------------------
# Function: check_sequences
# Description:
#   Detects ascending or descending numeric sequences of length 3 in password
# Parameters:
#   password (str): The password string to check
# Returns:
#   bool: True if a sequence is found, False otherwise
# -----------------------------------------------------------------------------

def check_sequences(password: str) -> bool:
    digits = [int(c) for c in password if c.isdigit()]
    for i in range(len(digits) - 2):
        if digits[i] + 1 == digits[i+1] == digits[i+2] - 1:
            return True
        if digits[i] - 1 == digits[i+1] == digits[i+2] + 1:
            return True
    return False

# -----------------------------------------------------------------------------
# Function: veredict
# Description:
#   Maps numeric strength score to a hashtag-based verdict string
# Parameters:
#   score (int): Numeric strength score (0-6)\# Returns:
#   str: Verdict hashtag
# -----------------------------------------------------------------------------

def veredict(score: int) -> str:
    levels = [
        "#very_weak",   # 0
        "#weak",        # 1
        "#weak",        # 2
        "#mean",        # 3
        "#good",        # 4
        "#strong",      # 5
        "#very_strong"  # 6
    ]
    # Safeguard for out-of-range scores
    return levels[score] if 0 <= score < len(levels) else "#unknown"

# -----------------------------------------------------------------------------
# Function: verify
# Description:
#   Evaluates password strength by checking length, digits, punctuation,
#   case variety, and absence of predictable sequences
# Parameters:
#   password (str): Password string to evaluate
#   want_verdict (bool): If True, return textual verdict; else, return numeric score
# Returns:
#   int | str: Numerical strength score or verdict string for you to treat the values ​​as you wish, the values ​​(int) range from 0 - 6
# -----------------------------------------------------------------------------

def verify(
    password: str,
    want_verdict: bool = True,
) -> int | str:
    strength = 0

    # Length check (>=8 chars)
    if len(password) >= 8:
        strength += 1

        # Digit presence
        if re.search(r'\d', password):
            strength += 1

            # Special character presence
            if any(c in string.punctuation for c in password):
                strength += 1

                # Uppercase letter presence
                if any(c.isupper() for c in password):
                    strength += 1

                # Lowercase letter presence
                if any(c.islower() for c in password):
                    strength += 1

                # Sequence check (deduct if predictable)
                if not check_sequences(password):
                    strength += 1

    # Return verdict or raw score
    return veredict(strength) if want_verdict else strength

generator("Lucas", "17", "29/08/2007", ".yml")