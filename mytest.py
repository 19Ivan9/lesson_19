import sys
import os.path
from tack2 import*
import unittest
from unittest.mock import patch
from tack3 import*

class TestTack2(unittest.TestCase):
    def test_add(self):
        start_len = len(sys.path)
        sys_path_adder()
        self.assertTrue(len(sys.path)>start_len)

    def test_search(self):
        self.assertIn('E:/Users/Vanshi/Desktop',sys.path,'Dont have!')

    # def test_del(self):
    #     sys_path_deleter()
    #     self.assertFalse('E:/Users/Vanshi/Desktop' in sys.path,'Err delete!')

class TestTack3(unittest.TestCase):
    @patch('tack3.input',return_value='L')
    def test_answer_lines(self,input):
        self.assertEqual(test(file),print(count_lines(file)))

    @patch('tack3.input', return_value='S')
    def test_answer_symbols(self, input):
        self.assertEqual(test(file), print(count_chars(file)))

    @patch('tack3.input', return_value='A')
    def test_answer_all(self, input):
        self.assertEqual(test(file), print(count_lines(file),count_chars(file)))

    def test_my_file_txt(self):
        # os.path.isfile(file)
        try:
            f = open(file)
            f.close()
        except FileNotFoundError:
            print('File not found!')
if __name__ == '__main__':
    unittest.main()