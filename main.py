# main.py

from config import board_size, screen_size
from snake import Snake
from snack import Snack
from tile import Tile
import pygame


def print_game(my_snake: Snake, my_snack, size: int):
    snake_pos_list = my_snake.get_pos()
    snack_pos = my_snack.get_pos()

    for square in range(size - 1, -1, -1):
        for row in range(size):
            if (row, square) in snake_pos_list:
                print('⬜', end=' ')
            elif (row, square) == snack_pos:
                print('🔷', end=' ')
            else:
                print('⬛', end=' ')
        print()


def draw_board(dis: pygame.display, size: int, my_snake: Snake, my_snack: Snack):
    dis.fill((30, 32, 40))  # dark blue

    snake_pos_list = my_snake.get_pos()
    snack_pos = my_snack.get_pos()

    increment = min(display.get_size()) / size

    for y in range(size):
        for x in range(size):
            tile_size = increment - 2
            tile_pos = (x * increment, (-y + size - 1) * increment)
            tile = Tile(dis, tile_size, tile_pos)

            if (x, y) in snake_pos_list:
                tile.change_state('SNAKE')
            elif (x, y) == snack_pos:
                tile.change_state('SNACK')
            else:
                tile.change_state('BLANK')
            tile.draw()

    pygame.display.update()


if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()

    display = pygame.display.set_mode(screen_size)

    snake = Snake(board_size)
    snack = Snack(board_size)

    # Queue to keep track of the direction
    directions = ["RIGHT"]

    running = True
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and len(directions) <= 4:
                if event.key == pygame.K_UP:
                    directions.append("UP")
                elif event.key == pygame.K_DOWN:
                    directions.append("DOWN")
                elif event.key == pygame.K_RIGHT:
                    directions.append("RIGHT")
                elif event.key == pygame.K_LEFT:
                    directions.append("LEFT")

        while len(directions) != 0 and directions[0] == snake.get_direction():
            directions.pop(0)

        if len(directions) != 0:
            snake.change_direction(directions[0])
            directions.pop(0)
        snake.move()

        if snake.get_head() == snack.get_pos():
            snake.grow()
            snack.change_pos(snake.get_pos())

        if snake.touching_self() or snake.touching_edge():
            running = False

        draw_board(display, board_size, snake, snack)

    # print_game(snake, snack, board_size)
    #
    # running = True
    # while running:
    #     action = input('Input action: ')
    #     action = action.strip().upper()
    #     if action == 'LEFT':
    #         snake.move_left()
    #     elif action == 'RIGHT':
    #         snake.move_right()
    #     elif action == 'UP':
    #         snake.move_up()
    #     elif action == 'DOWN':
    #         snake.move_down()
    #     elif action == 'NONE':
    #         pass
    #     elif action == 'QUIT':
    #         running = False
    #         break
    #     else:
    #         print('Invalid action; Try again.')
    #
    #     if snake.get_head() == snack.get_pos():
    #         snake.grow()
    #         snack.change_pos()
    #
    #         while snack.get_pos() in snake.get_pos():
    #             snack.change_pos()
    #
    #     if snake.touching_self() or snake.touching_edge():
    #         running = False
    #
    #     print_game(snake, snack, board_size)
