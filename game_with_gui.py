import pygame as pg
import utils
from game import Game
import constains

pg.init()

board = pg.display.set_mode(
    (constains.BOARD_SIZE_WIDTH, constains.BOARD_SIZE_HEIGHT))
pg.display.set_caption('Code for food team')

clock = pg.time.Clock()


def handleKeyboardEvent(key):

    if key == pg.K_LEFT:
        return (-1, 0)
    if key == pg.K_RIGHT:
        return (1, 0)
    if key == pg.K_UP:
        return (0, -1)
    if key == pg.K_DOWN:
        return (0, 1)

    return (0, 0)

def drawScore(display, score):
    text = pg.font.SysFont("arial", 20).render(
        f"Eaten: {score}", True, (255, 128, 128))

    display.blit(text, [15, 15])

def drawSnake(display, snakes):
    for snake in snakes:
        pg.draw.rect(display, constains.SNAKE_COLOR, [
                     snake[0]*constains.CELL_SIZE, snake[1] *
                     constains.CELL_SIZE,
                     constains.CELL_SIZE, constains.CELL_SIZE])


def normalGame():

    game = Game()
    game.init()

    isExiting = False
    while isExiting == False:
        nextMove = (0, 0)

        # This the scope of normal game
        for event in pg.event.get():
            if event.type != pg.KEYDOWN:
                continue

            if event.key == pg.K_q:
                isExiting = True
                break

            if event.type == pg.KEYDOWN:
                # print(event.type)
                nextMove = handleKeyboardEvent(event.key)
                print(nextMove)
                break

        game.move([nextMove[0], nextMove[1], 0])

        board.fill(constains.BOARD_COLOR)
        pg.draw.rect(board, constains.FOOD_COLOR, [
            game.food.x*constains.CELL_SIZE, game.food.y*constains.CELL_SIZE,
            constains.CELL_SIZE, constains.CELL_SIZE])

        drawSnake(board, [[game.snake.headX, game.snake.headY], *game.snake.tails])
        drawScore(board, game.snake.size - 1)

        pg.display.update()

        while game.snake.hasDead == True:
            board.fill((255, 255, 255))

            utils.drawText(
                board, "Game over! Quit -> Q or give a Retry -> R", (213, 50, 80))

            drawScore(board, game.snake.size - 1)
            pg.display.update()

            for event in pg.event.get():
                if event.type != pg.KEYDOWN:
                    continue

                if event.key == pg.K_q:
                    isExiting = True
                elif event.key == pg.K_r:
                    game.init()

        clock.tick(constains.GAME_PFS)

    pg.quit()

    quit()


normalGame()
