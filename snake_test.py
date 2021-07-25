import unittest
from snake import Snake
import operator
import json

class SnakeTest(unittest.TestCase):

    def test_getVision1(self):
        snake = Snake()
        snake.headX = 10
        snake.headY = 10
        vision = snake.getVision(15, 15)
        
        self.assertListEqual(vision, [0, 0, 0, 0, 
                                        0, 1, 0, 1])

    def test_getVision2(self):
        snake = Snake()
        snake.headX = 0
        snake.headY = 0
        vision = snake.getVision(15, 15)
        
        self.assertListEqual(vision, [1, 0, 1, 0, 
                                        0, 1, 0, 1])

    def test_getVision3(self):
        snake = Snake()
        snake.headX = 0
        snake.headY = 0
        vision = snake.getVision(0, 15)
        
        self.assertListEqual(vision, [1, 0, 1, 0, 
                                        0, 0, 0, 1])

    def test_getVision4(self):
        snake = Snake()
        snake.headX = 0
        snake.headY = 20
        vision = snake.getVision(0, 15)
        
        self.assertListEqual(vision, [1, 0, 0, 0, 
                                        0, 0, 1, 0])



    def test_calculateReward1(self):
        snake = Snake()
        snake.size = 5
        snake.headX = 10
        snake.headY = 10
        snake.initHead = (10, 10)

        reward = snake.calculateReward(10, 15)
        
        self.assertEquals(reward, 200)

    def test_calculateReward2(self):
        snake = Snake()
        snake.size = 5
        snake.headX = 10
        snake.headY = 10
        snake.initHead = (10, 10)
        snake.hasDead =  True

        reward = snake.calculateReward(10, 15)
        
        self.assertEquals(reward, 100)


if __name__ == '__main__':
    unittest.main()