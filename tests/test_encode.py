"""
Unit tests for encode.py
"""

import os
import sys
import pytest
import tempfile
from unittest.mock import patch

# Add parent directory to path to import encode.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from encode import encode_to_morse, main

class TestEncoder:
    """Test class for Morse code encoder"""


    def test_encode_hello_world(self):
        """Test encoding hello world"""
        assert encode_to_morse("Hello World") == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    
    def test_encode_single_letter(self):
        """Test encoding a single letter"""
        assert encode_to_morse("A") == ".-"
        assert encode_to_morse("a") == ".-"  # Case insensitive
    
    def test_encode_word(self):
        """Test encoding a word"""
        assert encode_to_morse("HELLO") == ".... . .-.. .-.. ---"
        assert encode_to_morse("hello") == ".... . .-.. .-.. ---"  # Case insensitive
    
    def test_encode_sentence(self):
        """Test encoding a sentence"""
        assert encode_to_morse("HELLO WORLD") == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    
    def test_encode_with_punctuation(self):
        """Test encoding text with punctuation"""
        assert encode_to_morse("HELLO, WORLD!") == ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
    
    def test_encode_numbers(self):
        """Test encoding numbers"""
        assert encode_to_morse("123") == ".---- ..--- ...--"
    
    def test_encode_empty_input(self):
        """Test encoding empty input raises ValueError"""
        with pytest.raises(ValueError):
            encode_to_morse("")
    
    def test_encode_invalid_input(self):
        """Test encoding invalid input raises ValueError"""
        with pytest.raises(ValueError):
            encode_to_morse("Hello©World")

    @patch('sys.stdout')
    @patch('sys.argv', ['encode.py', 'HELLO'])
    def test_main_with_command_line_text(self, mock_stdout):
        """Test main function with command line text"""
        result = main()
        assert result == 0
    
    @patch('sys.stdout')
    @patch('sys.argv', ['encode.py', '--input', 'nonexistent.txt'])
    def test_main_with_nonexistent_input_file(self, mock_stdout):
        """Test main function with nonexistent input file"""
        result = main()
        assert result == 1
    
    def test_main_with_input_file(self):
        """Test main function with input file"""
        test_content = "HELLO WORLD"
        expected_output = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        
        # Create temporary input and output files
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp_in:
            tmp_in.write(test_content)
            tmp_in_path = tmp_in.name
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp_out:
            tmp_out_path = tmp_out.name
        
        try:
            # Mock sys.argv to simulate command line arguments
            with patch('sys.argv', ['encode.py', '--input', tmp_in_path, '--output', tmp_out_path]):
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
    @patch('sys.argv', ['encode.py'])
    def test_main_with_no_input(self, mock_stdout):
        """Test main function with no input"""
        result = main()
        assert result == 0  # Should show help message and exit successfully 