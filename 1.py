import pygame, sys
def moving(): #функция непрерывного(для игрока) движения черной дыры
    screen.blit(black_hole,(x,600))
    screen.blit(black_hole,(x+432,600))

pygame.init()

x = 0
screen = pygame.display.set_mode((432,768)) #ширина и высота экрана

clock = pygame.time.Clock()

back = pygame.image.load("back.png").convert() #преобразует изобр в тип файла с которым легче работаь 

black_hole = pygame.image.load("black_hole.png").convert()

pers = pygame.image.load("pers.png").convert()
pers_rect = pers.get_rect(center = (75,384)) #помещаем персонажа в "прямоугольник"

while True: #игровой цикл
    for event in pygame.event.get(): #ищет все события которые происходят прямо сейчас(движение мыш)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(back,(0,0))
    screen.blit(pers,pers_rect)
    x -= 1 
    moving()
    if x <= -432:
        x = 0 #обнуляем x когда он дойдет до конца экрана

    pygame.display.update()
    clock.tick(120)
