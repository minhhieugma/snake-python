import random
import constains

class Food:
  x = 0
  y = 0

  # def __init__(self):

  def randomPosition(self, snakeBlock):
    self.x  = round(random.randrange(0, constains.BOARD_SIZE_WIDTH - constains.CELL_SIZE) / constains.CELL_SIZE) * constains.CELL_SIZE
    self.y = round(random.randrange(0, constains.BOARD_SIZE_HEIGHT - constains.CELL_SIZE) / constains.CELL_SIZE) * constains.CELL_SIZE
