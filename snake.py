import random
from tkinter import LEFT, RIGHT
import constains
import math

# from models.direction import Direction


class Snake:
    headX = 0
    headY = 0

    initHead = (0, 0)

    tails = []

    size = 1

    direction = [0, 0, 0, 0]

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

        self.direction = [0, 0, 0, 0]

        self.hasDead = False
        self.hasHitApple = False
        self.hasHitTail = False

    def randomPosition(self):
      # Let's say the board width is 1000, and the width of the snake is 50
      # It means we have exactly 1000/50 = 200 positions to place the snake at
      # => The same to height as well

        self.headX = random.randrange(0, constains.NORMALIZED_WIDTH)
        self.headY = random.randrange(0, constains.NORMALIZED_HEIGHT)

        self.initHead = (self.headX, self.headY)

    def updateState(self, foodX, foodY):
        self.hasHitWall = Snake.hitTheWals(self.headX, self.headY)
        self.hasHitTail = self.hitItself()
        self.hasHitApple = self.hitTheFood(foodX, foodY)

        self.hasDead = self.hasHitWall or self.hasHitTail

        if self.hasHitApple:
            self.increaseSize()

    def move(self, newDirection, foodX, foodY):
        # Snake cannot turn 180 degree, from left to right or from right to left
        invalidMove = self.direction[constains.LEFT] + \
            newDirection[constains.RIGHT] == 2 or self.direction[constains.RIGHT] + \
            newDirection[constains.LEFT] == 2
        # Snake cannot turn 180 degree, from up to down or from down to to
        invalidMove = invalidMove or self.direction[constains.UP] + \
            newDirection[constains.DOWN] == 2 or self.direction[constains.DOWN] + \
            newDirection[constains.UP] == 2

        if invalidMove == False:
            # print('Valid move')
            print(newDirection)
            self.direction = [*newDirection]

        self.headX += self.direction[constains.LEFT] * - \
            1 + self.direction[constains.RIGHT]
        self.headY += self.direction[constains.UP] * - \
            1 + self.direction[constains.DOWN]

        snakeHead = [self.headX, self.headY]
        self.tails.append(snakeHead)

        # While the snake is moving, we remove the last tail and add the head
        if len(self.tails) > self.size:
            del self.tails[0]

        self.updateState(foodX, foodY)

    def calculateReward(self, foodX, foodY):
        """ Calculate current score the snake has"""

        # Every apple the snake ate, we give 50 score
        score = (self.size - 1) * 50

        # Give a small score if the snake comes closer to the food
        score += math.sqrt((foodX - self.initHead[0])**2 + (foodY - self.initHead[1])**2) - math.sqrt((foodX - self.headX)**2 + (foodY - self.headY)**2)

        # Minus a large score if the snake is dead
        if self.hasDead:
            score -= 100

        return score
    
    def findObstacle(self, x, y):
        for tail in self.tails[:-1]:
            if tail[0] == x and tail[1] == y:
                return True

        if Snake.hitTheWals(x, y):
            return True

        return False

    def getVision(self, foodX, foodY):
        """ Get snake's vision of the game board and the apple"""

        return [
           self.findObstacle(self.headX - 1, self.headY), # Obstacle is on the Left
           self.findObstacle(self.headX + 1, self.headY), # Obstacle is on the Right
           self.findObstacle(self.headX, self.headY - 1), # Obstacle is on the top
           self.findObstacle(self.headX, self.headY + 1), # Obstacle is on the bottom

           foodX < self.headX, # Apple is on the left
           foodX > self.headX, # Appe is on the right
           foodY < self.headY, # Apple is on the top
           foodY > self.headY, # APple is on the bottom
        ]

    def increaseSize(self):
        self.size += 1

    def hitItself(self):
        head = [self.headX, self.headY]

        for tail in self.tails[:-1]:
            if tail == head:
                return True

        return False

    def hitTheWals(x, y):
        # Break the flow to have a better performance

        hitRightWall = x >= constains.NORMALIZED_WIDTH
        if(hitRightWall):
            return True

        hitLeftWall = x < 0
        if(hitLeftWall):
            return True

        hitTopWall = y >= constains.NORMALIZED_HEIGHT
        if(hitTopWall):
            return True

        hitBottomWall = y < 0
        if(hitBottomWall):
            return True

        # if hitRightWall or hitLeftWall or hitTopWall or hitBottomWall:
        #     return True

        return False

    def hitTheFood(self, foodX, foodY):
        if self.headX == foodX and self.headY == foodY:
            return True

        return False
