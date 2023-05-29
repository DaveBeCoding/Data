import unittest
from unittest.mock import patch
import io
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from wordmatrix import parse_pdf, display_character_matrix, display_word_matrix, save_word_matrix_report


class TestPDFParsing(unittest.TestCase):

    def test_parse_pdf(self):
        expected_character_count = 2345
        expected_word_count = 123
        expected_character_matrix = [100, 200, 300]
        expected_word_matrix = [["word1", "word2"], ["word3"], ["word4", "word5", "word6"]]

        with patch('builtins.open'), patch('PyPDF2.PdfReader') as mock_pdf_reader:
            mock_pdf_reader.return_value.pages.__getitem__.return_value.extract_text.return_value = "Sample text"

            character_count, word_count, character_matrix, word_matrix = parse_pdf("sample.pdf")

            self.assertEqual(character_count, expected_character_count)
            self.assertEqual(word_count, expected_word_count)
            self.assertEqual(character_matrix, expected_character_matrix)
            self.assertEqual(word_matrix, expected_word_matrix)

    def test_display_character_matrix(self):
        expected_output = "Page 1: 100 characters\nPage 2: 200 characters\nPage 3: 300 characters\n"

        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            display_character_matrix([100, 200, 300])
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_word_matrix(self):
        expected_output = "Page 1:\nword1: 1\tword2: 1\t\nPage 2:\nword3: 1\t\nPage 3:\nword4: 1\tword5: 1\tword6: 1\t\n"

        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            display_word_matrix([["word1", "word2"], ["word3"], ["word4", "word5", "word6"]])
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_save_word_matrix_report(self):
        expected_output = "Page 1:\nword1: 1\tword2: 1\t\nPage 2:\nword3: 1\t\nPage 3:\nword4: 1\tword5: 1\tword6: 1\t\n"

        with patch('builtins.open', create=True) as mock_file:
            save_word_matrix_report([["word1", "word2"], ["word3"], ["word4", "word5", "word6"]], "report.txt")

            mock_file.return_value.__enter__.return_value.write.assert_called_once_with(expected_output)


if __name__ == '__main__':
    unittest.main()

