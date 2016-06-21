#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


def main():
    clock = pygame.time.Clock()
    
    pygame.init()
    screen = pygame.display.set_mode((1024, 768), HWSURFACE | DOUBLEBUF | RESIZABLE, 32)
    pygame.display.set_caption('Hello world!')

    background_image = pygame.image.load("item_1.png").convert()
    #background_image = pygame.transform.scale(background_image, (1024, 768))

    _quit = False
    while not _quit:
        for e in pygame.event.get():
            if e.type is QUIT: _quit = True
            if e.type is KEYDOWN and e.key == K_ESCAPE: _quit = True
            if e.type == VIDEORESIZE:
                screen = pygame.display.set_mode(e.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)

        screen.fill((100, 100, 100))

        player_position = pygame.mouse.get_pos()
        screen.blit(background_image, player_position)
        
        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main() 
