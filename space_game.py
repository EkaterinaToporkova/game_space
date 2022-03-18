import pygame, controls
from gun import Gun  # подключаем gun.py к нашей программе
from pygame.sprite import Group
from stats import Stats
from scores import Scores


# логика: запуск и инициализая pygame, создание объета экрана
def run():
    pygame.init()  # инициализируем игру с помощью метода init()
    screen = pygame.display.set_mode((700,
                                      800))  # создаем отображаемую область (screen), в которой будут все графические элемента игры, метод set_mode() - размер окна
    pygame.display.set_caption(
        'Космические защитники')  # создаем заголовок для графического окна с помощью метода set_caption()
    bg_color = (203, 96, 211)  # создаем фоновый цвет для окна
    gun = Gun(screen)  # создаем наш объект пушки
    bullets = Group()  # создаем объект пуль
    inos = Group()  # создаем объект - несколько инопланетянин
    controls.create_army(screen, inos)  # вызовем функцию, которая создает всю армию инопланетян
    stats = Stats()
    sc = Scores(screen, stats)  # создаем экземпляр на базе класса Scores

    # пишем главный цикл игры
    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)  # обновляет позицию пришельцев


run()
