import pygame
import random
import sys

def Uks(x,y, laius, kõrgus, pind, värv):
    punktid=[(x,y),(x,(1/2)*kõrgus),(x+(1/3)*laius,y-(1/2)*kõrgus),(x+(1/3)*laius,y),(x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv, False, punktid, suurus)

def aken(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y),(x,y-kõrgus),(x+laius,y-kõrgus),(x+laius,y),(x,y)]

    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,True,punktid,suurus)

image = pygame.image.load("images.png")

def tara(x, y, laius, kõrgus, ekraan,pind):
    image = pygame.image.load(pind)
    ekraan.blit(image, (x, y))

def Maja(x, y, laius, kõrgus, pind, värv):
    punktid=[(x, y- ((3/4.0)* kõrgus)), (x, y), (x+laius,y),(x+laius,y-(3/4.0)*kõrgus),
             (x,y-((3/4.0)*kõrgus)), (x+laius/2.0,y-kõrgus), (x+laius,y-(3/4.0)*kõrgus)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv, False, punktid, suurus)

    
    Uks(x + 20, y + 1, laius, kõrgus, pind, värv)
    aken(x + laius / 2 + 15, y +(-40), 100, 100, pind, värv)
    tara(x + laius / 2 + 150, y - kõrgus + 220, 40, 40, pind, "images.png")






r=random.randint(0, 255)
g=random.randint(0, 255)
b=random.randint(0, 255)
värv=[r,g,b]

font=[153, 255,150]

r=random.randint(0, 255)
g=random.randint(0, 255)
b=random.randint(0, 255)
majavärv=[r, g, b]




pind=pygame.display.set_mode((640, 480))
pygame.display.set_caption("Juhuslikud onjektid")
pind.fill(font)
Maja(100,400,300,400, pind, majavärv)
()
pygame.display.flip()




for i in range(10):
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)



    värv=[r,g,b]
    laius=random.randint(1, 80)
    kõrgus=random.randint(1, 80)
    
    
    
    x=random.randint(0, 610-laius)
    y=random.randint(0, 450-kõrgus)
    pygame.draw.rect(pind, värv, [x, y, laius, kõrgus])
    pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        sys.exit()
pygame.quit()
