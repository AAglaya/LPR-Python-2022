import math
import random as rnd
from random import choice

import pygame


FPS = 100

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GUN_COLOR = (16, 160, 173)
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.g = 3
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.vx_pos = 7
        self.vy_pos = 7
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy = self.vy - self.g
        if self.y + self.r >= 600 or self.y - self.r <= 0:
            self.vy = -self.vy * 0.65
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx = -self.vx * 0.9
        if self.x + self.r >= 800:
            self.x = self.x - abs(self.vx)
        if self.x - self.r <= 0:
            self.x = self.x + abs(self.vx)
        if self.y + self.r >= 600:
            self.y = self.y - abs(self.vy)
        if self.y - self.r <= 0:
            self.y = self.y + abs(self.vy)
        if abs(self.vy) <= 3.5 and self.y >= 550:
            self.vy = 0
            self.g = 0
            self.y = 600 - self.r
            self.vx *= 0.85

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GUN_COLOR
        self.x = 30
        self.y = 500
        self.r = 10
        self.vx = 7
        self.vy = 7

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-self.y) / (event.pos[0]-self.x))
        if self.f2_on:
            self.color = self.color
        else:
            self.color = GUN_COLOR

    def draw(self):
        pygame.draw.line(self.screen, self.color, (self.x, self.y),
                         (self.x + math.cos(self.an) * (15 + self.f2_power / 2),
                          self.y + math.sin(self.an) * (15 + self.f2_power / 2)), width=7)

        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 50:
                self.f2_power += 1
                if self.color[0] <= 250 and self.color[1] >= 5 and self.color[2] >= 5:
                    self.color = (self.color[0] + GUN_COLOR[0] / (FPS * 2), self.color[1] - GUN_COLOR[1] / (FPS * 2),
                                  self.color[2] - GUN_COLOR[2] / (FPS * 2))
        else:
            self.color = GUN_COLOR

    def move_up(self):
        '''Отвечает за движение пушки вверх'''
        if self.y - self.r >= 0:
            self.y -= self.vy

    def move_down(self):
        '''Отвечает за движение пушки вниз'''
        if self.y + self.r <= 600:
            self.y += self.vy

    def move_right(self):
        '''Отвечает за движение пушки вправо'''
        if self.x + self.r <= 800:
            self.x += self.vx

    def move_left(self):
        '''Отвечает за движение пушки влево'''
        if self.x - self.r >= 20:
            self.x -= self.vx



class Target:
    def __init__(self, screen):
        self.screen = screen
        self.points = 0
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd.randint(50, 750)
        self.y = rnd.randint(50, 550)
        self.r = rnd.randint(10, 30)
        self.vx = rnd.randint(0, 30) / 10
        self.vy = rnd.randint(0, 30) / 10
        self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """Отвечает за движение мишени"""
        self.x += self.vx
        self.y -= self.vy
        if self.x + self.vx - self.r < 0 or self.x + self.vx + self.r > 800:
            self.vx = -self.vx
        elif self.y - self.vy - self.r < 0 or self.y - self.vy + self.r > 600:
            self.vy = - self.vy

    def gun_hit(self, obj):
        """Проверяет, врезался ли снаряд в пушку"""
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) > (
                (self.x + self.vx - obj.x) ** 2 + (self.y + self.vy - obj.y) ** 2):
            return ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= (self.r + obj.r) ** 2
        else:
            return False


pygame.init()
screen = pygame.display.set_mode((800, 600))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target(screen)
target2 = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        if pygame.key.get_pressed()[pygame.K_w]:
            gun.move_up()
        if pygame.key.get_pressed()[pygame.K_s]:
            gun.move_down()
        if pygame.key.get_pressed()[pygame.K_a]:
            gun.move_left()
        if pygame.key.get_pressed()[pygame.K_d]:
            gun.move_right()

    target1.move()
    target2.move()
    if target1.gun_hit(gun) or target2.gun_hit(gun):
        finished = True

    for b in balls:
        b.move()
        if b.hittest(target1):
            target1.hit()
            target1.new_target()
        if b.hittest(target2):
            target2.hit()
            target2.new_target()
    gun.power_up()

pygame.quit()
