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
        self.snake.move(moves, self.food.x, self.food.y)
        
        if self.snake.hasHitApple:
            self.food.randomPosition()
            self.snake.hasHitApple = False

        # ---------------- Game Logic - END ---------------------    