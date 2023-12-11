# -*- coding: utf-8 -*-
"""
11/12/2023

@author: Mazard Pierre

#                                  Pendu _ Menu du jeu 
"""
#                       Importation des fonctions externes 
import pygame
import sys 

#                       Initialisations
pygame.init()
pygame.mixer.init()

#                       Musique de fond
music = "sounds/epic_dark.mp3"
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

#                       Création de la fenêtre
height, width  = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendu - Menu du jeu")

#                       Chargement des images de l'animation 
animation00 = pygame.image.load("images/animation_00.png")
animation01 = pygame.image.load("images/animation_01.png")
animation02 = pygame.image.load("images/animation_02.png")
animation03 = pygame.image.load("images/animation_03.png")
animation04 = pygame.image.load("images/animation_04.png")
animation05 = pygame.image.load("images/animation_05.png")
animation06 = pygame.image.load("images/animation_06.png")


pictures_list = [animation00, animation01, animation02, animation03, animation04, animation05, animation06]
current_picture = 0
animation_delay = 185 # Vitesse de transitions des images en millisecondes

clock = pygame.time.Clock()

#                       Redimentionnement des images
for i in range(len(pictures_list)):
    pictures_list[i] = pygame.transform.scale(pictures_list[i], (width, height))

#                       Icônes du bouton mute
speaker_on_icon = pygame.image.load("images/speaker_on.png")
speaker_off_icon = pygame.image.load("images/speaker_off.png")

#                       Position du bouton mute
button_x, button_y = width - speaker_on_icon.get_width() - 10, 10

#                       Etat de la musique activée 
music_on = True

#                       Boucle principale 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérification du clic sur le bouton de mute
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x <= mouse_x <= button_x + speaker_on_icon.get_width() and \
                    button_y <= mouse_y <= button_y + speaker_on_icon.get_height():
                music_on = not music_on
                if music_on:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
    
    screen.blit(pictures_list[current_picture], (0,0))
    
#                       Affichage du bouton mute
    if music_on:
      screen.blit(speaker_on_icon, (button_x, button_y))
    else:
        screen.blit(speaker_off_icon, (button_x, button_y))  
    
    pygame.display.flip()

    current_picture = (current_picture + 1) % len(pictures_list)
    pygame.time.delay(animation_delay)
    clock.tick(60)
