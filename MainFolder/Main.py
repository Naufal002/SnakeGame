import os
os.system('cls')

#Library here
import pygame

def display(): #Funtion display
    '''FUNTION DISPLAY'''
    from Player import atribut

    pygame.init()
    dis=pygame.display.set_mode((700, 600))
    pygame.display.update()
    pygame.display.set_caption('Snake game')

    atribut(dis)