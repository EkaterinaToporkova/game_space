import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores():  # вывод игровой информации
    def __init__(self, screen, stats):  # инициализируем подсчет очков
        self.screen = screen  # подключаем экран, на котором будем отрисовывать счет
        self.screen_rect = screen.get_rect()  # получаем объект rect от экрана
        self.stats = stats  # получаем атрибует, ответственный за статистику
        self.text_color = (225, 190, 231)  # настраиваем цвет текста
        self.font = pygame.font.SysFont(None, 36)  # настраиваем шрифт
        self.image_score()  # вызовем метод, который этот шрифт отрисует
        self.image_height_score()  # вызовем функцию, отвественная за рекорд
        self.image_guns()  # выведем кол-во жизней

    def image_score(self):  # роебразует текст счет в изображение
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (203, 96, 211))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_height_score(self):  # проебразует рекорд в гравическое изображение
        self.height_score_image = self.font.render(str(self.stats.height_score), True, self.text_color, (203, 96, 211))
        self.height_score_rect = self.height_score_image.get_rect()
        self.height_score_rect.centerx = self.screen_rect.centerx
        self.height_score_rect.top = self.screen_rect.top + 20

    def image_guns(self): # пропишем метод вызова кол-ва жизней
        self.guns = Group() # создадим группу с маленькими пушками (кол-во жизней)
        for gun_number in range(self.stats.guns_left):  # в цикле будем перебирать столько пушечек, сколько будет жизней
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun) # добавляем маленькую пушечку в группу Guns

    def show_score(self):  # напишем функцию, для отображения текста счета, рекорда и кол-ва жизней на экране
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.height_score_image, self.height_score_rect)
        self.guns.draw(self.screen)
