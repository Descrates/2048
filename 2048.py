import pygame
import random
import os, sys
from pygame.locals import *

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
beige = (164, 168, 128)
purple = (75, 0, 130)
lb = (253, 245, 230)
lr = (255, 99, 71)
orange = (255, 165, 0)
yellow = (255, 255, 255)
ly = (255, 255, 51)

y4 = [0, 0, 0, 0]
y3 = [0, 0, 0, 0]
y2 = [0, 0, 0, 0]
y1 = [2, 2, 2, 2]

current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, 'resources')
image_path = os.path.join(resource_path, 'images') #

pygame.init()
size = (760, 760)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("2048 - Python")
pygame.key.set_repeat(1, 1)
font = pygame.font.SysFont("Stencil", 20)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

screen.fill(lb)
while True:
    pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.lines(screen, beige, True, ((175, 0), (175, 760)), 10)
    pygame.draw.lines(screen, beige, True, ((370, 0), (370, 760)), 10)
    pygame.draw.lines(screen, beige, True, ((565, 0), (565, 760)), 10)

    pygame.draw.lines(screen, beige, True, ((0, 175), (760, 175)), 10)
    pygame.draw.lines(screen, beige, True, ((0, 370), (760, 370)), 10)
    pygame.draw.lines(screen, beige, True, ((0, 565), (760, 565)), 10)

    pygame.draw.lines(screen, beige, True, ((3, 3), (760, 3)), 10)
    pygame.draw.lines(screen, beige, True, ((3, 0), (3, 760)), 10)
    pygame.draw.lines(screen, beige, True, ((755, 760), (755, 3)), 10)
    pygame.draw.lines(screen, beige, True, ((0, 755), (755, 755)), 10)



    pygame.display.update()
