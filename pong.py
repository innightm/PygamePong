#Импорт библиотеки pygame и её инициализация
import pygame
from paddle import Paddle #Оператор импорта для нашего класса
from ball import Ball #импорт мячика

pygame.init()

#Определение цветов, которые используем
BLACK = (0,0,0)
WHITE = (255,255,255)

#Открываем новое окно
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#Список, содержащий все спрайты, используемые в игре
all_sprites_list = pygame.sprite.Group()

#Добавить "весла" в список спрайтов
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#Цикл будет продолжаться до тех пор, пока пользователь не выйдет из игры (например, не нажмет кнопку закрытия)
carryOn = True

#Скорость обновления экрана
clock = pygame.time.Clock()
# Координаты заднего фона
background_position = [0, 0]
background_image = pygame.image.load("images/background.png").convert()


# Инициализируем результаты игрока
scoreA = 0
scoreB = 0

#Основной цикл программы
while carryOn:
    #Основной цикл событий
    for event in pygame.event.get():#Пользователь сделал что-то
        if event.type == pygame.QUIT:#Если пользователь нажал закрыть
            carryOn = False #Отметить что закончили, поэтому выходим из цикла
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x: #Нажатие клавиши x- выход из игры
                carryOn = False

    # Перемещение "весла", когда пользователь использует клавиши со стрелками (игрок A) или клавиши "W / S" (игрок B)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)


    #Логика игры должна идти сюда
    all_sprites_list.update()

    #Убедитесь, что мяч отскакивает от любой из 4 стен:
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    #Обнаружить столкновения между мячом и "веслами"
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    #Код для рисования
    #Очистить экран до чёрного
    screen.fill(BLACK)

    #Нарисуем сеть
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

# Если вы хотите задний фон, поместись здесь
    # Задний фон
    screen.blit(background_image, background_position)
    #Теперь давайте нарисуем все спрайты за один раз.
    all_sprites_list.draw(screen)

    # Отображение баллов:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    #Обновить экран с тем, что нарисовали
    pygame.display.flip()

    #Ограничение до 60-ти кадров в секунду
    clock.tick(60)

#После выхода из основного цикла программы мы можем остановить игровой движок:
pygame.quit()
