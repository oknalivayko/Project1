import pygame, sys, random 

def init_and_check_for_errors():
    """Функция для инициализации и
    проверки как запустится pygame"""
    check_errors = pygame.init()
    if check_errors[1] > 0:
        sys.exit()
    else:
        print('ok')

def moving(): 
    """Функция непрерывного (для игрока) движения нижней
    поверхности (пола). Не принимает аргументов"""
    screen.blit(floor,(x,700)) #blict берет фоновую поверхность и рисует ее на экране и размещает в точке (x, y)
    screen.blit(floor,(x+432,700)) #рисует такую же картинку рядом

def star_moving():
    """Функция которая рисует на экран звезды(рябь). Не принимает аргументов """
    randomstarx = random.choice(starx)
    randomstary = random.choice(stary)
    screen.blit(star,(randomstarx,randomstary))

def create_asteroid():
    """Функция для создания объектов столкновения (кометы). Создает
    объекты в любом месте на экране, возвращает комету"""
    random_asteroid_pos = random.choice(asteroid_heiht) #случайно определяет позицию y из созданного списка
    new_asteroid = asteroid_draw.get_rect(center=(700,random_asteroid_pos)) #позиция x=700 чтобы игрок не видел как астероид резко появляется на глазах
    return new_asteroid


def move_asteroids(asteroids):
    """ Функция для перемещения комет. Функция принимает список 
    комет, затем перебирает каждый объект, перемещая на 
    некоторое расстояние влево, возвращает новый список комет"""
    for asteroid in asteroids:
        asteroid.centerx -= 5 
    return(asteroids)

def draw_asteroids(asteroids):
    """Функция для отображения комет на экране. 
    Принимает список комет."""
    for asteroid in asteroids:
        p = pygame.transform.rotozoom(asteroid_draw,-angle*3,1)
        screen.blit(p,asteroid)

def crash(asteroids): 
    """Функция для столкновения с астероидами и границами игры, 
    принимает список комет, возвращает ДА или НЕТ"""
    for asteroid in asteroids:
        if pers_rect.colliderect(asteroid):   #если есть столкновение с астероидом
            death_sound.play()
            return False
    if pers_rect.top<=-100 or pers_rect.bottom>=700: #если игрок вылетел за пределы экрана
        death_sound.play()
        return False
    return True

def dis_score (game_pos): 
    """Функция для отображения счета на экране. Функция принимает 
    "позицию" игры. Если игра в активной позиции, то функция
    отображает счетчик. Если игра окончена, то отображает 
    полученный счет и лучший счет"""
    if game_pos == 'main_game': 
        score_surface = game_font.render(str(int(score)),True,(166, 13, 20)) #выбор цвета
        score_rect = score_surface.get_rect(center = (210,150))
        screen.blit(score_surface,score_rect)
    if game_pos == 'game_over':
        score_surface = game_font.render('Score: ' + str(int(score)),True,(166, 13, 20)) #выбор цвета
        score_rect = score_surface.get_rect(center = (210,150))
        screen.blit(score_surface,score_rect)

        best_score_surface = game_font.render('Best score: ' + str(int(best_score)),True,(166, 13, 20)) #выбор цвета
        best_score_rect = best_score_surface.get_rect(center = (210,600))
        screen.blit(best_score_surface,best_score_rect)

def score_update(score, best_score):
    """Функция для определения лучшего счета. Принимает счет,
    лучший счет, сравнивает их и возвращает лучший счет"""
    if score > best_score:
        best_score = score
    return best_score

def pers_rotate(personage):
    """Функция для вращения объекта. Принимает объект 
    персонажа, возвращает вращающегося персонажа""" 
    p = pygame.transform.rotozoom(personage,pers_movement*3,1)
    return p

def pers_animation():
    """Функция для создания анимации персонажа"""
    new_pers = pers_massive[pers_index]
    new_pers_rect = new_pers.get_rect(center = (75,pers_rect.centery)) #мы берем позицию y прошлого прямоугольника чтобы не менять положение когда мы обновляем прямоугольник
    return new_pers, new_pers_rect

init_and_check_for_errors()
pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 1, buffer = 256)
pygame.init() 

angle = 0 #счетчик для вращения комет
x = 0 # позиция для пола
gravity = 0.125 #создаем гравитацию
pers_movement = 0 #движение персонажа
game = False #создаем переменную отвечающую за процесс игры, если она положительна - игра идет, если нет - конец игры
score = 0 #счет
best_score = 0 #лучший счет
screen = pygame.display.set_mode((432,768)) #Cоздание поверхности изображения, принимает длину и ширину экрана
clock = pygame.time.Clock() #Создание объекта для отслеживания игрового времени
game_font = pygame.font.Font('MarkerFelt-Thin.ttf',50) #Создание нового объекта Font (шрифт) из файла. Принимает имя файла, размер шрифта
back = pygame.image.load("back.png").convert() #Загружает изображение из файла. Принимает имя файла или файловый объект python
floor = pygame.image.load("floor.png").convert()
pers_fire = pygame.image.load('pers_fire.png').convert_alpha()
pers_n_fire = pygame.image.load('pers.png').convert_alpha()
pers_massive = [pers_fire,pers_n_fire] #создаем массив из двух элементов - положений персонажа
pers_index = 0 # индекс для массива, который будет принимать значение 0 или 1
pers = pers_massive[pers_index] 
pers_rect = pers.get_rect(center = (75,384))
tutorial = pygame.image.load('gameover.png').convert_alpha()
tutorial = pygame.transform.scale2x(tutorial)
tutorial_rect = tutorial.get_rect(center = (216,284))
asteroid_draw = pygame.image.load("asteroid.png").convert_alpha()
asteroid_list = []

spawn = pygame.USEREVENT
pygame.time.set_timer(spawn,1500) #обновляем событие по времени каждую секунду
asteroid_heiht = [100,200,400]

score_sound = pygame.mixer.Sound('score.wav')
theme_sound = pygame.mixer.Sound('theme.wav')
death_sound = pygame.mixer.Sound('death.wav')
score_sound_x = 200

asteroid_draw = pygame.image.load("asteroid.png").convert_alpha()
asteroid_list = [] #создаем список в который мы будем добавлять "прямоугольники" с астероидами
spawn = pygame.USEREVENT #создаем событие, которое будет вызываться по таймеру
pygame.time.set_timer(spawn,1500) #обновляем событие по времени каждые 1500 мс
asteroid_heiht = [100,200,400] #список с высотой на которой будут создаваться астероиды
star = pygame.image.load('star.png').convert_alpha()
starx = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750]
stary = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750]

if __name__ == '__main__':
    while True: #Игровой цикл
        for event in pygame.event.get(): #Поиск событий которые происходят прямо сейчас (движение мышью)
            if event.type == pygame.QUIT: #выход из игры
                pygame.quit()
                sys.exit() #говорит интерпретатору остановить выполнение программы
            
            if event.type == pygame.KEYDOWN: #проверяет была ли нажата кнопка на клавиатуре
                if event.key == pygame.K_UP:
                    pers_fire_1 = pygame.image.load('pers_fire_y.png').convert_alpha()
                    pers_n_fire_1 = pygame.image.load('yellow.png').convert_alpha()
                    pers_massive = [pers_fire_1,pers_n_fire_1]

                if event.key == pygame.K_DOWN:
                    pers_fire_1 = pygame.image.load('orange1.png').convert_alpha()
                    pers_n_fire_1 = pygame.image.load('orange.png').convert_alpha()
                    pers_massive = [pers_fire_1,pers_n_fire_1]

                if event.key == pygame.K_RIGHT:
                    pers_fire = pygame.image.load('pers_fire.png').convert_alpha()
                    pers_n_fire = pygame.image.load('pers.png').convert_alpha()
                    pers_massive = [pers_fire,pers_n_fire]

                if event.key == pygame.K_LEFT:
                    pers_fire_1 = pygame.image.load('white1.png').convert_alpha()
                    pers_n_fire_1 = pygame.image.load('white.png').convert_alpha()
                    pers_massive = [pers_fire_1,pers_n_fire_1]

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
                    asteroid_list.clear() #очищаем весь список астероидов
                    pers_movement = 0 #возвращаем 0 движению персонажа
                    pers_rect.center = (75,384) #и возвращаем в исходную позицию
                    score = 0
            if event.type == spawn:
                asteroid_list.append(create_asteroid()) #добавляем в список кометы с помощью функции


        screen.blit(back,(0,0))
        
        if game: #если игра идет то создаем персонажа и препяствия
            angle+=1
            pers_movement += gravity
            pers_rect.centery += pers_movement #перемещаем центр "прямоугольника" вместе с персом по оси y 
            pers_rotated = pers_rotate(pers)
            screen.blit(pers_rotated,pers_rect) 
            game = crash(asteroid_list)
            asteroid_list = move_asteroids(asteroid_list)
            draw_asteroids(asteroid_list)
            score += 0.005
            score_sound_x -= 1
            if score_sound_x <= 0:
                score_sound.play()
                score_sound_x = 200
            dis_score('main_game')
            star_moving() 
        else:
            best_score = score_update(score, best_score)
            score_sound_x = 200
            dis_score('game_over')
            screen.blit(tutorial,tutorial_rect)   
        x -= 1
        moving()
        if x <= -432:
            x = 0 #обнуляем x когда он дойдет до конца экрана

        pygame.display.update() #Обновление части экрана. В данном случае обновляет весь дисплей,т.к не передаем никакие аргументы
        clock.tick(120) #Принимает количество кадров в секунду, т.е как быстро будет выполнять цикл
