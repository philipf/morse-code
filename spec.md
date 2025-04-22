# Morse Code Encoder/Decoder Specification

## Overview
A Python application to convert English text to Morse code and vice versa. The application consists of two main components:
1. `encode.py` - Converts English text to Morse code
2. `decode.py` - Converts Morse code to English text

## Requirements

### Functional Requirements
1. Both programs must accept input from:
   - Command line arguments
   - Input files
2. Both programs must support output to:
   - Standard output (default)
   - Specified output files
3. The encoder must accurately convert all alphanumeric characters and common punctuation to Morse code
4. The decoder must accurately convert valid Morse code back to English text
5. Both programs must handle errors gracefully, including invalid inputs

### Technical Specifications

#### Morse Code Standard
- Use International Morse Code standard
- Space between letters: 1 space
- Space between words: 3 spaces
- Characters supported:
  - All 26 English letters (A-Z, case-insensitive)
  - Numbers 0-9
  - Basic punctuation (., ,, ?, !, /, -, etc.)

#### Command Line Interface
- `encode.py`:
  ```
  python encode.py [--input INPUT_FILE] [--output OUTPUT_FILE] [text_to_encode]
  ```
- `decode.py`:
  ```
  python decode.py [--input INPUT_FILE] [--output OUTPUT_FILE] [morse_to_decode]
  ```

#### Input/Output Handling
- If both command line text and input file are provided, prioritize command line text
- If no input is provided, display usage help
- If no output file is specified, print to stdout
- Input files should be read as plain text
- Output files should be written as plain text

### Testing Requirements
- Comprehensive unit tests using pytest
- Test all supported characters for encoding/decoding
- Test input/output from both files and command line
- Test error handling for invalid inputs
- Test edge cases (empty input, very long input, etc.)

## Implementation Details

### Project Structure 


morse-code/
├── encode.py # English to Morse code encoder
├── decode.py # Morse code to English decoder
├── morse_utils.py # Shared utilities and mappings
├── tests/ # Unit tests directory
│ ├── test_encode.py # Tests for encoder
│ ├── test_decode.py # Tests for decoder
│ └── test_utils.py # Tests for utilities
├── README.md # Project documentation
└── requirements.txt # Dependencies (pytest)

### Morse Code Mapping
The application will use standard International Morse Code mapping for all supported characters.

## Future Enhancements (Optional)
- Support for audio output of Morse code
- Additional character set support
- Web-based interface 