import pygame
from pygame.locals import *

pygame.init()

while(True):
    for event in pygame.event.get():
        if (event.type == KEYDOWN):
            print (event)
            if (event.key == K_KP0):
                print ("numpad 0")
        elif (event.type == KEYUP):
            print("stopping")
            break
