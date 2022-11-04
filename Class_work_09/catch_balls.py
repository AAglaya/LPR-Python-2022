import pygame
from pygame.draw import circle, polygon
from random import randint


pygame.init()

FPS = 120
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
font_style_finish = pygame.font.SysFont(None, 150)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    parameters = [x, y, r, color]
    return parameters


def new_triangle():
    x = randint(100, 700)
    y = randint(100, 500)
    a = randint(30, 50)
    color = COLORS[randint(0, 5)]
    polygon(screen, color, [[x, y], [x + a // 2, y - a],
                            [x + a, y]])
    parameters = [x, y, a, color]
    return parameters


def ball(parameters):
    x = parameters[0]
    y = parameters[1]
    r = parameters[2]
    color = parameters[3]
    circle(screen, color, (x, y), r)


def triangle(parameters):
    x = parameters[0]
    y = parameters[1]
    a = parameters[2]
    color = parameters[3]
    polygon(screen, color, [[x, y], [x + a // 2, y - a],
                            [x + a, y]])


def speed():
    x_speed = randint(-500, 500) / 100
    y_speed = randint(-500, 500) / 100
    return [x_speed, y_speed]


def score_message(msg, color):
    mesg = font_style.render("Score: " + str(msg), True, color)
    screen.blit(mesg, [1000, 70])


def timer_message(timer, color):
    mesg = font_style.render("Time: " + str(timer), True, color)
    screen.blit(mesg, [1000, 120])


def win_message(color):
    mesg = font_style_finish.render("YOU WIN!", True, color)
    screen.blit(mesg, [300, 400])


def lose_message(color):
    mesg = font_style_finish.render("YOU LOSE!", True, color)
    screen.blit(mesg, [300, 400])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

num_of_balls = 3
num_of_triangles = 3
timer = 5
finish_time = 0
score = 0
parameters_balls = []
parameters_triangles = []
speed_list_balls = []
speed_list_triangles = []

for i in range(num_of_balls):
    parameters_balls.append(new_ball())
    speed_list_balls.append(speed())

for i in range(num_of_triangles):
    parameters_triangles.append(new_triangle())
    speed_list_triangles.append(speed())

while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)

    for num_of_ball in range(num_of_balls):
        parameters_balls[num_of_ball][0] += speed_list_balls[num_of_ball][0]
        parameters_balls[num_of_ball][1] += speed_list_balls[num_of_ball][1]
        if parameters_balls[num_of_ball][0] + parameters_balls[num_of_ball][2] >= 1200 or \
                parameters_balls[num_of_ball][0] - parameters_balls[num_of_ball][2] <= 0:
            speed_list_balls[num_of_ball][0] = -speed_list_balls[num_of_ball][0]
        if parameters_balls[num_of_ball][1] + parameters_balls[num_of_ball][2] >= 900 or \
                parameters_balls[num_of_ball][1] - parameters_balls[num_of_ball][2] <= 0:
            speed_list_balls[num_of_ball][1] = -speed_list_balls[num_of_ball][1]

    for num_of_triangle in range(num_of_triangles):
        parameters_triangles[num_of_triangle][0] += speed_list_triangles[num_of_triangle][0]
        parameters_triangles[num_of_triangle][1] += speed_list_triangles[num_of_triangle][1]
        if parameters_triangles[num_of_triangle][0] + parameters_triangles[num_of_triangle][2] >= 1200 or \
                parameters_triangles[num_of_triangle][0] <= 0:
            speed_list_triangles[num_of_triangle][0] = -speed_list_triangles[num_of_triangle][0]
        if parameters_triangles[num_of_triangle][1] >= 900 or \
                parameters_triangles[num_of_triangle][1] - parameters_triangles[num_of_triangle][2] <= 0:
            speed_list_triangles[num_of_triangle][1] = -speed_list_triangles[num_of_triangle][1]

    for num_of_ball in range(len(parameters_balls)):
        ball(parameters_balls[num_of_ball])

    for num_of_triangle in range(len(parameters_triangles)):
        triangle(parameters_triangles[num_of_triangle])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for num_of_ball, position in enumerate(parameters_balls):
                if (event.pos[0]-position[0])**2 + (event.pos[1]-position[1])**2 <= position[2]**2:
                    score += 1
                    parameters_balls[num_of_ball] = new_ball()
                    speed_list_balls[num_of_ball] = speed()
            for num_of_triangle, position in enumerate(parameters_triangles):
                x0, y0 = event.pos[0], event.pos[1]
                x1, y1 = position[0], position[1]
                x2, y2 = position[0] + position[2]//2, position[1] - position[2]
                x3, y3 = position[0] + position[2], position[1]
                a = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
                b = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
                c = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
                if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):
                    score += 3
                    parameters_triangles[num_of_triangle] = new_triangle()
                    speed_list_triangles[num_of_triangle] = speed()
    timer -= 1/120

    score_message(str(score), MAGENTA)
    timer_message(str(int(timer)), MAGENTA)
    pygame.display.update()

    if score >= 2 and timer >= 0:
        win_message(RED)
        finished = True
    elif timer < 0:
        lose_message(RED)
        finished = True

    pygame.display.update()


pygame.quit()