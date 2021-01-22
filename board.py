# board.py
import pygame


class Board:
    def __init__(self, row: int, col: int):
        self._board = [[0 for _ in range(col)] for _ in range(row)]
