import pygame
from pygame.locals import *
import logic 
import player

FPS = 60
WHITE = (255, 255, 255)
 
class App(logic.CEvent):
    def __init__(self, width, height):
        self._running = True
        self._display_surf = None
        self.width = width
        self.height = height
        self._clock = pygame.time.Clock()
        self.sprites = {}

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        self._running = True
        self.player = player.player(self.width, self.height)
        self.sprites["player"] = self.player

    def on_key_down(self, event):
        self.player.key_down(event)

    def on_key_up(self, event):
        self.player.key_up(event)

    def on_mouse_move(self, event):
        self.player.mouse(event)

    def on_mbutton_down(self, event):
        self.sprites["bullet"] = self.player.on_click(event)
 
    def on_loop(self):
        self.player.update()

    def on_render(self):
        self._display_surf.fill(WHITE)
        for sprite in self.sprites.keys():
            self._display_surf.blit(self.sprites[sprite].draw_image, self.sprites[sprite].rect)
        pygame.display.flip()

        
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
            
 
        while( self._running ):
            self._clock.tick(FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()