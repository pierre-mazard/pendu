# -*- coding: utf-8 -*-
"""
11/12/2023

@author: Mazard Pierre

#                                  Pendu _ Menu du jeu 
"""

import pygame
import sys 


pygame.init()

height, width  = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendu - Menu du jeu")

animation00 = pygame.image.load("images/animation_00.png")
animation01 = pygame.image.load("images/animation_01.png")
animation02 = pygame.image.load("images/animation_02.png")
animation03 = pygame.image.load("images/animation_03.png")
animation04 = pygame.image.load("images/animation_04.png")
animation05 = pygame.image.load("images/animation_05.png")
animation06 = pygame.image.load("images/animation_06.png")

pictures_list = [animation00, animation01, animation02, animation03, animation04, animation05, animation06]
current_picture = 0
animation_delay = 185

clock = pygame.time.Clock()

for i in range(len(pictures_list)):
    pictures_list[i] = pygame.transform.scale(pictures_list[i], (width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(pictures_list[current_picture], (0,0))
    pygame.display.flip()

    current_picture = (current_picture + 1) % len(pictures_list)
    pygame.time.delay(animation_delay)
    clock.tick(60)
