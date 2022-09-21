#Library here
from Main import display
import pygame

def atribut(dis):
    '''FUNTION ATRIBUT'''
    game_over= False
    while not game_over:
        for event in pygame.event.get():
            print(event)#prints out all the actions that take place on the screen
            if event.type==pygame.QUIT:
                game_over=True
    
    pygame.quit()
    quit()

display()
