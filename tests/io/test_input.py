import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from app.io.input import read_from_file, read_from_file_with_pandas
from io import StringIO

class TestFileReadingFunctions(unittest.TestCase):
    
    def test_read_from_file_success(self):
        mock_data = "line1\nline2\nline3\n"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = read_from_file("fake_path.txt")
            self.assertEqual(result, ["line1\n", "line2\n", "line3\n"])
    
    def test_read_from_file_empty(self):
        with patch("builtins.open", mock_open(read_data="")):
            result = read_from_file("fake_path.txt")
            self.assertEqual(result, [])
    
    def test_read_from_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file("non_existent_file.txt")

if __name__ == '__main__':
    unittest.main()

    