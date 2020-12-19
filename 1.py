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
        p = pygame.transform.rotozoom(comet_draw,-angle*3,1)
        screen.blit(p,comet)

def crash(comets): #функция столкновения с астероидами и границами игры, возвращает ДА или НЕТ
    for comet in comets:
        if pers_rect.colliderect(comet):
            return False
    if pers_rect.top<=-100 or pers_rect.bottom>=700:
        return False
    return True

def dis_score (game_pos): #вызовает отображение счета на экране
    if game_pos == 'main_game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255)) #выбор цвета
        score_rect = score_surface.get_rect(center = (210,150))
        screen.blit(score_surface,score_rect)
    if game_pos == 'game_over':
        score_surface = game_font.render('Score: ' + str(int(score)),True,(255,255,255)) #выбор цвета
        score_rect = score_surface.get_rect(center = (210,150))
        screen.blit(score_surface,score_rect)

        best_score_surface = game_font.render('Best score: ' + str(int(best_score)),True,(255,255,255)) #выбор цвета
        best_score_rect = best_score_surface.get_rect(center = (210,600))
        screen.blit(best_score_surface,best_score_rect)

def score_update(score, best_score):
    if score > best_score:
        best_score = score
    return best_score

def pers_rotate(personage):
    p = pygame.transform.rotozoom(personage,pers_movement*3,1)
    return p

def pers_animation():
    new_pers = pers_massive[pers_index]
    new_pers_rect = new_pers.get_rect(center = (75,pers_rect.centery))
    return new_pers, new_pers_rect
pygame.init()

angle = 0
x = 0
gravity = 0.125 #создаем гравитацию
pers_movement = 0 #движение персонажа
game = True #создаем переменную отвечающую за процесс игры, если она положительна - игра идет, если нет - конец игры
score = 0 #счет
best_score = 0 #лучший счет

screen = pygame.display.set_mode((432,768)) #ширина и высота экрана
clock = pygame.time.Clock()
game_font = pygame.font.Font('MarkerFelt-Thin.ttf',50) #шрифт
back = pygame.image.load("back.png").convert() #преобразует изобр в тип файла с которым легче работаь 
black_hole = pygame.image.load("black_hole.png").convert()

pers_fire = pygame.image.load('pers_fire.png').convert_alpha()
pers_n_fire = pygame.image.load('pers.png').convert_alpha()
pers_massive = [pers_fire,pers_n_fire]
pers_index = 0
pers = pers_massive[pers_index]
pers_rect = pers.get_rect(center = (75,384))

#pers = pygame.image.load("pers.png").convert_alpha()
#pers_rect = pers.get_rect(center = (75,384)) #помещаем персонажа в "прямоугольник" и располагаем в центре экрана


tutorial = pygame.image.load('gameover.png').convert_alpha()
tutorial = pygame.transform.scale2x(tutorial)
tutorial_rect = tutorial.get_rect(center = (216,284))
comet_draw = pygame.image.load("comet.png").convert_alpha()
comet_list = []

spawn = pygame.USEREVENT
pygame.time.set_timer(spawn,1500) #обновляем событие по времени каждую секунду
comet_heiht = [100,200,400]


while True: #игровой цикл
    for event in pygame.event.get(): #ищет все события которые происходят прямо сейчас(движение мыш)
        if event.type == pygame.QUIT: #выход из игры
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #проверяет была ли нажата кнопка на клавиатуре
            if event.key == pygame.K_SPACE and game == True: #если нажали кнопку space вначале игры
                pers_movement = 0
                pers_movement -= 5
                if pers_index == 0:
                    pers_index = 1
                else:
                    pers_index = 0
                pers,pers_rect = pers_animation()
            if event.key == pygame.K_SPACE and game == False: #если нажали пробел когда проиграли
                game = True #игра начинается заново
                comet_list.clear() #очищаем весь список астероидов
                pers_movement = 0 #возвращаем 0 движению персонажа
                pers_rect.center = (75,384) #и возвращаем в исходную позицию
                score = 0
        if event.type == spawn:
            comet_list.append(create_comet())
    
           
    screen.blit(back,(0,0))
    
    if game: #если игра идет то создаем персонажа и препяствия
        angle+=1
        pers_movement += gravity
        pers_rect.centery += pers_movement #перемещаем центр "прямоугольника" вместе с персом
        pers_rotated = pers_rotate(pers)
        screen.blit(pers_rotated,pers_rect)
        game = crash(comet_list)

        comet_list = move_comets(comet_list)
        draw_comets(comet_list)
        
        score += 0.005
        dis_score('main_game')
    else:
        best_score = score_update(score, best_score)
        dis_score('game_over')
        screen.blit(tutorial,tutorial_rect)
        crash(comet_list)
    x -= 1 
    moving()
    if x <= -432:
        x = 0 #обнуляем x когда он дойдет до конца экрана

    pygame.display.update()
    clock.tick(120)
