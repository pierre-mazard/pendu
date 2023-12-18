# -*- coding: utf-8 -*-
"""
12/12/2023

@author: Mazard Pierre

#                                  Pendu _ Partie lancée ! 
"""


#                       Importation des fonctions externes 
import pygame
import sys 
from random import choice
#                       Initialisations
pygame.init()
pygame.mixer.init()


#                       Musique de fond
music = "game/sounds/just_relax.mp3"
pygame.mixer.music.load(music)

pygame.mixer.music.play(-1)

#                       Création de la fenêtre
height, width  = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pendu                                                      Partie lancée !")



#                       Chargement des images de la potence 
potence00 = pygame.image.load("game/images/potence_00.png")
potence01 = pygame.image.load("game/images/potence_01.png")
potence02 = pygame.image.load("game/images/potence_02.png")
potence03 = pygame.image.load("game/images/potence_03.png")
potence04 = pygame.image.load("game/images/potence_04.png")
potence05 = pygame.image.load("game/images/potence_05.png")
potence06 = pygame.image.load("game/images/potence_06.png")



current_picture = 0
animation_delay = 185 # Vitesse de transitions des images en millisecondes

clock = pygame.time.Clock()

#                       Redimentionnement des images de la potence

potence00 = pygame.transform.scale(potence00, (width, height))


#                       Création de la police
font = pygame.font.Font(None, 36)

#                       Chargement des mots depuis un fichier
def choisir_mot():
    with open('mots.txt', 'r', encoding='utf8') as f:
        mots = f.readlines()
    return choice(mots).strip().upper()

#                       Implémentation du jeu du pendu
def jeu_du_pendu():
    while True:
        mot_a_deviner = choisir_mot()
        mot_masque = '_ ' * len(mot_a_deviner)
        tentatives_restantes = 10

        while '_' in mot_masque and tentatives_restantes > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                        lettre = chr(event.key).upper()

                        if lettre in mot_a_deviner:
                            for i, char in enumerate(mot_a_deviner):
                                if char == lettre:
                                    mot_masque = mot_masque[:i] + lettre + mot_masque[i+1:]
                        else:
                            tentatives_restantes -= 1
            #                       Affichage de la potence    
            screen.blit(potence00, (0,0))
            message_mot = f"Mot à deviner: {mot_masque}"
            message_tentatives = f"Tentatives restantes: {tentatives_restantes}"
            text_surface_mot = font.render(message_mot, True, (150, 150, 150))
            text_surface_tentatives = font.render(message_tentatives, True, (150, 150, 150))
            screen.blit(text_surface_mot, (10, 10))
            screen.blit(text_surface_tentatives, (10, 50))
            pygame.display.flip()  # Met à jour l'affichage

        if '_' not in mot_masque:
            message_gagne = f"Félicitations! Vous avez deviné le mot: {mot_a_deviner}"
            text_surface_gagne = font.render(message_gagne, True, (0, 150, 0))
            screen.blit(text_surface_gagne, (10, 100))
        else:
            message_perdu = f"Dommage! Le mot était: {mot_a_deviner}"
            text_surface_perdu = font.render(message_perdu, True, (150, 1, 0))
            screen.blit(text_surface_perdu, (10, 100))
            pygame.display.flip()  # Met à jour l'affichage
            pygame.time.delay(2000)  # Attend avant de quitter

        pygame.display.flip()  # Met à jour l'affichage
        pygame.time.delay(2000)  # Attend avant de recommencer    

#                       Icônes du bouton mute
speaker_on_icon_00 = pygame.image.load("images/speaker_on_00.png")
speaker_on_icon_01 = pygame.image.load("images/speaker_on_01.png")
speaker_on_icon_02 = pygame.image.load("images/speaker_on_02.png")
speaker_on_icon_03 = pygame.image.load("images/speaker_on_03.png")
speaker_on_icon_04 = pygame.image.load("images/speaker_on_04.png")
speaker_on_icon_05 = pygame.image.load("images/speaker_on_05.png")
speaker_off_icon = pygame.image.load("images/speaker_off.png")

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
                

    
#                       Affichage du bouton mute
    if music_on:
        screen.blit(speaker_on_images[current_image_index], (button_x, button_y))
    else:
        screen.blit(speaker_off_icon, (button_x, button_y))  
     
    jeu_du_pendu()


    current_image_index = (current_image_index + 1) % len(speaker_on_images)
    pygame.time.delay(animation_delay)
    clock.tick(60)
    pygame.display.flip()