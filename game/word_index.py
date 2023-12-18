# -*- coding: utf-8 -*-
"""
15/12/2023

@author: Mazard Pierre

#                                  Pendu _ Index des mots
"""
#                       Importation des fonctions externes 
import pygame
import sys 
import os 
from pygame.locals import *
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



#                       Chargement de l'image de fond 
word_index = pygame.image.load("game/images/magic_library.jpg")
#                       Redimentionnement de l'image de fond

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

#                       Zone cliquable 
clickable_area = pygame.Rect((220, 210), (149, 150))
#                       Dessin zone cliquable  
pygame.draw.rect(screen, (255, 0, 0), clickable_area, 2)

#                       Image de la souris
cursor_img = pygame.image.load("game/images/mouse.png").convert_alpha()
cursor_img = pygame.transform.scale(cursor_img, (100, 50))

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Police de caractères
police = pygame.font.Font(None, 16)  # Choisissez la police et la taille souhaitées

# Texte à afficher
texte = "Voici l'index des mots, veuillez cliquer sur la page au milieu du pupitre et inscrire un mot via le terminal."

# Créez une surface pour le texte
texte_surface = police.render(texte, True, noir)

# Obtenez les dimensions du texte
texte_largeur, texte_hauteur = texte_surface.get_size()

# Calculez la position pour centrer le texte en haut de la fenêtre
x_pos = (width - texte_largeur) // 2
y_pos = 10  # Ajustez cette valeur pour définir la hauteur du texte

#                        Vérification si le fichier mots.txt existe
if not os.path.exists("mots.txt"):
#                        Création du fichier s'il n'existe pas
    open("mots.txt", "w").close()


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
#                       Inscription de mots à l'intérieur du fichier mots.txt       
            if clickable_area.collidepoint(mouse_x, mouse_y):
#                       Demander un mot à l'utilisateur
                mot_utilisateur = input("Entrez un mot : ")

#                       Lire le contenu actuel du fichier
                with open("mots.txt", "r") as fichier:
                    mots_contenus = fichier.read().splitlines()

#                       Ajout de mot à la liste (si il n'est pas déjà présent)
                if mot_utilisateur not in mots_contenus:
                    mots_contenus.append(mot_utilisateur)
                    mots_contenus.sort()  # Trie de la liste par ordre alphabétique
                    with open("mots.txt", "w") as fichier:
                        fichier.write("\n".join(mots_contenus) + "\n") 
#                        Lire les mots depuis le fichier "mots.txt"
            with open("mots.txt", "r") as fichier:
                mots = fichier.read().splitlines()
            
#                       Trier les mots par longueur
            mots_tries = sorted(mots, key=len)
            
#                       Écrire les mots triés dans le fichier "mots_classement_longueur"
            with open("mots_classement_longueur.txt", "w") as nouveau_fichier:
                for mot in mots_tries:
                    nouveau_fichier.write(mot + "\n")


#                       Affichage image curseur 
    cursor_img_rect = cursor_img.get_rect() 
    cursor_img_rect.center = pygame.mouse.get_pos()
    screen.blit(cursor_img, cursor_img_rect)
            
    pygame.display.flip()
#                       Affichage de l'image de fond  
    screen.blit(word_index, (0,0))    
#                       Affichage du bouton mute
    if music_on:
        screen.blit(speaker_on_images[current_image_index], (button_x, button_y))
    else:
        screen.blit(speaker_off_icon, (button_x, button_y))  
 # Affichez le texte centré
    screen.blit(texte_surface, (x_pos, y_pos))
#                       Annimations
    current_image_index = (current_image_index + 1) % len(speaker_on_images)
    pygame.time.delay(animation_delay)
    clock.tick(60)
