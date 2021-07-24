import random
import constains

class Food:
  x = 0
  y = 0

  # def __init__(self):

  def randomPosition(self):
    self.x = random.randrange(0, constains.NORMALIZED_WIDTH)
    self.y = random.randrange(0, constains.NORMALIZED_HEIGHT)
