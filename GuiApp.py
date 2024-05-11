from Logic import Logic
from ToggleSwitch import ToggleSwitch
from LightBulb import LightBulb
from ToggleSwitchGuiView import ToggleSwitchGuiView
from LightBulbGuiView import LightBulbGuiView


ts1 = ToggleSwitch()
ts2 = ToggleSwitch()
ts3 = ToggleSwitch()
lb = LightBulb()
logic = Logic(lb, [ts1, ts2, ts3])


import pygame

pygame.init()
pygame.display.set_caption("GUI LightBulb example")
screen = pygame.display.set_mode((500, 400), 0, 32)
white = (255, 255, 255)  # RGB value for white
screen.fill(white)
lbv = LightBulbGuiView(lb, screen)
lbv.view()
tsv1 = ToggleSwitchGuiView(ts1, screen, 140, 250)
tsv2 = ToggleSwitchGuiView(ts2, screen, 220, 250)
tsv3 = ToggleSwitchGuiView(ts3, screen, 300, 250)
tsv1.view()
tsv2.view()
tsv3.view()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            for tsv in [tsv1, tsv2, tsv3]:
                if tsv.area[0] <= x <= tsv.area[2] and tsv.area[1] <= y <= tsv.area[3]:
                    tsv.ts.switch()
                    logic.processing()
                    tsv.view()
                    lbv.view()
                    pygame.display.flip()

        else:
            print(event)


pygame.quit()
