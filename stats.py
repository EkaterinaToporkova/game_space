# здесь будет отслеживаться вся статистика игры

class Stats():  # создадим класс для отслеживания статистики
    def __init__(self):  # инициализируем статистику
        self.reset_stats()
        self.run_game = True  # создадим атрибут, который будет проверять, если счет равен 0, то будет возвращать False и игра закончится
        with open('heightscore.txt', 'r') as f:
            self.height_score = int(f.readline())  # пропишем рекорд

    def reset_stats(self):  # статистика, изменяющаяся во время игры
        self.guns_left = 2  # создадим атрибут для подсчета кол-ва жизней
        self.score = 0  # создадим атрибут, который будет отвественнен за текущий счет



