import unittest
from rDuplicate import remove_duplicate, merge_and_remove_duplicate, get_diffrence, read_csv, write_csv

class TestCSVFunctions(unittest.TestCase):
    def test_remove_duplicate(self):
        input_path = 'test_data/test_data1.csv'
        input_data = read_csv(input_path)
        expected_output = [ ['duplicatedLine', 'rwerwe', 'werwrw', 'werwerwer', 'rwerw'],
                            ['title changed only', 'rwerwe', 'werwrw', 'werwerwer', 'rwerw']
                        ]
        self.assertEqual(remove_duplicate(input_data, 0), expected_output)

    def test_merge_and_remove_duplicate(self):
        input_path1 = 'test_data/test_data1.csv'
        input_data1 = read_csv(input_path1)
        input_path2 = 'test_data/test_data2.csv'
        input_data2 = read_csv(input_path2)

        expected_output = [
            ['duplicatedLine', 'rwerwe', 'werwrw', 'werwerwer', 'rwerw'],
            ['title changed only', 'rwerwe', 'werwrw', 'werwerwer', 'rwerw'],
            ['line exist only in this file', 'should be there', 'fdfssdf']
        ]
        self.assertEqual(merge_and_remove_duplicate(input_data1, input_data2, 0), expected_output)


    def test_get_diffrence(self):
        input_path1 = 'test_data/test_data1.csv'
        input_data1 = read_csv(input_path1)
        input_path2 = 'test_data/test_data2.csv'
        input_data2 = read_csv(input_path2)

        expected_output = [
            ['line exist only in this file', 'should be there', 'fdfssdf']
        ]
        
        self.assertEqual(get_diffrence(input_data1, input_data2, 0), expected_output)



if __name__ == '__main__':
    unittest.main()