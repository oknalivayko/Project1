import pygame
pygame.init()
screen = pygame.display.set_mode((576,1024)) #ширина и высота экрана
while True: #игровой цикл
    for event in pygame.event.get(): #ищет все события которые происходят прямо сейчас(движение мыш)
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
