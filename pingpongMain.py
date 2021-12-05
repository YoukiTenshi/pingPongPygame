import pygame as pg
import pingPongAux as aux

bolaCorrendo = False
pg.init()
tamTela = 700  #screen size
screen = pg.display.set_mode((tamTela, tamTela))  #tamanho da tela
clock = pg.time.Clock()  #refere o fps dps

red = (255, 0, 0)
blue = (130, 150, 255)
dkGreen = (0, 90, 0)

player1 = aux.Player(1, tamTela)
player2 = aux.Player(2, tamTela)
bola = aux.Bola(tamTela)  #ball(screenSize)  (class instance)
bolaCorrendo = True
bola.refTamTela = tamTela
player1.refTamTela = tamTela
player2.refTamTela = tamTela

all_sprites = pg.sprite.Group()  #onde as coisas vão p ser atualizadas e desenhadas / where stuff is updated and drawn
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
	if pg.sprite.collide_rect(bola, player1) or pg.sprite.collide_rect(bola, player2):
		aux.rebaterBolaX(bola)
	all_sprites.draw(screen)
	pg.display.flip()
	
pg.quit()
