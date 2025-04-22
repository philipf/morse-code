"""
Unit tests for decode.py
"""

import os
import sys
import pytest
import tempfile
from unittest.mock import patch

# Add parent directory to path to import decode.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from decode import decode_from_morse, main

class TestDecoder:
    """Test class for Morse code decoder"""
    
    def test_decode_single_letter(self):
        """Test decoding a single letter"""
        assert decode_from_morse(".-") == "A"
        assert decode_from_morse("-...") == "B"
    
    def test_decode_word(self):
        """Test decoding a word"""
        assert decode_from_morse(".... . .-.. .-.. ---") == "HELLO"
    
    def test_decode_sentence(self):
        """Test decoding a sentence"""
        assert decode_from_morse(".... . .-.. .-.. --- / .-- --- .-. .-.. -..") == "HELLO WORLD"

    def test_decode_sentence_relax_spaces_around_words(self):
        """Test decoding a sentence"""
        assert decode_from_morse(".... . .-.. .-.. ---/.-- --- .-. .-.. -..") == "HELLO WORLD"

    def test_decode_sentence_relax_spaces_around_words_before(self):
        """Test decoding a sentence"""
        assert decode_from_morse(".... . .-.. .-.. --- /.-- --- .-. .-.. -..") == "HELLO WORLD"        

    def test_decode_sentence_relax_spaces_around_words_after(self):
        """Test decoding a sentence"""
        assert decode_from_morse(".... . .-.. .-.. ---/ .-- --- .-. .-.. -..") == "HELLO WORLD"                
    
    def test_decode_with_punctuation(self):
        """Test decoding Morse code with punctuation"""
        assert decode_from_morse(".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--") == "HELLO, WORLD!"

    def test_decode_good_bye_sweet_world_exclamation(self):
        """Test decoding Morse code with punctuation"""
        assert decode_from_morse("--. --- --- -.. / -... -.-- . / ... .-- . . - / .-- --- .-. .-.. -.. -.-.--") == "GOOD BYE SWEET WORLD!"
    
    def test_decode_numbers(self):
        """Test decoding numbers"""
        assert decode_from_morse(".----") == "1"
        assert decode_from_morse("..---") == "2"
        assert decode_from_morse("...--") == "3"
        assert decode_from_morse("--...") == "7"
        assert decode_from_morse("---..") == "8"
        assert decode_from_morse("----.") == "9"

    def test_decode_from_chatgpt(self):
        assert decode_from_morse("-.-.--") == "!"
        assert decode_from_morse(".-..-.") == '"'
        assert decode_from_morse("...-..-") == "$"
        assert decode_from_morse(".-...") == "&"
        assert decode_from_morse(".----.") == "'"
        assert decode_from_morse("-.--.") == "("
        assert decode_from_morse("-.--.-") == ")"
        assert decode_from_morse(".-.-.") == "+"
        assert decode_from_morse("--..--") == ","
        assert decode_from_morse("-....-") == "-"
        assert decode_from_morse(".-.-.-") == "."
        assert decode_from_morse("-..-.") == "/"
        assert decode_from_morse("-----") == "0"
        assert decode_from_morse(".----") == "1"
        assert decode_from_morse("..---") == "2"
        assert decode_from_morse("...--") == "3"
        assert decode_from_morse("....-") == "4"
        assert decode_from_morse(".....") == "5"
        assert decode_from_morse("-....") == "6"
        assert decode_from_morse("--...") == "7"
        assert decode_from_morse("---..") == "8"
        assert decode_from_morse("----.") == "9"
        assert decode_from_morse("---...") == ":"
        assert decode_from_morse("-.-.-.") == ";"
        assert decode_from_morse("-...-") == "="
        assert decode_from_morse("..--..") == "?"
        assert decode_from_morse(".--.-.") == "@"
        assert decode_from_morse(".-") == "A"
        assert decode_from_morse("-...") == "B"
        assert decode_from_morse("-.-.") == "C"
        assert decode_from_morse("-..") == "D"
        assert decode_from_morse(".") == "E"
        assert decode_from_morse("..-.") == "F"
        assert decode_from_morse("--.") == "G"
        assert decode_from_morse("....") == "H"
        assert decode_from_morse("..") == "I"
        assert decode_from_morse(".---") == "J"
        assert decode_from_morse("-.-") == "K"
        assert decode_from_morse(".-..") == "L"
        assert decode_from_morse("--") == "M"
        assert decode_from_morse("-.") == "N"
        assert decode_from_morse("---") == "O"
        assert decode_from_morse(".--.") == "P"
        assert decode_from_morse("--.-") == "Q"
        assert decode_from_morse(".-.") == "R"
        assert decode_from_morse("...") == "S"
        assert decode_from_morse("-") == "T"
        assert decode_from_morse("..-") == "U"
        assert decode_from_morse("...-") == "V"
        assert decode_from_morse(".--") == "W"
        assert decode_from_morse("-..-") == "X"
        assert decode_from_morse("-.--") == "Y"
        assert decode_from_morse("--..") == "Z"
        assert decode_from_morse("..--.-") == "_"        
    
    def test_decode_empty_input(self):
        """Test decoding empty input raises ValueError"""
        with pytest.raises(ValueError):
            decode_from_morse("")
    
    def test_decode_invalid_input(self):
        """Test decoding invalid input raises ValueError"""
        with pytest.raises(ValueError):
            decode_from_morse(".... . .-.-..-. .-.. ---")

    @patch('sys.stdout')
    @patch('sys.argv', ['decode.py', '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'])
    def test_main_with_command_line_morse(self, mock_stdout):
        """Test main function with command line Morse code"""
        result = main()
        assert result == 0
    
    @patch('sys.stdout')
    @patch('sys.argv', ['decode.py', '--input', 'nonexistent.txt'])
    def test_main_with_nonexistent_input_file(self, mock_stdout):
        """Test main function with nonexistent input file"""
        result = main()
        assert result == 1
    
    def test_main_with_input_file(self):
        """Test main function with input file"""
        test_content = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        expected_output = "HELLO WORLD"
        
        # Create temporary input and output files
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp_in:
            tmp_in.write(test_content)
            tmp_in_path = tmp_in.name
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp_out:
            tmp_out_path = tmp_out.name
        
        try:
            # Mock sys.argv to simulate command line arguments
            with patch('sys.argv', ['decode.py', '--input', tmp_in_path, '--output', tmp_out_path]):
                result = main()
                
                assert result == 0
                
                # Check output file content
                with open(tmp_out_path, 'r') as f:
                    assert f.read() == expected_output
        
        finally:
            # Clean up
            if os.path.exists(tmp_in_path):
                os.remove(tmp_in_path)
            if os.path.exists(tmp_out_path):
                os.remove(tmp_out_path)
    
    @patch('sys.stdout')
    @patch('sys.argv', ['decode.py'])
    def test_main_with_no_input(self, mock_stdout):
        """Test main function with no input"""
        result = main()
        assert result == 0  # Should show help message and exit successfully 