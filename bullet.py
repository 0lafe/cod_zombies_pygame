import pygame
import os

SIZE_X = 128
SIZE_Y = 128

class bullet():
    def __init__(self, x, y, rotate):
        self.picture = pygame.image.load(os.path.join("assets", "bullet.png")).convert()
        self.picture = pygame.transform.scale(self.picture, (SIZE_X, SIZE_Y))
        self.rect = self.picture.get_rect()
        self.draw_image = pygame.transform.rotate(self.picture, rotate)
        self.rect.x = x
        self.rect.y = y