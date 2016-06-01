import pygame, sys, random,glob
from Virus import Virus
from Menu import Menu
from Upgrade import Upgrade
from Cenario import Cenario

##alguns metodos sei la de quem
def checkColisao(obj, virus):
    w = 0
    while (w < len(obj)):
        if ((virus.col.colliderect(obj[w].col))):

            if(obj[w].tipo == 'wall'):
                virus.vida -= 1

            if(obj[w].tipo == 'antivirus'):
                if ((obj[w].y >= virus.y + 20  or virus.velPulo > 0) and virus.estado == "dash"):
                    virus.velPulo = -20
                    virus.score +=10
                    virus.estado = "pulando"
                    virus.dinheiro += 5
                else:
                    virus.vida -= 1
            if(obj[w].tipo == 'moeda'):
                virus.dinheiro += 1
            obj.remove(obj[w])
        w += 1

def jogo():
    cenario.desenha(display)
    cenario.update()
    checkColisao(cenario.listWalls, virus)
    checkColisao(cenario.listMoedas, virus)
    checkColisao(cenario.listAntivirus, virus)
    virus.desenhaEfeito(display)
    virus.desenha(display)

    virus.pula()
    cenario.desenhaFloor(display)
    cenario.controler()

    if(virus.vida <= 0):
        menu.pag = 0

def chamaMenu():
    MousePos = pygame.mouse.get_pos()
    menu.desenha(display)
    if pygame.mouse.get_pressed() == (1, 0, 0) and menu.start.collidepoint(MousePos):
        virus.vida = virus.vidaBase
        virus.score = 0
        menu.pag = 1
        cenario.reset()
    if pygame.mouse.get_pressed() == (1, 0, 0) and menu.upgrade.collidepoint(MousePos):
        menu.pag = 2

def chamaUpgrade():
    MousePos = pygame.mouse.get_pos()
    upgrade.desenha(display,virus)
    if pygame.mouse.get_pressed() == (1, 0, 0) and upgrade.menuBtn.collidepoint(MousePos):
        menu.pag = 0
    if pygame.mouse.get_pressed() == (1, 0, 0) and upgrade.vidaBtn.collidepoint(MousePos):
        virus.vidaBase +=1
    if pygame.mouse.get_pressed() == (1, 0, 0) and upgrade.planarBtn.collidepoint(MousePos):
        virus.unlockPlanar = True
    if pygame.mouse.get_pressed() == (1, 0, 0) and upgrade.puloDuploBtn.collidepoint(MousePos):
        virus.unlockPuloDuplo = True
    if pygame.mouse.get_pressed() == (1, 0, 0) and upgrade.superPesoBtn.collidepoint(MousePos):
        virus.unlockSuperPeso = True

pygame.init()
pygame.font.init()
mainClock = pygame.time.Clock()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jogo')

menu = Menu()
upgrade = Upgrade()
virus = Virus()
cenario = Cenario()
cenario.criaWalls()
cenario.criaMoedas()
cenario.criaAntivirus()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if(menu.pag == 0):
        chamaMenu()
    elif(menu.pag == 1):
        jogo()
    else:
        chamaUpgrade()
    pygame.display.update()
    mainClock.tick(40)
