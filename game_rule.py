import pygame
import constains
import random

def drawScore(display, score):
    text = pygame.font.SysFont("arial", 20).render(f"Eaten: {score}", True, (255, 128, 128))

    display.blit(text, [15, 15])
 
def isDead(snake, head):
    for i in snake[:-1]:
        if i == head:
            return True
    
    return False

def hitTheWals(snakeX, snakeY):
    hitRightWall = snakeX >= constains.BOARD_SIZE_WIDTH
    hitLeftWall = snakeX < 0
    hitTopWall = snakeY >= constains.BOARD_SIZE_HEIGHT 
    hitBottomWall = snakeY < 0

    if hitRightWall or hitLeftWall or hitTopWall or hitBottomWall:
        return True
    
    return False


def hitTheFood(snakeX, snakeY, foodX, foodY):
    if snakeX == foodX and snakeY == foodY:
        return True

    return False