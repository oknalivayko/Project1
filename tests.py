import unittest,pygame
from main import score_update
from main import move_asteroids
class Test_Among (unittest.TestCase):

    def test_1(self):
        self.assertEqual (score_update(2,3), 3)
        
