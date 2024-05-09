import pygame
from cuadrado import *
from pygame.locals import *
from EspacioDeJuego import *
pygame.init()

wight=700
height=700
sr=(wight,height)
screen = pygame.display.set_mode(sr)
pygame.display.set_caption("Rompecabezas")
blanco=(255,255,255) 
pos=[20,20]
ta=(50,50)
# cuadro_1=Cudrado(50,50,blanco,screen)
espacio = EspacioDeJuego(150,150,blanco,screen)
while True:
    screen.fill((0, 0, 0))
    espacio.inicio()
    espacio.dib_all()
    espacio.movicion()
    espacio.win(wight,height)
    # espacio.move()
    # cuadro_1.dib()
    pygame.display.flip()