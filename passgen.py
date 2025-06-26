import itertools

# Ciphers dictionary to replace letters
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


# Function to apply ciphers to text
def aplly_ciphers(text):
    return ''.join(ciphers.get(char, char) for char in text)

# Function to generate passwords
def pass_generator(name, age, birth_date):
    day, month, yaer = birth_date.split("/")

    name_tiny = name.lower().replace(" ", "")
    name_capital = name.upper().replace(" ", "")

    parts_name = name.split()
    first = parts_name[0]
    middle = "".join(parts_name[1:-1]) if len(parts_name) > 2 else ""
    last = parts_name[-1] if len(parts_name) > 1 else ""

    age_reversed  = age[::-1]

    base_combinations = [
        name_tiny, name_capital, first, middle, last,
        day, month, yaer,
        age, age_reversed ,
        aplly_ciphers(name_tiny), aplly_ciphers(first), aplly_ciphers(last)
    ]

    # Remove empty and duplicate strings
    base_combinations = list(set(filter(lambda x: x.strip() != "", base_combinations)))

    possible_passwords = set()

    # Generates combinations of 2 to 4 base elements
    for i in range(2, 5):
        for combo in itertools.permutations(base_combinations, i):
            password = "".join(combo)
            if 6 <= len(password) <= 18:
                possible_passwords.add(password)

    return list(possible_passwords)

# Function to save passwords to file
def save_to_txt(passwords, file_name="pass_generated.txt"):
    with open(file_name, "w", encoding="utf-8") as file:
        for password in passwords:
            file.write(password + "\n")
