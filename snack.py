# snack.py

import random


class Snack:
    def __init__(self, start_x=11, start_y=7):
        self._x = start_x
        self._y = start_y

    def get_pos(self):
        return self._x, self._y

    def change_pos(self, off_limits: list):
        self._x = random.randint(0, 14)
        self._y = random.randint(0, 14)

        while (self._x, self._y) in off_limits:
            self._x = random.randint(0, 14)
            self._y = random.randint(0, 14)
