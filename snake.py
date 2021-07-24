
import pygame as pg

import random
import constains


class Snake:
    headX = 0
    headY = 0
    tails = []

    size = 1

    momentumX = 0
    momentumY = 0

    hasHitWall = False
    hasHitTail = False
    hasHitApple = False

    hasDead = False

    def __init__(self):
        self.headX = 0
        self.headY = 0
        self.size = 1

    def randomPosition(self):
      # Let's say the board width is 1000, and the width of the snake is 50
      # It means we have exactly 1000/50 = 200 positions to place the snake at
      # => The same to height as well

        self.headX = random.randrange(0, constains.NORMALIZED_WIDTH)
        self.headY = random.randrange(0, constains.NORMALIZED_HEIGHT)

    def updateState(self, foodX, foodY):
        self.hasHitWall = self.hitTheWals()
        self.hasHitTail = self.hitItself()
        self.hasHitApple = self.hitTheFood(foodX, foodY)

        self.hasDead = self.hasHitWall or self.hasHitTail
      
        if self.hasHitApple:
            self.increaseSize()


    def move(self):

        self.headX += self.momentumX
        self.headY += self.momentumY

        snakeHead = [self.headX, self.headY]
        self.tails.append(snakeHead)

        # While the snake is moving, we remove the last tail and add the head
        if len(self.tails) > self.size:
            del self.tails[0]

    def changeDirection(self, stepX, stepY):

        if self.momentumX == stepX and self.momentumY == stepY:
            # No change couse of moves
            return

        if self.momentumX != 0 and stepX != 0:
            # Snake cannot turn 180 degree, from left to right or right to left
            return

        if self.momentumY != 0 and stepY != 0:
            # Snake cannot turn 180 degree, from up to down or down to up
            return

        self.momentumX = stepX
        self.momentumY = stepY

        # self.move()

    # def moveLeft(self):
    #     self.changeDirection(-self.block, 0)

    # def moveRight(self):
    #     self.changeDirection(self.block, 0)

    # def moveUp(self):
    #     self.changeDirection(0, -self.block)

    # def moveDown(self):
    #     self.changeDirection(0, self.block)

    def increaseSize(self):
        self.size += 1

    def hitItself(self):
        head = [self.headX, self.headY]

        for tail in self.tails[:-1]:
            if tail == head:
                return True

        return False

    def hitTheWals(self):
        # Break the flow to have a better performance

        hitRightWall = self.headX >= constains.NORMALIZED_WIDTH
        if(hitRightWall):
            return True

        hitLeftWall = self.headX < 0
        if(hitLeftWall):
            return True

        hitTopWall = self.headY >= constains.NORMALIZED_HEIGHT
        if(hitTopWall):
            return True

        hitBottomWall = self.headY < 0
        if(hitBottomWall):
            return True

        # if hitRightWall or hitLeftWall or hitTopWall or hitBottomWall:
        #     return True

        return False

    def hitTheFood(self, foodX, foodY):
        if self.headX == foodX and self.headY == foodY:
            return True

        return False


def drawSnake(display, snakes):
    for snake in snakes:
        pg.draw.rect(display, constains.SNAKE_COLOR, [
                     snake[0]*constains.CELL_SIZE, snake[1] *
                     constains.CELL_SIZE,
                     constains.CELL_SIZE, constains.CELL_SIZE])
