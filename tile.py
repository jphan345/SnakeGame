# tile.py

import pygame


class TileStateError(Exception):
    pass


class Tile:
    WHITE = (175, 175, 175)
    RED = (125, 39, 39)
    DARK_BLUE = (30, 32, 40)

    def __init__(self, display: pygame.display, size: int, position: tuple):
        self._display = display
        self._size = size
        self._pos = position
        self._color = self.WHITE

    def _change_color(self, new_color: tuple) -> None:
        self._color = new_color

    def change_state(self, state: str) -> None:
        state = state.upper()

        if state == "BLANK":
            self._color = self.WHITE
        elif state == "SNAKE":
            self._color = self.DARK_BLUE
        elif state == "SNACK":
            self._color = self.RED
        else:
            raise TileStateError("Invalid state", state, "specified.")

    def draw(self) -> None:
        # noinspection PyRedundantParentheses
        tile = pygame.Rect((self._pos), (self._size, self._size))  # Pygame Rect: (position: tuple, size: tuple)
        pygame.draw.rect(self._display, self._color, tile)
