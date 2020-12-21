import unittest
from main import score_update
class Test_Among (unittest.TestCase):

    def test_1(self):
        self.assertEqual (score_update(2,3), 7)
