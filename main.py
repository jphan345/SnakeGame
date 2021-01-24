# main.py

from snake import Snake
from snack import Snack


def print_game(my_snake: Snake, my_snack, size: int):
    snake_pos = my_snake.get_pos()
    snack_pos = my_snack.get_pos()

    for square in range(size - 1, -1, -1):
        for row in range(size):
            if (row, square) in snake_pos:
                print('⬜', end=' ')
            elif (row, square) == snack_pos:
                print('🔷', end=' ')
            else:
                print('⬛', end=' ')
        print()


if __name__ == '__main__':
    board_size = 15
    snake = Snake()
    snack = Snack()

    print_game(snake, snack, board_size)

    running = True
    while running:
        action = input('Input action: ')
        action = action.strip().upper()
        if action == 'LEFT':
            snake.move_left()
        elif action == 'RIGHT':
            snake.move_right()
        elif action == 'UP':
            snake.move_up()
        elif action == 'DOWN':
            snake.move_down()
        elif action == 'NONE':
            pass
        elif action == 'QUIT':
            running = False
            break
        else:
            print('Invalid action; Try again.')

        if snake.get_head() == snack.get_pos():
            snake.grow()
            snack.change_pos()

            while snack.get_pos() in snake.get_pos():
                snack.change_pos()

        if snake.touching_self() or snake.touching_edge():
            running = False

        print_game(snake, snack, board_size)
