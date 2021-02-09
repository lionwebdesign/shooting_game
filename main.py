import pygame, sys, random

#Configuración inicial
pygame.init()
screen_width = 1024
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#imagenes
madera_bg = pygame.image.load("shooting_game/media/Wood_BG.png")
piso_bg = pygame.image.load("shooting_game/media/Land_BG.png")
agua_bg = pygame.image.load("shooting_game/media/Water_BG.png")
nube_1 = pygame.image.load("shooting_game/media/Cloud1.png")
nube_2 = pygame.image.load("shooting_game/media/Cloud2.png")
mira = pygame.image.load("shooting_game/media/crosshair.png")
patos = pygame.image.load("shooting_game/media/duck.png")

#Animacion de escenario
posicion_piso_y = 450
velocidad_piso = 1
posicion_agua_y = 475
velocidad_agua = 2

patos_list = []
for pato in range(20):
    posicion_patos_x = random.randrange(75, 975)
    posicion_patos_y = random.randrange(50, 500)
    patos_rect = patos.get_rect(center = (posicion_patos_x, posicion_patos_y))
    patos_list.append(patos_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mira_rect = mira.get_rect(center = event.pos)

    screen.blit(madera_bg,(0, 0))

    posicion_piso_y -= velocidad_piso
    if posicion_piso_y <= 425 or posicion_piso_y >= 490:
        velocidad_piso *= -1
    screen.blit(piso_bg,(0, posicion_piso_y))

    for patos_rect in patos_list:
        screen.blit(patos, patos_rect)

    posicion_agua_y -= velocidad_agua 
    if posicion_agua_y <= 470 or posicion_agua_y >= 510:
        velocidad_agua *= -1
    screen.blit(agua_bg,(0, posicion_agua_y))

    screen.blit(nube_1,(0,0))
    screen.blit(nube_2,(150,screen_height/6))
    screen.blit(nube_1,(screen_width/2,100))
    screen.blit(nube_2,(700,0))

    screen.blit(mira, mira_rect)

    pygame.display.update()
    clock.tick(60)