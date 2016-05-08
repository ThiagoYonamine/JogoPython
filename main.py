import pygame, sys, random,glob
from Virus import Virus

class Wall():
    #Declara atributos da classe
    def __init__ (self,vel):
        self.y = 400
        self.x = random.randint(500, 1500)
        self.velocidade = vel
        self.img = pygame.image.load('wall.png')


    def desenha(self):
        self.x -= self.velocidade
        self.col = pygame.Rect(self.x, self.y, 40, 60)##arrumar o tamanho certo
        display.blit(self.img, (self.x, self.y))

####se pa herança
### cenario pode ter uma lista de walls
class Cenario():
    #Declara atributos da classe
    def __init__ (self):
        self.y = 0
        self.x = 0
        self.velocidade = 6
        self.img = pygame.image.load('background.png')
        self.listWalls = []

    def desenha(self):
        self.x -= self.velocidade
        display.blit(self.img, (self.x, self.y))
        if(self.x <= 500-800): # recomeça o background
            self.x=0

    def criaWalls(self):
        for i in range(2):
            self.listWalls.append(Wall(cenario.velocidade))


pygame.init()
pygame.font.init()
mainClock = pygame.time.Clock()
display = pygame.display.set_mode((500,600)) ## mudar de acordo com a img certa. ps 1ª ser +- 1/3 da img
pygame.display.set_caption('Jogo')

virus = Virus()
cenario = Cenario()
cenario.criaWalls()
#################apenas um teste, colocar uma lista de walls no cenario, mudar desenha do cenario para desenhar walls tbm###
#git
###########################################################################################################################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    cenario.desenha()
    #####################colocar no desenha do cenario########################3
    for i in range(len(cenario.listWalls)):
        cenario.listWalls[i].desenha()

    ################achar um lugar pra iss0 -_-##############################
    w=0
    while(w < len(cenario.listWalls)):
        if (cenario.listWalls[w].x < -20):
            cenario.listWalls.remove(cenario.listWalls[w])
            #w -=1

        elif ((virus.col.colliderect(cenario.listWalls[w].col))):
            cenario.listWalls.remove(cenario.listWalls[w])

        w +=1

    if (len(cenario.listWalls) < 2):
        cenario.listWalls.append(Wall(cenario.velocidade))
    ################################################
    virus.desenha(display)
    virus.pula()
    pygame.display.update()
    mainClock.tick(40)
