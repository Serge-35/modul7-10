from threading import Thread
import time

enemy = 100
class Knight(Thread):

    def __init__(self, name, power, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.power = power

    def run(self):
        warriors = enemy
        print(f'{self.name},на нас напали!')
        n = 0
        while warriors != 0:
            warriors = warriors - self.power
            n += 1
            print(f'{self.name} сражается {n} дней(дня)..., осталось {warriors} воинов.', flush=True)
            time.sleep(1)

        print(f'{self.name} одержал победу спустя {n} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('.' * 20, 'Все битвы закончились!')