import os
import pygame as pg
import constains

def load_images(folderPath):
  
    imgs = []
    for file in os.listdir(folderPath):
        
        relativePath = folderPath + os.sep + file
        image = pg.image.load(relativePath).convert()
        
        imgs.append(image)

    return imgs

 
def drawText(display, txt, color):
    
    mesg = pg.font.SysFont("arial", 15).render(txt, True, color)
    
    display.blit(mesg, [constains.BOARD_SIZE_WIDTH / 6, constains.BOARD_SIZE_HEIGHT / 3])