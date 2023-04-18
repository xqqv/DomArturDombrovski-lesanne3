import pygame
import random
import sys

def Maja(x, y, laius, kõrgus, pind, värv):
    punktid = [(x, y-((3/4.0)*kõrgus)), (x, y), (x+laius, y), (x+laius, y-((3/4.0)*kõrgus)),
               (x, y-((3/4.0)*kõrgus)), (x+laius/2.0, y-kõrgus), (x+laius, y-((3/4.0)*kõrgus))]
    suurus = random.randint(1, 10)
    pygame.draw.lines(pind, värv, False, punktid, suurus)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


pygame.init()
pind = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Juhuslikud onjektid")

background_color = (153, 255, 150)
pind.fill(background_color)


majavärv = random_color()
Maja(100, 400, 300, 400, pind, majavärv)

pygame.draw.rect(pind, (165, 42, 42), pygame.Rect(297, 217, 100, 180))

pygame.draw.rect(pind, (0, 0, 255), pygame.Rect(187, 197, 60, 60))


for i in range(10):
    värv = random_color()
    laius = random.randint(1, 80)
    kõrgus = random.randint(1, 80)
    x = random.randint(0, 610-laius)
    y = random.randint(0, 450-kõrgus)
    pygame.draw.rect(pind, värv, pygame.Rect(x, y, laius, kõrgus))


pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

