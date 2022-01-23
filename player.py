import os
import pygame
from pygame.transform import rotate
import characterFuncs
import bullet

SIZE = 128

class player:
    def __init__(self, width, height):
        self.picture = pygame.image.load(os.path.join("assets", "player.png")).convert()
        self.picture = pygame.transform.scale(self.picture, (SIZE, SIZE))
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.max_width = (width - SIZE)
        self.max_height = (height - SIZE)
        self.move_factor = 4
        self.look = (0, 0)
        self.rect = pygame.Rect(width/2, height/2, SIZE, SIZE)
        self.draw_image = self.picture
        self.rotate = 0

    def key_down(self, event):
        if (event.key == 119):
            self.up = True
        if (event.key == 97):
            self.left = True
        if (event.key == 115):
            self.down = True
        if (event.key == 100):
            self.right = True
        if (event.key == 1073742049):
            self.move_factor *= 3

    def key_up(self, event):
        if (event.key == 119):
            self.up = False
        if (event.key == 97):
            self.left = False
        if (event.key == 115):
            self.down = False
        if (event.key == 100):
            self.right = False
        if (event.key == 1073742049):
            self.move_factor /= 3

    def mouse(self, event):
        self.look = event.pos

    def on_click(self, event):
        shot = bullet.bullet(event.pos[0], event.pos[1], self.rotate_angle)
        return shot

    def update(self):
        if (self.up == True):
            self.rect.y = max(self.rect.y - self.move_factor, 0)
        if (self.left == True):
            self.rect.x = max(self.rect.x - self.move_factor, 0)
        if (self.down == True):
            self.rect.y = min(self.rect.y + self.move_factor, self.max_height)
        if (self.right == True):
            self.rect.x = min(self.rect.x + self.move_factor, self.max_width)
        self.rect_center = self.rect.center
        self.rotate_angle = characterFuncs.rotate(self.rect.center, self.look)
        self.draw_image = pygame.transform.rotate(self.picture, self.rotate_angle)
        self.rect = self.picture.get_rect(center=self.rect_center)
