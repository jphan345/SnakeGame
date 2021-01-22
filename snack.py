# snack.py

import random


class Snack:
    def __init__(self, start_x=11, start_y=7):
        self._x = start_x
        self._y = start_y

    def get_pos(self):
        return self._x, self._y

    def change_pos(self):
        new_x = random.randint(0, 14)
        while new_x == self._x:
            new_x = random.randint(0, 14)

        new_y = random.randint(0, 14)
        while new_y == self._y:
            new_y = random.randint(0, 14)

        self._x = new_x
        self._y = new_y
