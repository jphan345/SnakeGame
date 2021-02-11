# snack.py

import random


class Snack:
    def __init__(self, board_size: int, start_x=11, start_y=7):
        self._board_size = board_size
        self._x = start_x
        self._y = start_y

    def get_pos(self) -> (int, int):
        return self._x, self._y

    def change_pos(self, off_limits: list) -> None:
        self._x = random.randint(0, self._board_size - 1)
        self._y = random.randint(0, self._board_size - 1)

        while (self._x, self._y) in off_limits:
            self._x = random.randint(0, self._board_size - 1)
            self._y = random.randint(0, self._board_size - 1)
