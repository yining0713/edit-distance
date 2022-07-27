import unittest
from editdistance import EditDistance

TEST1a = "long live the walls we crashed through"
TEST1b = "long live the wall you crashed through"
class TestEditDistance(unittest.TestCase):

    def test_error_count(self):
        self.assertEqual(EditDistance(TEST1a, TEST1b).error_count(), 2)

if __name__ == '__main__':
    unittest.main()
