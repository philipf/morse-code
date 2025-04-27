# Morse Code Encoder/Decoder

A Python application to convert English text to Morse code and vice versa.

## Features

- Convert English text to Morse code
- Convert Morse code to English text
- Input from command line arguments or files
- Output to standard output or files
- Support for all 26 English letters (case-insensitive), numbers 0-9, and basic punctuation
- Option to skip characters that cannot be converted to Morse code

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/philipf/morse-code.git
   cd morse-code
   ```

2. (Optional) Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Encoding (English to Morse Code)

To encode English text to Morse code:

```
python encode.py [--input INPUT_FILE] [--output OUTPUT_FILE] [--skip-unknown] [text_to_encode]
```

Examples:
```
# Encode text from command line
python encode.py "Hello World"

# Encode text from a file
python encode.py --input input.txt

# Encode text and save to a file
python encode.py "Hello World" --output output.txt

# Encode text from a file and save to another file
python encode.py --input input.txt --output output.txt

# Encode text with unsupported characters by skipping them
python encode.py "Hello © World" --skip-unknown
```

### Decoding (Morse Code to English)

To decode Morse code to English text:

```
python decode.py [--input INPUT_FILE] [--output OUTPUT_FILE] [morse_to_decode]
```

Examples:
```
# Decode Morse code from command line
python decode.py ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

# Decode Morse code from a file
python decode.py --input morse.txt

# Decode Morse code and save to a file
python decode.py ".... . .-.. .-.. ---" --output decoded.txt

# Decode Morse code from a file and save to another file
python decode.py --input morse.txt --output decoded.txt
```

## Morse Code Format

- Space between letters: 1 space
- Space between words: 1 forward slash

## Running Tests

To run the tests:

```
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
