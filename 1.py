import pygame, sys
def 
pygame.init()
screen = pygame.display.set_mode((432,768)) #ширина и высота экрана
clock = pygame.time.Clock()
back = pygame.image.load("back.png").convert() #преобразует изобр в тип файла с которым легче работаь 
black_hole = pygame.image.load("black_hole.png").convert()
while True: #игровой цикл
    for event in pygame.event.get(): #ищет все события которые происходят прямо сейчас(движение мыш)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(back,(0,0))
    screen.blit(black_hole,(0,600))
    pygame.display.update()
    clock.tick(120)
