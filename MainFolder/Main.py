import os
os.system('cls')

#Library here
import pygame

def display(): #Funtion display
    '''FUNTION DISPLAY'''
    from Player import atribut

    pygame.init()
    dis= pygame.display.set_mode((700, 600))
    color = (43, 191, 254)
    pygame.display.update()
    pygame.display.set_caption('Snake game')

    atribut(dis, color)

#DUMMY
'''
def atribut(dis,bg_color):
    game_over= False
    while not game_over:
        dis.fill(bg_color)
        for event in pygame.event.get():
            #print(event)#prints out all the actions that take place on the screen
            if event.type==pygame.QUIT:
                game_over=True
    
    pygame.quit()
    quit()

#Call Funtion
display()
'''