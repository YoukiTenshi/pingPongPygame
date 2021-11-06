import pygame as pg
import random as rd
import math as ma

pg.init()
tamTela = 500  #screen size
screen = pg.display.set_mode((tamTela, tamTela))  #tamanho da tela
clock = pg.time.Clock()  #refere o fps dps

red = (255, 0, 0)
blue = (130, 150, 255)
dkGreen = (0, 90, 0)

class Player(pg.sprite.Sprite):
	def __init__(self, numP, tamTela):
		self.numP = numP
		self.altura = 200  #height
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((12, self.altura))
		self.image.fill(blue)
		self.rect = self.image.get_rect()
		self.speedY = 0
		if numP == 1:
			self.rect.center = (8, 140)  #bota o player ali nas coords / centers player there
		else:
			self.rect.center = (492, 140)  #bota o player ali nas coords

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
		if self.rect.y > tamTela - self.altura:
			self.rect.y = tamTela - self.altura
	
class Bola(pg.sprite.Sprite):  #ball
	def __init__(self, tamTela):  #tamtela = "screen size"
		pg.sprite.Sprite.__init__(self)
		tamBola = 20  #ball size
		self.image = pg.Surface((tamBola, tamBola))
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.speedX = 0
		self.speedY = 0
		self.rect.center = (tamTela/2 - tamBola, tamTela/2 - tamBola)  #bota o player ali nas coords / centers player there
	
	def move(self):
		tamBola = 20  #ball size
		if self.speedX == 0 and self.speedY == 0:
			self.speedX = ma.ceil(6*rd.random() + 3)  # 4 a 9 de velocidade da bolinha / 4 to 9 ball speed
			self.speedY = ma.ceil(6*rd.random() + 3)  # 4 a 9 de velocidade da bolinha
		self.rect.x += self.speedX
		self.rect.y += self.speedY
		if self.rect.x < 0:
			self.rect.x = 0
			self.speedX = -self.speedX
		if self.rect.x > tamTela - tamBola:  #tela = screen, bola = ball, tam = tamanho = size
			self.rect.x = tamTela - tamBola
			self.speedX = -self.speedX
		if self.rect.y < 0:
			self.rect.y = 0
			self.speedY = -self.speedY
		if self.rect.y > tamTela - tamBola:
			self.rect.y = tamTela - tamBola
			self.speedY = -self.speedY
	
all_sprites = pg.sprite.Group()  #onde as coisas vão p ser atualizadas e desenhadas / where stuff is updated and drawn
player1 = Player(1, tamTela)
player2 = Player(2, tamTela)
bola = Bola(tamTela)  #ball(screenSize)  (class instance)
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(bola)

running = True
while running:
	clock.tick(30)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
	all_sprites.update()		
	screen.fill(dkGreen)
	bola.move()
	all_sprites.draw(screen)
	pg.display.flip()
	
pg.quit()
