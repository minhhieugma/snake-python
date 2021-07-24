import pygame as pg
import utils
import snake as s
import game_rule
import constains
import food as f

pg.init()

board = pg.display.set_mode(
    (constains.BOARD_SIZE_WIDTH, constains.BOARD_SIZE_HEIGHT))
pg.display.set_caption('Code for food team')

clock = pg.time.Clock()


def normalGame():

    snake = s.Snake()
    snake.randomPosition()

    food = f.Food()
    food.randomPosition(snake.block)

    isExiting = False
    isDead = False
    while isExiting == False:

        for event in pg.event.get():

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    snake.moveLeft()
                elif event.key == pg.K_RIGHT:
                    snake.moveRight()
                elif event.key == pg.K_UP:
                    snake.moveUp()
                elif event.key == pg.K_DOWN:
                    snake.moveDown()

            elif event.type == pg.QUIT:
                isExiting = True

        snake.move()

        isDead = snake.hitTheWals()

        board.fill(constains.BOARD_COLOR)
        pg.draw.rect(board, constains.FOOD_COLOR, [
                         food.x, food.y, 
                         constains.CELL_SIZE, constains.CELL_SIZE])

        isDead = isDead or snake.hitItself()

        s.drawSnake(board, snake.block, [[snake.headX, snake.headY], *snake.tails])
        # s.drawSnake(board, snake.block, snake.tails)
        game_rule.drawScore(board, snake.size - 1)

        pg.display.update()

        if snake.hitTheFood(food.x, food.y):
            food.randomPosition(food)

            snake.increaseSize()

        while isDead == True:
            board.fill((255, 255, 255))

            utils.drawText(
                board, "Game over! Quit -> Q or give a Retry -> R", (213, 50, 80))

            game_rule.drawScore(board, snake.size - 1)
            pg.display.update()

            for event in pg.event.get():
                if event.type != pg.KEYDOWN:
                    continue

                if event.key == pg.K_q:
                    isExiting = True
                    isDead = False
                elif event.key == pg.K_r:
                    normalGame()


        clock.tick(constains.GAME_PFS)

    pg.quit()

    quit()


normalGame()
