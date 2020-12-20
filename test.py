import unittest
from main import score_update

class Test_game(unittest.TestCase):

    def test_1(self):
        self.assertEqual(score_update(3,2),3)

if __name__ == '__main__':
    unittest.main()