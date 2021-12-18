import numpy as np
import pygame
from pygame.locals import *
import random

def random_coordinate(max, min=0):
    return (random.randint(min, max))



def main(window_x=1000, window_y=750):
    
    ##############################
    #                            #
    #    SIMULATION MATH PART    #
    #                            #
    ##############################


    #scale of sim
    number_of_animals = 10
    number_of_food_pieces = 8
    min_distance_from_food_px = 100
    
    #animal needs
    number_food_for_survival = 1
    number_food_for_reproduction = 2

    food_positions = []

    #spawns
    spawn_map = np.zeros((window_x,window_y))                   #spawn map array initialization
    for i in range (number_of_food_pieces):                     #food spawns
        temp_x = random_coordinate(window_x-4,1)
        temp_y = random_coordinate(window_y-4,1)
        food_positions.append(temp_x)
        food_positions.append(temp_y)
        spawn_map[temp_x,temp_y]=1
    







    ##############################
    #                            #
    #    PYGAME DISPLAY PART     #
    #                            #
    ##############################
    
    pygame.init()

    #window creation
    win_x = window_x
    win_y = window_y
    win = pygame.display.set_mode((win_x, win_y))

    pygame.display.set_caption('sim display')

    #loop
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((255, 255, 255))
        for i in range (0, number_of_food_pieces*2-1, 2):
            pygame.draw.rect(win, (0, 255, 0), (food_positions[i], food_positions[i+1], 5, 5))
        
        pygame.display.update()
        


















if __name__ == '__main__':
    main()

pygame.quit()