"""
Utility functions and mappings for Morse code operations.
"""

# Dictionary mapping characters to Morse code
CHAR_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    
}

# Dictionary mapping Morse code to characters
MORSE_TO_CHAR = {v: k for k, v in CHAR_TO_MORSE.items()}


def validate_english_text(text):
    """
    Validates if the input text can be encoded to Morse code.

    Args:
        text (str): Text to be validated

    Returns:
        tuple: (is_valid, error_message)
    """
    if not text:
        return False, "Input text is empty"

    for char in text.upper():
        # Skip spaces
        if char == " ":
            continue

        if char not in CHAR_TO_MORSE:
            return False, f"Character '{char}' cannot be converted to Morse code"

    return True, ""


def validate_morse_code(morse_code):
    """
    Validates if the input is valid Morse code.

    Args:
        morse_code (str): Morse code to be validated

    Returns:
        tuple: (is_valid, error_message)
    """
    if not morse_code:
        return False, "Input Morse code is empty"

    # Normalize forward slashes by handling any combination of spaces around them
    morse_code = morse_code.strip()
    morse_code = morse_code.replace(' / ', '/')  # Remove spaces around slash
    morse_code = morse_code.replace(' /', '/')   # Remove space before slash
    morse_code = morse_code.replace('/ ', '/')   # Remove space after slash
    morse_code = morse_code.replace('/', ' / ')  # Add normalized spacing

    words = morse_code.strip().split(" / ")
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            if letter and letter not in MORSE_TO_CHAR:
                return False, f"Morse code '{letter}' does not match any character"

    return True, ""


def read_from_file(file_path):
    """
    Reads content from a file.

    Args:
        file_path (str): Path to the input file

    Returns:
        str: Content of the file

    Raises:
        FileNotFoundError: If the file is not found
        IOError: If there's an error reading the file
    """
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {file_path}")
    except IOError:
        raise IOError(f"Error reading file: {file_path}")


def write_to_file(file_path, content):
    """
    Writes content to a file.

    Args:
        file_path (str): Path to the output file
        content (str): Content to write

    Raises:
        IOError: If there's an error writing to the file
    """
    try:
        with open(file_path, "w") as f:
            f.write(content)
    except IOError:
        raise IOError(f"Error writing to file: {file_path}")
