import unittest
from editdistance import EditDistance

TEST1a = "long live the walls we crashed through"
TEST1b = "long live the wall you crashed through"
TEST2a = "30rock"
TEST2b = "41rock"
TEST3a = "片面心动在爱情里都显得有恃无恐"
TEST3b = "片面心动在情爱里都显的有恃无恐"
TEST4a = "你 礼貌 的 晚安，我 听 成 了 海浪。"
TEST4b = "你 礼貌的 晚安 我 听 成 了 海浪"

class TestEditDistance(unittest.TestCase):

    def test_error_count(self):
        self.assertEqual(EditDistance(TEST1a, TEST1b).error_count(), 2)
        self.assertEqual(EditDistance(TEST1a, TEST1b, "word").error_count(), 2)
        self.assertEqual(EditDistance(TEST1a, TEST1b, "char").error_count(), 4)
        self.assertEqual(EditDistance(TEST2a, TEST2b).error_count(), 1)
        self.assertEqual(EditDistance(TEST2a, TEST2b, "char").error_count(), 2)
        self.assertEqual(EditDistance(TEST3a, TEST3b, "char").error_count(), 3)
        self.assertEqual(EditDistance(TEST4a, TEST4b, "word").error_count(), 4)

if __name__ == '__main__':
    unittest.main()
