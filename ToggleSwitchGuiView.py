from ToggleSwitch import ToggleSwitch
import pygame


class ToggleSwitchGuiView:
    def __init__(self, ts: ToggleSwitch, screen: pygame.Surface, x: int, y: int):
        self.ts = ts
        self.screen = screen
        self.turn_off = pygame.image.load("toggle_switch_off.png")
        self.turn_on = pygame.image.load("toggle_switch_on.png")
        self.x = x
        self.y = y
        width, height = self.turn_off.get_size()
        self.area = (x, y, x + width, y + height)

    def view(self):
        if self.ts.state:
            self.screen.blit(self.turn_on, (self.x, self.y))
            width, height = self.turn_on.get_size()
            self.area = (self.x, self.y, self.x + width, self.y + height)
        else:
            self.screen.blit(self.turn_off, (self.x, self.y))
            width, height = self.turn_off.get_size()
            self.area = (self.x, self.y, self.x + width, self.y + height)
