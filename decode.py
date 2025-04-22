#!/usr/bin/env python3
"""
Morse Code Decoder - Converts Morse code to English text
"""

import argparse
import sys
import re
from morse_utils import MORSE_TO_CHAR, validate_morse_code, read_from_file, write_to_file

def decode_from_morse(morse_code):
    """
    Converts Morse code to English text.
    
    Args:
        morse_code (str): Morse code to be decoded
        
    Returns:
        str: Decoded English text
    """
    valid, error_msg = validate_morse_code(morse_code)
    if not valid:
        raise ValueError(error_msg)
    
    # Normalize the morse code string
    morse_code = morse_code.strip()
    
    # Replace any combination of spaces and slashes with a standard word separator
    morse_code = re.sub(r'\s*/\s*', ' / ', morse_code)
    
    words = []
    for word in morse_code.split(' / '):
        letters = []
        for letter in word.strip().split(' '):
            if letter:  # Skip empty strings
                letters.append(MORSE_TO_CHAR.get(letter, ''))
        words.append(''.join(letters))
    
    return ' '.join(words)

def main():
    """Main function for CLI operation"""
    parser = argparse.ArgumentParser(description='Convert Morse code to English text')
    
    parser.add_argument('morse', nargs='?', help='Morse code to decode')
    parser.add_argument('--input', '-i', help='Input file containing Morse code to decode')
    parser.add_argument('--output', '-o', help='Output file to write decoded text to')
    
    args = parser.parse_args()
    
    # Get input Morse code
    if args.morse:
        input_morse = args.morse
    elif args.input:
        try:
            input_morse = read_from_file(args.input)
        except (FileNotFoundError, IOError) as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    else:
        parser.print_help()
        return 0
    
    # Decode Morse code to text
    try:
        decoded_text = decode_from_morse(input_morse)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    # Output decoded text
    if args.output:
        try:
            write_to_file(args.output, decoded_text)
        except IOError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    else:
        print(decoded_text)
    
    return 0

if __name__ == '__main__':
    sys.exit(main()) 