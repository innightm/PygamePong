import pygame
from random import randint

BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    # Этот класс представляет мяч. Это происходит от класса "Sprite" в Pygame

    def __init__(self, color, width, height):
        #Вызываем родительский класс (Sprite) конструктор
        super().__init__()

        #Цвет шара а так же его ширину и высоту
        #Установите цвет фона и сделайте его прозрачным
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)



        # Нарисуем мяч (прямоугольник!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4,8),randint(-8,8)]
        #ball_image = pygame.image.load("images/Orbs.png").convert()
        # Делаем черный цвет прозрачным для спрайта мячика
        #ball_image.set_colorkey(BLACK)

        #Получаем объект прямоугольника, который имеер размеры изображения
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
