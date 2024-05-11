from LightBulb import LightBulb
import pygame


class LightBulbGuiView:
    def __init__(self, lb: LightBulb, screen):
        self.lb = lb
        self.screen = screen
        self.display_on = pygame.image.load("light_on.png")
        self.display_off = pygame.image.load("light_off.png")

    def view(self):
        if self.lb.state:
            self.screen.blit(self.display_on, (150, 0))
        else:
            self.screen.blit(self.display_off, (150, 0))
