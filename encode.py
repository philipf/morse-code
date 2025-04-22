#!/usr/bin/env python3
"""
Morse Code Encoder - Converts English text to Morse code
"""

import argparse
import sys
from morse_utils import CHAR_TO_MORSE, validate_english_text, read_from_file, write_to_file

def encode_to_morse(text):
    """
    Converts English text to Morse code.
    
    Args:
        text (str): Text to be encoded
        
    Returns:
        str: Morse code representation
    """
    valid, error_msg = validate_english_text(text)
    if not valid:
        raise ValueError(error_msg)
    
    morse_words = []
    for word in text.upper().split():
        morse_letters = []
        for char in word:
            if char in CHAR_TO_MORSE:
                morse_letters.append(CHAR_TO_MORSE[char])
        morse_words.append(' '.join(morse_letters))
    
    return ' / '.join(morse_words)

def main():
    """Main function for CLI operation"""
    parser = argparse.ArgumentParser(description='Convert English text to Morse code')
    
    parser.add_argument('text', nargs='?', help='Text to encode to Morse code')
    parser.add_argument('--input', '-i', help='Input file containing text to encode')
    parser.add_argument('--output', '-o', help='Output file to write Morse code to')
    
    args = parser.parse_args()
    
    # Get input text
    if args.text:
        input_text = args.text
    elif args.input:
        try:
            input_text = read_from_file(args.input)
        except (FileNotFoundError, IOError) as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    else:
        parser.print_help()
        return 0
    
    # Encode text to Morse code
    try:
        morse_code = encode_to_morse(input_text)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    # Output Morse code
    if args.output:
        try:
            write_to_file(args.output, morse_code)
        except IOError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    else:
        print(morse_code)
    
    return 0

if __name__ == '__main__':
    sys.exit(main()) 