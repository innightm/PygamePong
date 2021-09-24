import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    #Этот класс представляет "весло".

    def __init__(self, color, width, height):
        #Вызываем родительский класс (Sprite) конструктор
        super().__init__()

        #Цвет "весла", а так же его координаты x и y, ширину и высоту
        #Установите цвет фона и сделайте его прозрачным
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #Нарисуем "весло" (прямоугольник!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #Получаем объект прямоугольника, который имеер размеры изображения
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Убедиться, что мы не зашли слишком далеко (за кадром)
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        #Убедиться, что мы не зашли слишком далеко (за кадром)
        if self.rect.y > 400:
            self.rect.y = 400
