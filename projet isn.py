# Créé par mromme, le 10/03/2017 en Python 3.4
import pygame
from pygame.locals import *
from mouvement import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))



#fond
fond = pygame.image.load("fond.gif").convert()
fenetre.blit(fond, (0,0))

#personnage
perso = pygame.image.load("fantome.gif").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()


#boucle principale
continuer = 1
while continuer:
    accueil = pygame.image.load("image_accueil.jpg").convert()
    fenetre.blit(accueil, (0,0))

    pygame.display.flip()

    continuer_jeu = 1
    continuer_accueil = 1


    while continuer_accueil:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0

#Boucle de jeu
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer_jeu = 0
            continuer = 0

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer_jeu = 0
            if event.key == K_RIGHT:
                position_perso = position_perso.move(10,0)
                perso = pygame.image.load("fantome d.gif").convert_alpha()
            if event.key == K_LEFT:
                position_perso = position_perso.move(-10,0)
                perso = pygame.image.load("fantome g.gif").convert_alpha()
            if event.key == K_UP:
                position_perso = position_perso.move(0,-10)
                perso = pygame.image.load("fantome h.gif").convert_alpha()
            if event.key ==K_DOWN:
                position_perso = position_perso.move(0,10)
                perso = pygame.image.load("fantome b.gif").convert_alpha()


    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)

    pygame.display.flip()


