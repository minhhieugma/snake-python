import pygame
import constains
import random
from snake import Snake
from food import Food

class Game:
    snake = Snake()
    food = Food()

    def init(self):
        self.snake.init()

        self.snake.randomPosition()
        self.food.randomPosition()

    
    def move(self, moves):
        # LRT
        # Turn Left, Right, Go Straight

        if self.snake.hasDead:
            return

        # ---------------- Game Logic - START ---------------------    
        if not (moves[0] == 0 and moves[1] == 0):
            self.snake.changeDirection(moves[0], moves[1])
        
        self.snake.move()
        self.snake.updateState(self.food.x, self.food.y)

        if self.snake.hasHitApple:
            self.food.randomPosition()
            self.snake.hasHitApple = False

        # ---------------- Game Logic - END ---------------------    