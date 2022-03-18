import pygame, sys
from bullet import Bullet
from ino import Ino
import time


# тут все функции, которые отрисовывают, обновляют экран, обрабатывают события

def events(screen, gun, bullets):  # напишем функцию, которая будет прослушивать события
    for event in pygame.event.get():  # в цикле перебираем все события в игре
        if event.type == pygame.QUIT:  # событие завершения игры, с помощью модуля sys с методом exit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # напишем код, который реагирует на нажатие клавиши D
                gun.mright = True
            elif event.key == pygame.K_a:  # напишем код, который реагирует на нажатие клавиши A
                gun.mleft = True
            elif event.key == pygame.K_SPACE:  # пропишем событие для нажатия клавиши пробел
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)  # добавляем пульку в контейнер bullets
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:  # если клавиша D отжата
                gun.mright = False
            elif event.key == pygame.K_a:  # если клавиша A отжата
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, inos, bullets):  # создаем функцию, отвестсвенную за обновление экрана
    screen.fill(bg_color)  # фоновый цвет
    sc.show_score()  # выводим текущий счет
    for bullet in bullets.sprites():  # выводим пульки из пушки
        bullet.draw_bullet()
    gun.output()  # вызываем функци. output() из gun.py, которая отрисовывает пушку
    inos.draw(screen)  # добавляем инопланетянин (отрисовываем их)
    pygame.display.flip()  # прорисуем последний экран


def update_bullets(screen, stats, sc, inos, bullets):  # обновление позиции пули
    bullets.update()  # отрисуем и поместим на экран пули
    for bullet in bullets.copy():  # удаляем все пульки, которые вышли за пределы экрана, чтобы не тратить память на комп-е
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True,
                                            True)  # проверяем попадание пуль в пришельцев (коллизии), делаем словарь - ключь: пулька, значение: пришелец
    if collisions:  # если словарь создался (пулька перекрывает пришельца)
        for inos in collisions.values():
            stats.score += 10 * len(inos)  # мы увеличиваем тек. счет кол-во убитый пришельцев * 10
        sc.image_score()  # показываем на экране счет
        chec_height_score(stats, sc) # вывели проверку рекорда
        sc.image_guns()  # показываем кол-во жизней
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def gun_kill(stats, screen, sc, gun, inos,
             bullets):  # создадим новую функцию уничтожения пушки при столкновении с пришельцем
    if stats.guns_left > 0:
        stats.guns_left -= 1  # отнимаем одну жизнь, после того, как пушка столкнулась с пришельцем
        sc.image_guns()  # отрисуем кол-во жизней после того, как отняли
        inos.empty()  # очистим группу пришельцев после столкновения
        bullets.empty()  # очистим группу пуль после столкновения
        create_army(screen, inos)  # после перезагрузки создаем заново армию пришельцев
        gun.create_gun()
        time.sleep(1)  # время перезагрузки
    else:
        stats.run_game = False
        sys.exit()


def update_inos(stats, screen, sc, gun, inos, bullets):  # обновление позиции пришельцев
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):  # проверяем коллизии между пришельцами и пушкой
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc, gun, inos,
               bullets):  # создадим функцию, где мы будем проверять, дошли ли пришельцы до нижней части экрана
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


def create_army(screen, inos):  # напишем функцию, которая создает всю армию инопланетян
    ino = Ino(screen)  # чтобы узнать ширину одного пришельца, создаем его здесь
    ino_width = ino.rect.width  # ширина одного пришельца
    number_ino_x = int((700 - 2 * ino_width) / ino_width)  # теперь рассчитаем, сколько в один ряд помещается пришельцев
    ino_height = ino.rect.height  # подтянем высоту одного пришельца, чтобы рассчитать сколько у нас может быть рядов
    number_ino_y = int((600 - 100 - 2 * ino_height) / ino_height)  # теперь рассчитаем, сколько нужно рядов пришельцев

    for row_number in range(number_ino_y - 1):  # создаем цикл, которвый создает сами ряды
        for ino_number in range(
                number_ino_x):  # теперь начинаем создавать цикл, который заполнит и создаст один ряд пришельцев
            ino = Ino(screen)  # создаем одного пришешльца
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)  # добавляем пришельцев в группу inos


def chec_height_score(stats, sc):  # создадим функцию, которая будет проверять новый рекорд и записывать рекорд в файл
    if stats.score > stats.height_score:
        stats.height_score = stats.score
        sc.image_height_score()
        with open('heightscore.txt', 'w') as f:
            f.write(str(stats.height_score))
