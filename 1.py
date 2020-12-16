import pygame, sys, random
def moving(): #функция непрерывного(для игрока) движения черной дыры
    screen.blit(black_hole,(x,700))
    screen.blit(black_hole,(x+432,700))

def create_asteroid():
    random_asteroid_position = random.choice(asteroid_height)
    new_asteroid_down = asteroid_s.get_rect(midtop = (700,random_asteroid_position))
    new_asteroid_top = asteroid_s.get_rect(midbottom = (700,random_asteroid_position-300))
    return new_asteroid_down, new_asteroid_top

def move_asteroids(asteroids):
    for asteroid in asteroids:
        asteroid.centerx -= 5
    return asteroids

def draw_asteroids(asteroids):
    for asteroid in asteroids:
        screen.blit(asteroid_s,asteroid) 

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

asteroid_s = pygame.image.load("asteroid.png")
asteroid_list = []
spawn = pygame.USEREVENT
pygame.time.set_timer(spawn,1200)
asteroid_height = [1500,200,300]
while True: #игровой цикл
    for event in pygame.event.get(): #ищет все события которые происходят прямо сейчас(движение мыш)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #проверяет была ли нажата кнопка на клавиатуре
            if event.key == pygame.K_SPACE: #если нажали кнопку W
                pers_movement = 0
                pers_movement -= 5
        if event.type == spawn:
            asteroid_list.extend(create_asteroid())

    screen.blit(back,(0,0))
    
    pers_movement += gravity
    pers_rect.centery += pers_movement #перемещаем центр "прямоугольника" вместе с персом
    screen.blit(pers,pers_rect)

    asteroid_list = move_asteroids(asteroid_list)
    draw_asteroids(asteroid_list)


    x -= 1 
    moving()
    if x <= -432:
        x = 0 #обнуляем x когда он дойдет до конца экрана

    pygame.display.update()
    clock.tick(120)
