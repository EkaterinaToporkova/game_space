import pygame


# здесь вся логика пуль


class Bullet(pygame.sprite.Sprite):  # создаем новый класс на основе класса, который есть в модуле sprite

    def __init__(self, screen,
                 gun):  # прописываем метод __init__, передаем в кач-ве атрбиута экран и пушку, чтобы пуля была в позиции пушки
        super(Bullet, self).__init__()  # т.к. класс дочерний, прописываем метод super
        self.screen = screen  # загрузили экран
        self.rect = pygame.Rect(0, 0, 2, 12)  # создаем пули в координате 0, 0
        self.color = 225, 190, 231  # создаем цвет пули
        self.speed = 4.5  # создаем скорость пули
        self.rect.centerx = gun.rect.centerx  # пишем появление пули в верхней части пушки (из дула) в центре
        self.rect.top = gun.rect.top  # пишем появление пули в верхней части пушки (из дула) в центре
        self.y = float(self.rect.y)  # изменение позиции пули до верха

    def update(self):  # перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y  # обновление позиции пули

    def draw_bullet(self):  # отсуем пулю на графическом экране
        pygame.draw.rect(self.screen, self.color, self.rect)
