import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tema')

clock = pygame.time.Clock()
FPS = 60
BG = (150, 115, 220)

run=True
#primul patrat verticala
x = 100
y = 0
vy = 6

#al doilea patrat orizontala
x2=0
y2=50
vx2=15

#cerc
yc=300
vc=5

#patratul de la marginea ferestrei
x3=0
y3=0
vx3=2
vy3=2
dx=1
dy=0




while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
    #primul patrat vertical
    y += vy
    if y >= 590 or y <= 0:
        vy = -vy

    x2+=vx2
    #al doilea patrat
    if x2>=700 or x2<=0:
        vx2=-vx2

    #patratul de pe marginile ferestrei
    x3+=dx*vx3
    y3+=dy*vy3
    if x3==0 and y3==0:
        dx=1
        dy=0
    elif x3==750 and y3==0:
        dx=0
        dy=1
    elif x3==750 and y3==590:
        dx=-1
        dy=0
    elif x3==0 and y3==590:
        dx=0
        dy=-1

    #cerc mic
    yc+=vc
    if yc>300 or yc<150: vc=-vc

    


    screen.fill(BG)
    #cercuri, dreptunghiuri, linii, imagini, ...
    pygame.draw.rect(screen, (144, 15, 255), (200, y, 50, 50))
    pygame.draw.rect(screen, (144, 15, 255), (x2, 100, 50, 50))
    pygame.draw.circle(screen,(150,25,220),(300,300), 200)
    pygame.draw.circle(screen,(160,100,171),(300,yc), 20)
    pygame.draw.rect(screen, (144, 15, 255), (x3, y3, 50, 50))


    for j in range(0, SCREEN_HEIGHT, SCREEN_HEIGHT // 10):
        pygame.draw.line(screen, (255,255,255), (0, j), (SCREEN_WIDTH, j))


    for i in range(0, SCREEN_WIDTH, SCREEN_WIDTH// 10):
        pygame.draw.line(screen, (255,255,255), (i, 0), (i, SCREEN_HEIGHT))
    
    pygame.display.update()

pygame.quit()