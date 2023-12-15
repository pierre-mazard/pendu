# -*- coding: utf-8 -*-
"""
15/12/2023

@author: Mazard Pierre

#                                  Pendu _ Index des mots
"""
#                       Importation des fonctions externes 
import pygame
import sys 

#                       Initialisations
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)


#                       Musique de fond
music = "game/sounds/cave.mp3"
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

#                       Création de la fenêtre
height, width  = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendu                              Index des mots")



#                       Chargement des images de la potence 
word_index = pygame.image.load("game/images/magic_library.jpg")
#                       Redimentionnement des images de l'animation

word_index = pygame.transform.scale(word_index, (width, height))


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

animation_delay = 185 # Vitesse de transitions des images en millisecondes

clock = pygame.time.Clock()


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
                    
    pygame.display.flip()
#                       Affichage de l'animation de la potence    
    screen.blit(word_index, (0,0))    
#                       Affichage du bouton mute
    if music_on:
        screen.blit(speaker_on_images[current_image_index], (button_x, button_y))
    else:
        screen.blit(speaker_off_icon, (button_x, button_y))  

#                       Annimations
    current_image_index = (current_image_index + 1) % len(speaker_on_images)
    pygame.time.delay(animation_delay)
    clock.tick(60)