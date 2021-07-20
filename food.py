import random
import constains

class Food:
  x = 0
  y = 0

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def randomPosition(self, snakeBlock):
    self.x  = round(random.randrange(0, constains.BOARD_SIZE_WIDTH - snakeBlock) / 30.0) * 10.0
    self.y = round(random.randrange(0, constains.BOARD_SIZE_HEIGHT - snakeBlock) / 30.0) * 10.0
