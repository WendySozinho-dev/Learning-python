import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura=1000
altura=1000

tela=pygame.display.set_mode((largura,altura))


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.Quit()
            exit()
        pygame.display.update()

