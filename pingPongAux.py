import pygame as pg
import random as rd
import math as ma

red = (255, 0, 0)
blue = (130, 150, 255)
dkGreen = (0, 90, 0)
TamTela = 700

def randBoolSign():
	valor = 32000*rd.random()
	if valor < 16000:
		return -1
	else:
		return 1

class Player(pg.sprite.Sprite):
	global TamTela
	
	def __init__(self, numP, refTamTela):
		self.numP = numP
		self.altura = 200  #height
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((12, self.altura))
		self.image.fill(blue)
		self.rect = self.image.get_rect()
		self.speedY = 0
		if numP == 1:
			self.rect.center = (8, TamTela/2)  #bota o player ali nas coords / centers player there
		else:
			self.rect.center = (TamTela - 8, TamTela/2)  #bota o player ali nas coords

	def update(self):
		self.speedY = 0
		keystate = pg.key.get_pressed()
		if self.numP == 1:
			if keystate[pg.K_w]:
				self.speedY = -8
			if keystate[pg.K_s]:
				self.speedY = 8
		else:
			if keystate[pg.K_UP]:
				self.speedY = -8
			if keystate[pg.K_DOWN]:
				self.speedY = 8
		
		self.rect.y += self.speedY
		if self.rect.y < 0:
			self.rect.y = 0
		if self.rect.y > TamTela - self.altura:
			self.rect.y = TamTela - self.altura
	
class Bola(pg.sprite.Sprite):  #ball
	global TamTela
	
	def __init__(self, TamTela):  #tamtela = "screen size"
		pg.sprite.Sprite.__init__(self)
		tamBola = 20  #ball size
		self.image = pg.Surface((tamBola, tamBola))
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.speedX = 0
		self.speedY = 0
		self.rect.center = (TamTela/2 - tamBola, TamTela/2 - tamBola)  #bota o player ali nas coords / centers player there
	
	def move(self):
		tamBola = 20  #ball size
		if self.speedX == 0 and self.speedY == 0:
			self.speedX = ma.ceil(6*rd.random() + 2) * randBoolSign() # -8 a 8 velocidade X da bolinha / -8 to 8 ball X speed
			self.speedY = ma.ceil(6*rd.random() + 2)  # 4 a 8 de velocidade da bolinha / 4 to 8 ball Y speed
		self.rect.x += self.speedX
		self.rect.y += self.speedY
		if self.rect.x < 0:
			self.rect.x = 0
			#self.speedX = -self.speedX
			self.gol(2)  # pg.sprite.Sprite.kill(self)
		if self.rect.x > TamTela - tamBola:  #tela = screen, bola = ball, tam = tamanho = size
			self.rect.x = TamTela - tamBola
			self.speedX = -self.speedX
			self.gol(1)  # pg.sprite.Sprite.kill(self)
		if self.rect.y < 0:
			self.rect.y = 0
			self.speedY = -self.speedY
		if self.rect.y > TamTela - tamBola:
			self.rect.y = TamTela - tamBola
			self.speedY = -self.speedY
	
def rebaterBolaX(bola):
	global TamTela
	
	bola.speedX = - bola.speedX  #inverte velocidade da bola / revert ball speed
	if 32000*rd.random() < 16000:  # 50% chance:
		if bola.speedX > 0:
			if bola.speedX < 20:
				bola.speedX += 1
		else:
			if bola.speedX > -20:
				bola.speedX -= 1
