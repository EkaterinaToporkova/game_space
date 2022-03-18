import pygame
from pygame.sprite import Sprite

# здесь вся логика пушки

# соберем всю логику лазерной пушки в один класс
class Gun(Sprite):

    def __init__(self, screen):  # напишем метод инициализации пушки
        super(Gun, self).__init__()
        self.screen = screen  # получаем экран
        self.image = pygame.image.load(
            'images/pixil-frame-0.png')  # загружаем изображение пушки, метод load() загружает изображение из папки, куда мы его поместили
        # нужно получить поверхность экрана и поверхность картинки
        self.rect = self.image.get_rect()  # это мы получаем картинку
        self.screen_rect = screen.get_rect()  # это мы получаем экран
        self.rect.centerx = self.screen_rect.centerx  # прописываем координаты центра пушки
        self.center = float(self.rect.centerx)  # делаем преобразование числа в атрибуте rect в вещ. число
        self.rect.bottom = self.screen_rect.bottom  # прописываем координаты низа пушки
        self.mright = False  # создаем логическую переменную, в которой два значения: True - клавиша нажата, False - клавиша отжата (вправо)
        self.mleft = False  # создаем логическую переменную, в которой два значения: True - клавиша нажата, False - клавиша отжата (влево)

    def output(self):  # напишем функцию, которая вывод пушку на экран (делаем с помощью метода blit())
        self.screen.blit(self.image, self.rect)

    def update_gun(self):  # обновление позиции пушки
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5  # если клавиша D нажата, перемещаем пушку на 1.5 единицы вправо
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5  # если клавиша A нажата, перемещаем пушку на 1.5 единицы влево

        self.rect.centerx = self.center  # подключили атрибут center

    def create_gun(self):  # пропишем функцию, при вызове которой наша пушка будет появляться в центре экрана
        self.center = self.screen_rect.centerx
