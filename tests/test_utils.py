"""
Unit tests for morse_utils.py
"""

import os
import pytest
import tempfile
from morse_utils import (
    CHAR_TO_MORSE, 
    MORSE_TO_CHAR, 
    validate_english_text, 
    validate_morse_code,
    read_from_file,
    write_to_file
)

class TestMorseUtils:
    """Test class for Morse utility functions"""
    
    def test_char_to_morse_mapping(self):
        """Test character to Morse code mapping"""
        assert CHAR_TO_MORSE['A'] == '.-'
        assert CHAR_TO_MORSE['Z'] == '--..'
        assert CHAR_TO_MORSE['0'] == '-----'
        assert CHAR_TO_MORSE['9'] == '----.'
        assert CHAR_TO_MORSE['.'] == '.-.-.-'
    
    def test_morse_to_char_mapping(self):
        """Test Morse code to character mapping"""
        assert MORSE_TO_CHAR['.-'] == 'A'
        assert MORSE_TO_CHAR['--..'] == 'Z'
        assert MORSE_TO_CHAR['-----'] == '0'
        assert MORSE_TO_CHAR['----.'] == '9'
        assert MORSE_TO_CHAR['.-.-.-'] == '.'
    
    def test_validate_english_text_valid(self):
        """Test validation of valid English text"""
        valid, _ = validate_english_text("Hello World")
        assert valid is True
        
        valid, _ = validate_english_text("HELLO 123")
        assert valid is True
        
        valid, _ = validate_english_text("Hello, World!")
        assert valid is True
    
    def test_validate_english_text_invalid(self):
        """Test validation of invalid English text"""
        valid, error_msg = validate_english_text("")
        assert valid is False
        assert "empty" in error_msg.lower()
        
        valid, error_msg = validate_english_text("Hello©World")
        assert valid is False
        assert "©" in error_msg
    
    def test_validate_morse_code_valid(self):
        """Test validation of valid Morse code"""
        valid, _ = validate_morse_code(".... . .-.. .-.. ---")
        assert valid is True
        
        valid, _ = validate_morse_code(".... .   .-- --- .-. .-.. -..")
        assert valid is True
    
    def test_validate_morse_code_invalid(self):
        """Test validation of invalid Morse code"""
        valid, error_msg = validate_morse_code("")
        assert valid is False
        assert "empty" in error_msg.lower()
        
        valid, error_msg = validate_morse_code(".... . .-.-..-. .-.. ---")
        assert valid is False
        assert ".-.-..-." in error_msg
    
    def test_file_operations(self):
        """Test file read and write operations"""
        test_content = "Hello, World!"
        
        # Create a temporary file for testing
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name
            
        try:
            # Test writing to file
            write_to_file(tmp_path, test_content)
            
            # Test reading from file
            content = read_from_file(tmp_path)
            assert content == test_content
            
        finally:
            # Clean up
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
    
    def test_file_not_found(self):
        """Test handling of non-existent files"""
        with pytest.raises(FileNotFoundError):
            read_from_file("nonexistent_file.txt") 