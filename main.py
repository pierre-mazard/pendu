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
pygame.mixer.music.set_volume(0.1)


#                       Musique de fond
music = "sounds\epic_dark.mp3"
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)


#                       Bruitage clic start
start_sound = pygame.mixer.Sound("sounds/start.mp3")

#                       Création de la fenêtre
height, width  = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendu - Menu du jeu")


#                       Chargement de l'image du boutton de l'index des mots 
index_des_mots = pygame.image.load("images/index_des_mots.png")

#                       Redimentionnement de l'image de l'index des mots
index_des_mots = pygame.transform.scale(index_des_mots, (75, 100))

#                       Chargement des images de l'animation de la potence 
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

#                       Redimentionnement des images de l'animation de la potence
for i in range(len(pictures_list)):
    pictures_list[i] = pygame.transform.scale(pictures_list[i], (width, height))

#                       Icône du bouton pour lancer la partie 
launch_game_icon = pygame.image.load("images/launch_game.png")

#                       Position du bouton pour lancer la partie
button_launch_x, button_launch_y = 10, 10

#                       Redimentionnement de l'image du bouton pour lancer la partie
launch_game_icon = pygame.transform.scale(launch_game_icon, (210, 125))
 
#                       Icônes du bouton mute
speaker_on_icon_00 = pygame.image.load("images/speaker_on_00.png")
speaker_on_icon_01 = pygame.image.load("images/speaker_on_01.png")
speaker_on_icon_02 = pygame.image.load("images/speaker_on_02.png")
speaker_on_icon_03 = pygame.image.load("images/speaker_on_03.png")
speaker_on_icon_04 = pygame.image.load("images/speaker_on_04.png")
speaker_on_icon_05 = pygame.image.load("images/speaker_on_05.png")
speaker_off_icon = pygame.image.load("images\speaker_off.png")

speaker_on_images = [speaker_on_icon_00, speaker_on_icon_01, speaker_on_icon_02, speaker_on_icon_03, speaker_on_icon_04, speaker_on_icon_05]
current_image_index = 0
#                       Position du bouton mute
image_width = speaker_on_images[0].get_width()
image_height = speaker_on_images[0].get_height()
button_x, button_y = width - image_width - 35, 5

#                       Etat de la musique activée 
music_on = True

#                       Boucle principale 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
#                        Vérification du clic sur le bouton de mute
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x <= mouse_x <= button_x + image_width and \
                    button_y <= mouse_y <= button_y + image_height :
                music_on = not music_on
                if music_on:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
#                       Vérification du clic sur le bouton start et chargement du module correspondant.             
            elif button_launch_x <= mouse_x <= button_launch_x + 210 and \
               button_launch_y <= mouse_y <= button_launch_y + 125:
                #                       Jouer le son du boutton
                start_sound.play()
                from game import game
                game.py

#                       Affichage de l'animation de la potence    
    screen.blit(pictures_list[current_picture], (0,0))
    
#                       Affichage du bouton mute
    if music_on:
        screen.blit(speaker_on_images[current_image_index], (button_x, button_y))
    else:
        screen.blit(speaker_off_icon, (button_x, button_y))  
 
#                       Affichage du boutton pour lancer la partie
    screen.blit(launch_game_icon, (button_launch_x, button_launch_y))    
    
    

#                       Affichage du boutton de l'index des mots 
    screen.blit(index_des_mots, (300, 15))

    pygame.display.flip()    
#                       Annimations
    current_image_index = (current_image_index + 1) % len(speaker_on_images)
    current_picture = (current_picture + 1) % len(pictures_list)
    pygame.time.delay(animation_delay)
    clock.tick(60)
