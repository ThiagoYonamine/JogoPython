import pygame

class Sons():
    #Declara atributos da classe
    def __init__ (self):
        self.back = pygame.mixer.music.load("MusicaJogo.mp3")
        self.coin = pygame.mixer.Sound('smw_coin.wav')
        self.dano = pygame.mixer.Sound('damage.wav')

    def playBack(self):
        pygame.mixer.music.play(loops=-1)

    def coinSound(self):
        self.coin.play()

    def danoSound(self):
        self.dano.play()