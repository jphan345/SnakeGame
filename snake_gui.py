# snake_gui.py

from tile import Tile
from snake import Snake
from snack import Snack
import pygame


class SnakeGUI:
    def __init__(self, display: pygame.display, size: int, snake: Snake, snack: Snack):
        self._display = display
        self._size = size
        self.snake = snake
        self.snack = snack

    def print_board(self):
        self._display.fill((30, 32, 40))  # dark blue

        snake_pos_list = self.snake.get_pos()
        snack_pos = self.snack.get_pos()

        increment = min(self._display.get_size()) / self._size

        for col in range(self._size - 1, -1, -1):
            for row in range(self._size):
                tile_size = increment - 2
                tile_pos = (row * increment, col * increment)
                tile = Tile(self._display, tile_size, tile_pos)

                if (row, col) in snake_pos_list:
                    tile.change_state('SNAKE')
                elif (row, col) == snack_pos:
                    tile.change_state('SNACK')
                else:
                    tile.change_state('BLANK')
                tile.draw()

        pygame.display.update()
