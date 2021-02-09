import pygame, sys

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(madera_bg,(0, 0))
    screen.blit(piso_bg,(0, 450))
    screen.blit(agua_bg,(0, 510))
    
    screen.blit(nube_1,(0,0))
    screen.blit(nube_2,(150,screen_height/6))
    screen.blit(nube_1,(screen_width/2,100))
    screen.blit(nube_2,(700,0))
    pygame.display.update()
    clock.tick(60)