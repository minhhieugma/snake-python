
import pygame as pg

import random
import constains

class Snake:
  x = 0
  y = 0
  size = 1
  block = 10
  
  momentumX = 0
  momentumY = 0

  def __init__(self):
    self.x = 0
    self.y = 0
    self.size = 1

  def randomPosition(self):

    self.x = round(random.randrange(0, constains.BOARD_SIZE_WIDTH))
    self.y =  round(random.randrange(0, constains.BOARD_SIZE_HEIGHT))
 
  def move(self):

    self.x += self.momentumX
    self.y += self.momentumY
  
  def changeDirection(self, stepX, stepY):
    self.momentumX = stepX
    self.momentumY = stepY

    self.move()
  
  def moveLeft(self):
     self.changeDirection(-self.block, 0)

  
  def moveRight(self):
     self.changeDirection(self.block, 0)

  
  def moveUp(self):
     self.changeDirection(0, -self.block)


  def moveDown(self):
     self.changeDirection(0, self.block)

  def increaseSize(self):
    self.size += 1

def drawSnake(display, snakeBlock, snakes):
    for snake in snakes:
        pg.draw.rect(display, (0, 0, 0), [snake[0], snake[1], snakeBlock, snakeBlock])