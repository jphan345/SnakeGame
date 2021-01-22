# snake.py


class Snake:
    def __init__(self):
        self._positions = [(2, 7), (3, 7), (4, 7)]      # the tail is at index 0; head at last index
        self._head = (4, 7)
        self._prev_tail = (2, 7)

    def move_up(self) -> None:
        self._head = (self._head[0], self._head[1] + 1)
        self._prev_tail = self._positions[0]
        self._positions.append(self._head)
        self._positions.pop(0)

    def move_down(self) -> None:
        self._head = (self._head[0], self._head[1] - 1)
        self._prev_tail = self._positions[0]
        self._positions.append(self._head)
        self._positions.pop(0)

    def move_left(self) -> None:
        self._head = (self._head[0] - 1, self._head[1])
        self._prev_tail = self._positions[0]
        self._positions.append(self._head)
        self._positions.pop(0)

    def move_right(self) -> None:
        self._head = (self._head[0] + 1, self._head[1])
        self._prev_tail = self._positions[0]
        self._positions.append(self._head)
        self._positions.pop(0)

    def grow(self):
        self._positions.insert(0, self._prev_tail)

    def touching_self(self) -> bool:
        snake_length = len(self._positions)
        if self._head in self._positions[:snake_length - 1]:
            return True
        else:
            return False

    def touching_edge(self) -> bool:
        if self._head[0] >= 15 or self._head[0] <= -1:
            return True
        elif self._head[1] >= 15 or self._head[1] <= -1:
            return True
        else:
            return False

    def get_pos(self):
        return self._positions

    def get_head(self):
        return self._head
