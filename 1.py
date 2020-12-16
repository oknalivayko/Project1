import pygame, sys
def moving(): #функция непрерывного(для игрока) движения черной дыры
    screen.blit(black_hole,(x,700))
    screen.blit(black_hole,(x+432,700))

pygame.init()

x = 0
gravity = 0.125 #создаем гравитацию
pers_movement = 0 #движение персонажа


screen = pygame.display.set_mode((432,768)) #ширина и высота экрана

clock = pygame.time.Clock()

back = pygame.image.load("back.png").convert() #преобразует изобр в тип файла с которым легче работаь 

black_hole = pygame.image.load("black_hole.png").convert()

pers = pygame.image.load("pers.png").convert()
pers_rect = pers.get_rect(center = (75,384)) #помещаем персонажа в "прямоугольник" и располагаем в центре экрана

while True: #игровой цикл
    for event in pygame.event.get(): #ищет все события которые происходят прямо сейчас(движение мыш)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #проверяет была ли нажата кнопка на клавиатуре
            if event.key == pygame.K_SPACE: #если нажали кнопку W
                pers_movement = 0
                pers_movement -= 5

    screen.blit(back,(0,0))
    
    pers_movement += gravity
    pers_rect.centery += pers_movement #перемещаем центр "прямоугольника" вместе с персом
    screen.blit(pers,pers_rect)
    x -= 1 
    moving()
    if x <= -432:
        x = 0 #обнуляем x когда он дойдет до конца экрана

    pygame.display.update()
    clock.tick(120)
