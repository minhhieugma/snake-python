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


def normalGame():

    snake = s.Snake()
    snake.randomPosition()

    food = f.Food()
    food.randomPosition()

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

            

        # ---------------- Game Logic - START ---------------------    
        if not (nextMove[0] == 0 and nextMove[1] == 0):
            snake.changeDirection(nextMove[0], nextMove[1])
        
        snake.move()
        snake.updateState(food.x, food.y)

        if snake.hasHitApple:
            food.randomPosition()
            snake.hasHitApple = False

        # ---------------- Game Logic - END ---------------------    

        board.fill(constains.BOARD_COLOR)
        pg.draw.rect(board, constains.FOOD_COLOR, [
            food.x*constains.CELL_SIZE, food.y*constains.CELL_SIZE,
            constains.CELL_SIZE, constains.CELL_SIZE])

        s.drawSnake(board, [[snake.headX, snake.headY], *snake.tails])
        game_rule.drawScore(board, snake.size - 1)

        pg.display.update()

        while snake.hasDead == True:
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
                elif event.key == pg.K_r:
                    normalGame()

        clock.tick(constains.GAME_PFS)

    pg.quit()

    quit()


normalGame()
