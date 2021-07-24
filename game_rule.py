import pygame
import constains
import random


def drawScore(display, score):
    text = pygame.font.SysFont("arial", 20).render(
        f"Eaten: {score}", True, (255, 128, 128))

    display.blit(text, [15, 15])
