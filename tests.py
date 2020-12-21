import unittest,pygame
from main import score_update
from main import move_asteroids
from main import crash
class Test_Among (unittest.TestCase):

    def test_1(self):
        self.assertEqual (score_update(2,3), (3))
        self.assertEqual (score_update(4,3), (4))
        self.assertEqual (score_update(6,5), (6))
        self.assertEqual (score_update(4456,3), (4456))
        self.assertEqual (score_update(78,56), (78))

    def test_2(self):
        asteroid_draw = pygame.image.load("asteroid.png").convert_alpha()
        asteroid_list = []
        asteroid_list.append(asteroid_draw.get_rect(center=(700,500)))
        self.assertEqual (move_asteroids(asteroid_list),[asteroid_draw.get_rect(center=(695,500))])
        asteroid_list = [asteroid_draw.get_rect(center=(700,500)),asteroid_draw.get_rect(center=(695,500))]
        self.assertEqual (move_asteroids(asteroid_list), [asteroid_draw.get_rect(center=(695,500)),asteroid_draw.get_rect(center=(690,500))])
        asteroid_list = []
        self.assertEqual (move_asteroids(asteroid_list),[])
        asteroid_list = [asteroid_draw.get_rect(center=(0,0)),asteroid_draw.get_rect(center=(3,100))]
        self.assertEqual (move_asteroids(asteroid_list), [asteroid_draw.get_rect(center=(-5,0)),asteroid_draw.get_rect(center=(-2,100))])

    #def test_3(self):
        #asteroid_draw = pygame.image.load("asteroid.png").convert_alpha()
        #asteroid_list = []
        


