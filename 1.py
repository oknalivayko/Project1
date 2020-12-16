import pygame, sys
pygame.init()
screen = pygame.display.set_mode((576,1024)) #ширина и высота экрана
clock = pygame.time.Clock()
while True: #игровой цикл
    for event in pygame.event.get(): #ищет все события которые происходят прямо сейчас(движение мыш)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(120)
