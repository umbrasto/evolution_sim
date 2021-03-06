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
    number_of_animals = 12 #multiple de 4 sinn le plus proche du bas pris until fixed
    number_of_food_pieces = int(1.5*(number_of_animals))
    min_distance_from_food_px = 100
    animal_height = 15
    animal_width = animal_height
    
    #animal needs
    number_food_for_survival = 1
    number_food_for_reproduction = 2

    food_positions = []

    #spawns
    spawn_map = np.zeros((window_x,window_y))                   #spawn map array initialization
    
    
    for i in range (number_of_food_pieces):                     #food spawns
        temp_x = random_coordinate(window_x+1-animal_width,animal_width)
        temp_y = random_coordinate(window_y+1-animal_height,animal_height)
        food_positions.append(temp_x)
        food_positions.append(temp_y)
        spawn_map[temp_x,temp_y]=1
    
    

    animal_start_positions = []
    
    #north side
    for i in range (number_of_animals//4):
         temp_coor = random_coordinate(window_x-animal_width)
         while spawn_map[temp_coor,0] == 2:       #checks no other animal there already
            temp_coor = random_coordinate(window_x-animal_width)
         animal_start_positions.append((temp_coor,0))
         spawn_map[temp_coor:temp_coor+animal_width,0:animal_height] = 2

    #south side
    for i in range (number_of_animals//4):
         temp_coor = random_coordinate(window_x-animal_width)
         while spawn_map[temp_coor,window_y-animal_height] == 2:       #checks no other animal there already
            temp_coor = random_coordinate(window_x-animal_width)
         animal_start_positions.append((temp_coor,window_y-animal_height))
         spawn_map[temp_coor:temp_coor+animal_width,window_y-animal_height:window_y] = 2

    #east side
    for i in range (number_of_animals//4):
         temp_coor = random_coordinate(window_y-animal_height)
         while spawn_map[0, temp_coor] == 2:       #checks no other animal there already
            temp_coor = random_coordinate(window_y-animal_height)
         animal_start_positions.append((0,temp_coor))
         spawn_map[0:0+animal_width, temp_coor:temp_coor+animal_height] = 2

    #west side mf
    for i in range (number_of_animals//4):
         temp_coor = random_coordinate(window_y-animal_height)
         while spawn_map[window_x-animal_width, temp_coor] == 2:       #checks no other animal there already
            temp_coor = random_coordinate(window_y-animal_height)
         animal_start_positions.append((window_x-animal_width,temp_coor))
         spawn_map[window_x-animal_width:window_x,temp_coor:temp_coor+animal_height] = 2

    print(animal_start_positions)
    animal_start_positions_numpy = np.array(animal_start_positions)
    print(animal_start_positions_numpy)
        

        






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
            pygame.draw.rect(win, (255, 119, 255), (food_positions[i], food_positions[i+1], 5, 5))

        for i in range ((number_of_animals//4)*4):
            pygame.draw.rect(win, (0, 0, 0), (animal_start_positions_numpy[i,0], animal_start_positions_numpy[i,1], animal_height, animal_width))
        
        pygame.display.update()
        


















if __name__ == '__main__':
    main()

pygame.quit()
