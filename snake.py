import random
from tkinter import LEFT, RIGHT
import constains
# from models.direction import Direction

class Snake:
    headX = 0
    headY = 0
    tails = []

    size = 1

    direction = [0,0,0,0]

    hasHitWall = False
    hasHitTail = False
    hasHitApple = False

    hasDead = False

    # def __init__(self):

    def init(self):
        self.headX = 0
        self.headY = 0
        self.size = 1
        self.tails = []

        self.direction = [0,0,0,0]

        self.hasDead = False
        self.hasHitApple = False
        self.hasHitTail = False

        

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

    def move(self, newDirection, foodX, foodY):
        # Snake cannot turn 180 degree, from left to right or from right to left
        invalidMove = self.direction[constains.LEFT] + newDirection[constains.RIGHT] == 2 or self.direction[constains.RIGHT] + newDirection[constains.LEFT] == 2
        # Snake cannot turn 180 degree, from up to down or from down to to
        invalidMove = invalidMove or self.direction[constains.UP] + newDirection[constains.DOWN] == 2 or self.direction[constains.DOWN] + newDirection[constains.UP] == 2
        
        if invalidMove == False:
            # print('Valid move')
            print(newDirection)
            self.direction = [*newDirection]
            

        self.headX += self.direction[constains.LEFT] * -1 + self.direction[constains.RIGHT]
        self.headY += self.direction[constains.UP] * -1 + self.direction[constains.DOWN] 

        snakeHead = [self.headX, self.headY]
        self.tails.append(snakeHead)

        # While the snake is moving, we remove the last tail and add the head
        if len(self.tails) > self.size:
            del self.tails[0]

        self.updateState(foodX, foodY)

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
