import unittest
from ls import *


class TestLs(unittest.TestCase):
    def test_basic(self):
        path = 'Test'
        l_flag = False
        normal_output = 'another_file.txt\nsome_file.txt\nsome_other_file.txt\n'
        self.assertEqual(listFiles(path, l_flag), normal_output)

    def test_basic_l_flag(self):
        path = 'Test'
        l_flag = True
        normal_output = '-rw-rw-rw- 2017-12-21 21:30 another_file.txt\n-rw-rw-rw- 2017-12-21 21:31 some_file.txt\n-rw-rw-rw- 2017-12-21 21:31 some_other_file.txt\n'
        self.assertEqual(listFiles(path, l_flag), normal_output)

    def test_space_in_dir_name(self):
        path = 'Test Space'
        l_flag = True
        normal_output = '-rw-rw-rw- 2017-12-21 21:38 just_a_file.txt\n'
        self.assertEqual(listFiles(path, l_flag), normal_output)

    def test_prefix(self):
        path = 'Test/so'
        l_flag = True
        normal_output = '-rw-rw-rw- 2017-12-21 21:31 some_file.txt\n-rw-rw-rw- 2017-12-21 21:31 some_other_file.txt\n'
        self.assertEqual(listFiles(path, l_flag), normal_output)

    def test_not_a_directory(self):
        path = 'Test2/'
        l_flag = False
        normal_output = 'The specified folder can not be found.'
        self.assertEqual(listFiles(path, l_flag), normal_output)

    def test_prefix_of_no_files(self):
        path = 'Test/si'
        l_flag = False
        normal_output = 'None of the file names in the folder contain \'si\' as a prefix.'
        self.assertEqual(listFiles(path, l_flag), normal_output)


if __name__ == '__main__':
    unittest.main()
