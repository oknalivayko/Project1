import pygame, sys, random
def moving(): #функция непрерывного(для игрока) движения черной дыры
    screen.blit(black_hole,(x,700))
    screen.blit(black_hole,(x+432,700))
def create_comet():
    random_comet_pos = random.choice(comet_heiht)
    new_comet = comet_draw.get_rect(center=(700,random_comet_pos))
    return new_comet
def move_comets(comets):
    for comet in comets:
        comet.centerx -= 5 
    return(comets)
def draw_comets(comets):
    for comet in comets:
        screen.blit(comet_draw,comet)
def crash(comets):
    for comet in comets:
        if pers_rect.colliderect(comet):
            return False
    if pers_rect.top<=-100 or pers_rect.bottom>=700:
        return False
    return True

pygame.init()

x = 0
gravity = 0.125 #создаем гравитацию
pers_movement = 0 #движение персонажа
game = True

screen = pygame.display.set_mode((432,768)) #ширина и высота экрана

clock = pygame.time.Clock()

back = pygame.image.load("back.png").convert() #преобразует изобр в тип файла с которым легче работаь 
black_hole = pygame.image.load("black_hole.png").convert()

pers = pygame.image.load("pers.png").convert()
pers_rect = pers.get_rect(center = (75,384)) #помещаем персонажа в "прямоугольник" и располагаем в центре экрана
comet_draw = pygame.image.load("comet.png").convert()
comet_list = []
spawn = pygame.USEREVENT
pygame.time.set_timer(spawn,1200)
comet_heiht = [100,200,400]

while True: #игровой цикл
    for event in pygame.event.get(): #ищет все события которые происходят прямо сейчас(движение мыш)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #проверяет была ли нажата кнопка на клавиатуре
            if event.key == pygame.K_SPACE and game == True: #если нажали кнопку space
                pers_movement = 0
                pers_movement -= 5
            if event.key == pygame.K_SPACE and game == False:
                game = True
                comet_list.clear()
                pers_movement = 0
                pers_rect.center = (75,384)
        if event.type == pygame.USEREVENT:
            comet_list.append(create_comet())
            
        

    screen.blit(back,(0,0))
    
    if game:
        pers_movement += gravity
        pers_rect.centery += pers_movement #перемещаем центр "прямоугольника" вместе с персом
        screen.blit(pers,pers_rect)
        game = crash(comet_list)

        comet_list = move_comets(comet_list)
        draw_comets(comet_list)

        crash(comet_list)
    x -= 1 
    moving()
    if x <= -432:
        x = 0 #обнуляем x когда он дойдет до конца экрана

    pygame.display.update()
    clock.tick(120)
