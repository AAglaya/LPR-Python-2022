import pygame
from pygame.draw import circle, polygon
from random import randint


pygame.init()

FPS = 120                                                                       #Установка FPS
screen = pygame.display.set_mode((1200, 900))                                   #Создание игрового окна
clock = pygame.time.Clock()                                                     #Создание часов
font_style = pygame.font.SysFont(None, 50)                                      #Создание стилей текста для вывода
font_style_start = pygame.font.SysFont(None, 100)                               #надписей
font_style_finish = pygame.font.SysFont(None, 150)

RED = (255, 0, 0)                                                               #Установка цветов
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]                                   #Создание массива цветов


def new_ball():
    '''
    Создаёт новый шарик
    Рандомно выбирает параметры x (координата по x), y (координата по y),
    r (радиус шарика), color (цвет шарика). Отрисовывает полученный шарик.
    Возращает список параметров
    '''
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 4)]
    circle(screen, color, (x, y), r)
    parameters = [x, y, r, color]
    return parameters


def new_triangle():
    '''
    Создаёт новый треугольник
    Рандомно выбирает параметры x (координата по x), y (координата по y),
    a (длина стороны треугольник вдоль оси x и его высота), color (цвет треугольника).
    Отрисовывает полученный шарик. Возращает список параметров
    '''
    x = randint(100, 700)
    y = randint(100, 500)
    a = randint(30, 50)
    color = COLORS[randint(0, 4)]
    polygon(screen, color, [[x, y], [x + a // 2, y - a],
                            [x + a, y]])
    parameters = [x, y, a, color]
    return parameters


def ball(parameters):
    '''
    Отрисовывает шарик
    parameters - (list) список характеритик
    parameters[0] - (int) координата шарика по оси x
    parameters[1] - (int) координата шарика по оси y
    parameters[2] - (int) радиус шарика
    parameters[3] - (tuple) цвет шарика
    '''
    x = parameters[0]
    y = parameters[1]
    r = parameters[2]
    color = parameters[3]
    circle(screen, color, (x, y), r)


def triangle(parameters):
    ''''
    Отрисовывает треугольник
    parameters - (list) список характеритик
    parameters[0] - (int) координата треугольника по оси x
    parameters[1] - (int) координата треугольника по оси y
    parameters[2] - (int) радиус треугольника
    parameters[3] - (tuple) цвет треугольника
    '''
    x = parameters[0]
    y = parameters[1]
    a = parameters[2]
    color = parameters[3]
    polygon(screen, color, [[x, y], [x + a // 2, y - a],
                            [x + a, y]])


def speed():
    '''Генерирует компоненты скорости вдоль осей x и y'''
    x_speed = randint(-500, 500) / 100
    y_speed = randint(-500, 500) / 100
    return [x_speed, y_speed]


def score_message(msg, color):
    '''Выводит на экран счёт игрока'''
    mesg = font_style.render("Score: " + str(msg), True, color)
    screen.blit(mesg, [1000, 70])


def timer_message(timer, color):
    '''Выводит на экран оставшееся время игрока'''
    mesg = font_style.render("Time: " + str(timer), True, color)
    screen.blit(mesg, [1000, 120])


def win_message(color):
    '''Выводит на экран сообщение о победе'''
    mesg = font_style_finish.render("YOU WIN!", True, color)
    screen.blit(mesg, [300, 400])


def lose_message(color):
    '''Выводит на экран сообщение о проигрыше'''
    mesg = font_style_finish.render("YOU LOSE!", True, color)
    screen.blit(mesg, [300, 400])


def start_game():
    '''Отрисовывает три кнопки для выбора уровня сложности игры (easy, normal, hard)'''
    pygame.display.update()
    start_game = False                                                                      #Игра ещё не началась
    while not start_game:                                                                   #Пока игра не началась
        screen.fill(BLACK)                                                                  #Залить экран чёрны цветом
        question = font_style_start.render("Choose level", True, CYAN)                      #Сгенерировать вопрос
        level1 = font_style_start.render("Easy", True, GREEN)                               #о выборе уровня и варинты
        level2 = font_style_start.render("Normal", True, YELLOW)                            #уровней сложности
        level3 = font_style_start.render("Hard", True, RED)
        screen.blit(question, [360, 150])                                                   #Вывести вопрос
        screen.blit(level1, [500, 300])                                                     #Вывести варианты уровней
        screen.blit(level2, [460, 450])                                                     #сложности
        screen.blit(level3, [500, 600])
        pygame.display.update()                                                             #Показать изменения
                                                                                            #на экране
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:                                        #Узнать координаты мышки
                if 400 <= event.pos[0] <= 750:                                              #Если мышка попадает в
                    if 275 <= event.pos[1] <= 375:                                          #облать названия уровня,
                        level = 1                                                           #установить соответсвующую
                        start_game = True                                                   #сложность (easy - 1,
                    elif 425 <= event.pos[1] <= 525:                                        #normal - 2, hard - 3)
                        level = 2                                                           #Так же установить,что игра
                        start_game = True                                                   #началась (start_game=True)
                    elif 575 <= event.pos[1] <= 675:
                        level = 3
                        start_game = True

    return level                                                                            #Вернуть выбранную сложность


def play_game(level):
    '''
    Игра "Поймай шарик"
    level - (int) уровень сложности игры: 1 - easy, 2 - normal, 3 - hard
    '''
    finished = False                                                                        #Игра ещё не закончилась
    pygame.display.update()                                                                 #Обновить изменения на экран
    clock = pygame.time.Clock()                                                             #Установить часы
    num_of_balls = 3                                                                        #Количество шариков 3
    num_of_triangles = 3                                                                    #Количество треугольников 3
    timer = 100                                                                             #На игру даётся 100 секунд
    score = 0                                                                               #Начальный счёт 0
    if level == 1:                                                                          #В зависимости от уровня
        score_for_win = 10                                                                  #сложности выставляется
        speed_boost = 1                                                                     #количество очков для победы
    elif level == 2:                                                                        #и speed_boost фигур
        score_for_win = 50
        speed_boost = 1.5
    elif level == 3:
        score_for_win = 50
        speed_boost = 2
    parameters_balls = []                                                                   #Список шариков
    parameters_triangles = []                                                               #Список треугольников
    speed_list_balls = []                                                                   #Список скоростей шариков
    speed_list_triangles = []                                                               #Список скоростей треугльков
    for _ in range(num_of_balls):                                                           #Заполнить списки шариков и
        parameters_balls.append(new_ball())                                                 #треугольнков и их скоростей
        speed_list_balls.append(speed())
    for _ in range(num_of_triangles):
        parameters_triangles.append(new_triangle())
        speed_list_triangles.append(speed())
    while not finished:                                                                     #Пока игра не кончилась
        clock.tick(FPS)
        screen.fill(BLACK)                                                                  #Залить экран чёрным
        for num_of_ball in range(num_of_balls):                                             #Upd:координата+столконвение
            parameters_balls[num_of_ball][0] += speed_list_balls[num_of_ball][0] * speed_boost
            parameters_balls[num_of_ball][1] += speed_list_balls[num_of_ball][1] * speed_boost
            if parameters_balls[num_of_ball][0] + parameters_balls[num_of_ball][2] >= 1200 or \
                    parameters_balls[num_of_ball][0] - parameters_balls[num_of_ball][2] <= 0:
                speed_list_balls[num_of_ball][0] = -speed_list_balls[num_of_ball][0]
            if parameters_balls[num_of_ball][1] + parameters_balls[num_of_ball][2] >= 900 or \
                    parameters_balls[num_of_ball][1] - parameters_balls[num_of_ball][2] <= 0:
                speed_list_balls[num_of_ball][1] = -speed_list_balls[num_of_ball][1]
        for num_of_triangle in range(num_of_triangles):                                     #Upd:координата+столконвение
            parameters_triangles[num_of_triangle][0] += speed_list_triangles[num_of_triangle][0] * speed_boost
            parameters_triangles[num_of_triangle][1] += speed_list_triangles[num_of_triangle][1] * speed_boost
            if parameters_triangles[num_of_triangle][0] + parameters_triangles[num_of_triangle][2] >= 1200 or \
                    parameters_triangles[num_of_triangle][0] <= 0:
                speed_list_triangles[num_of_triangle][0] = -speed_list_triangles[num_of_triangle][0]
            if parameters_triangles[num_of_triangle][1] >= 900 or \
                    parameters_triangles[num_of_triangle][1] - parameters_triangles[num_of_triangle][2] <= 0:
                speed_list_triangles[num_of_triangle][1] = -speed_list_triangles[num_of_triangle][1]
        for num_of_ball in range(len(parameters_balls)):                                   #Отрисовать фигуры с новыми
            ball(parameters_balls[num_of_ball])                                            #координатами
        for num_of_triangle in range(len(parameters_triangles)):
            triangle(parameters_triangles[num_of_triangle])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:                                     #Проверить, попал ли игрок в
                for num_of_ball, position in enumerate(parameters_balls):                  #шарик
                    if (event.pos[0] - position[0]) ** 2 + (event.pos[1] - position[1]) ** 2 <= position[2] ** 2:
                        score += 1                                                         #Если да,добавить очки и
                        parameters_balls[num_of_ball] = new_ball()                         #создать новый шарик
                        speed_list_balls[num_of_ball] = speed()
                for num_of_triangle, position in enumerate(parameters_triangles):
                    x0, y0 = event.pos[0], event.pos[1]
                    x1, y1 = position[0], position[1]
                    x2, y2 = position[0] + position[2] // 2, position[1] - position[2]
                    x3, y3 = position[0] + position[2], position[1]
                    a = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
                    b = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
                    c = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
                    if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):   #Проверить, попал ли игрок в
                        score += 4                                                         #треугольник. Если да,
                        parameters_triangles[num_of_triangle] = new_triangle()             #добавить очки, создать новый
                        speed_list_triangles[num_of_triangle] = speed()                    #треугольник
        timer -= 1 / 120                                                                   #уменьшить таймер
        score_message(str(score), MAGENTA)                                                 #вывести счет
        timer_message(str(int(timer)), MAGENTA)                                            #выести оставшееся время
        pygame.display.update()                                                            #вывести изменения на экран
        if score >= score_for_win and timer >= 0:                                          #если набрал нужное кол-во
            win_message(RED)                                                               #очков для победы до конца
            finished = True                                                                #времени, вывести сообщение
        elif timer < 0:                                                                    #о победе и закончить игру
            lose_message(RED)                                                              #если нет, то о поражении
            finished = True
        pygame.display.update()                                                            #вывести изменения на экран
    pygame.time.wait(850)                                                                  #задержка 850 ms
    pygame.quit()                                                                          #выйти из игры


level = start_game()
play_game(level)