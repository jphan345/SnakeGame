# snake.py

class SnakeDirectionError(Exception):
    pass


class Snake:
    def __init__(self, board_size: int):
        self._board_size = board_size
        self._positions = [(2, 7), (3, 7), (4, 7)]      # the tail is at index 0; head at last index
        self._head = (4, 7)
        self._prev_tail = (2, 7)
        self._direction = "RIGHT"

    def _move_up(self) -> None:
        self._head = (self._head[0], self._head[1] + 1)
        self._prev_tail = self._positions[0]
        self._positions.append(self._head)
        self._positions.pop(0)

    def _move_down(self) -> None:
        self._head = (self._head[0], self._head[1] - 1)
        self._prev_tail = self._positions[0]
        self._positions.append(self._head)
        self._positions.pop(0)

    def _move_left(self) -> None:
        self._head = (self._head[0] - 1, self._head[1])
        self._prev_tail = self._positions[0]
        self._positions.append(self._head)
        self._positions.pop(0)

    def _move_right(self) -> None:
        self._head = (self._head[0] + 1, self._head[1])
        self._prev_tail = self._positions[0]
        self._positions.append(self._head)
        self._positions.pop(0)

    def move(self):
        if self._direction == "RIGHT":
            self._move_right()
        elif self._direction == "LEFT":
            self._move_left()
        elif self._direction == "UP":
            self._move_up()
        elif self._direction == "DOWN":
            self._move_down()

    def change_direction(self, direction: str):
        direction = direction.upper()
        if direction != self._direction:
            if direction == "RIGHT" and self._direction != "LEFT":
                self._direction = "RIGHT"
            elif direction == "LEFT" and self._direction != "RIGHT":
                self._direction = "LEFT"
            elif direction == "UP" and self._direction != "DOWN":
                self._direction = "UP"
            elif direction == "DOWN" and self._direction != "UP":
                self._direction = "DOWN"

    def get_direction(self):
        return self._direction

    def grow(self):
        self._positions.insert(0, self._prev_tail)

    def touching_self(self) -> bool:
        snake_length = len(self._positions)
        if self._head in self._positions[:snake_length - 1]:
            return True
        else:
            return False

    def touching_edge(self) -> bool:
        if self._head[0] >= self._board_size or self._head[0] <= -1:
            return True
        elif self._head[1] >= self._board_size or self._head[1] <= -1:
            return True
        else:
            return False

    def get_pos(self):
        return self._positions

    def get_head(self):
        return self._head
