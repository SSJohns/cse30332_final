#Nathan Kowaleski
#Shaquille Johnson
#Final Project
#4/4/16
#gamestate.py

import math
import sys
import os
import pygame
from pygame.locals import *

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Player(pygame.sprite.Sprite):
	def __init__(self, isred, gs=None,cliFac):
		self.cliFac = cliFac
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.isred = isred
		
		if self.isred == 1:
			self.orig_image = pygame.image.load("./gamestate/media/redturtle.png")
		else:
			self.orig_image = pygame.image.load("./gamestate/media/blueturtle.png")
			
		
		self.image = self.orig_image
		self.rect = self.image.get_rect()
		self.splatimage = pygame.image.load("./gamestate/media/splat.png")
		if self.isred == 1:
			self.rect.centery = 25.0
		else:
			self.rect.centery = 475.0
			
		self.rect.centerx = 250.0
		self.speed = 2
		self.moveup = False
		self.movedown = False
		self.moveright = False
		self.moveleft = False
		self.deg = 0.0
		self.isdead = 0
		self.respawn = 180
		self.hp = 1
		self.key = 0
		self.newdeg = 0.0
		#down, left, right, up
		self.options = { 0 : -1.0,
			1 : 0.0,
			10 : 270.0,
			11 : 315.0,
			100 : 90.0,
			101 : 45.0,
			110 : -1.0,
			111 : 0.0,
			1000: 180.0,
			1001 : -1.0,
			1010 : 225.0,
			1011 : 270.0,
			1100 : 135.0,
			1101 : 90.0,
			1110 : 180.0,
			1111 : -1.0, 
			}

	def rth(self):
		if self.isred == 1:
			self.rect.centery = 25.0
			self.deg = 180.0
			
		else:
			self.rect.centery = 475.0
			self.deg = 0.0
			
		self.rect.centerx = 250.0
		self.isdead = 0
		self.respawn = 180
		self.image = pygame.transform.rotate(self.orig_image, (self.deg))
		self.hp = 1
		self.key = 0
		
	def tick(self):
		if self.isdead == 1:
			self.respawn = self.respawn - 1
			if self.respawn < 0:
				self.rth()
				
				
		elif self.hp < 1:
			self.isdead = 1
			self.image = self.splatimage
			self.speed = 2
				
		elif self.isred == 1 and self.rect.centery > 500:
			self.gs.chimesound.play()
			self.speed += 1
			self.rect.centerx = -200
			self.rect.centery = -200
			self.isdead = 1
			self.gs.redpoints = self.gs.redpoints + 1
		
		elif self.isred == 0 and self.rect.centery < 0:
			self.gs.chimesound.play()
			self.speed +=  1
			self.rect.centerx = -200
			self.rect.centery = -200
			self.isdead = 1
			self.gs.bluepoints = self.gs.bluepoints + 1

		else:
			self.key = 0
			if self.moveup == True:
				self.key = self.key + 1

			if self.movedown == True:
				self.key = self.key + 1000

			if self.moveright == True:
				self.key = self.key + 10

			if self.moveleft == True:
				self.key = self.key + 100
				
			self.newdeg = self.options[self.key]
			if self.newdeg < 0:
				pass
				
			else:
				self.deg = self.newdeg
				self.rect.centery -= self.speed * math.cos(math.radians(self.deg))
				self.rect.centerx -= self.speed * math.sin(math.radians(self.deg))
				
			self.image = pygame.transform.rotate(self.orig_image, (self.deg))
			if self.rect.centerx > 600 or self.rect.centerx < -100 or self.rect.centery > 600 or self.rect.centery < -100:
				self.isdead = 1
				self.gs.splatsound.play()
				self.speed = 2
			
			else:
				for k in self.gs.enemy:
					if self.rect.colliderect(k.rect):
						self.hp -= 1
						self.gs.splatsound.play()
						self.speed = 2
						break
				
				for p in self.gs.players:
					if self.gs.players[p].isred != self.isred and self.rect.colliderect(self.gs.players[p].rect):
						self.hp -= 1
						self.gs.splatsound.play()
						self.speed = 2
						break
						
						
						

class Enemy(pygame.sprite.Sprite):
	def __init__(self, istruck, location, gs=None):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.istruck = istruck
		if self.istruck == 1:
			self.image = pygame.image.load("./gamestate/media/truck.png")
			self.speed = -1
			
		else:
			self.image = pygame.image.load("./gamestate/media/car.png")
			self.speed = 2
			
		self.rect = self.image.get_rect()
		self.rect.centerx, self.rect.centery = location
		
		
	def rth(self):
		if self.istruck == 1:
			self.rect.centerx = 575
			
		else:
			self.rect.centerx = -50


	def tick(self):
			self.rect.centerx += self.speed
			if self.istruck == 1 and self.rect.centerx < -75:
				self.rth()
				
			elif self.istruck == 0 and self.rect.centerx > 550:
				self.rth()
	
class GameSpace:
	def enemyUpdate(self,data):
		for enemy in enemies:
			if enemy['id'] == data['id']:
				enemy['x'] = data['x']
				enemy['y'] = data['y']
	def newEnemy(self,name):
		enemy = Enemy()
		ss = spritesheet.spritesheet("./media/frog.png")
		image = ss.image_at((0,0,24,24),(0,0,0))		
		rect = image.get_rect()
		rect.centerx = 350
		rect.centery = 480-20*(len(enemies))
		enemies.append({
				'id':name,
				'enemy':enemy,
				'x':rect.centerx,
				'y':rect.centery,
				'rect':rect,
				'image':image})
	def main(self,factory):
		self.numberofplayers = 1
		pygame.init()
		self.redpoints = 0
		self.bluepoints = 0
		self.redfont = pygame.font.Font(None, 36)
		self.bluefont = pygame.font.Font(None, 36)
		self.bg = Background('./gamestate/media/bg.png', [0,0])
		self.size = self.width, self.height = 500, 500
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)
		self.clock = pygame.time.Clock()
		self.player = Player(0, self, cliFac)
		self.enemy = []
		self.players = {}
		self.splatsound = pygame.mixer.Sound("./gamestate/media/splat.wav")
		self.chimesound = pygame.mixer.Sound("./gamestate/media/chime.wav")
		self.enemy.append(Enemy(1, [500,175], self))
		self.enemy.append(Enemy(1, [250,275], self))
		self.enemy.append(Enemy(1, [375,375], self))
		self.enemy.append(Enemy(0, [124,125], self))
		self.enemy.append(Enemy(0, [250, 225], self))
		self.enemy.append(Enemy(0, [0,325], self))
		self.playerid = self.numberofplayers
		self.players[ self.playerid ] = Player(self.playerid % 2, self) 
		self.numberofplayers += 1

		while 1:
			self.clock.tick(60)
			if (pygame.key.get_pressed()[pygame.K_UP] != 0 or pygame.key.get_pressed()[pygame.K_w] != 0):
				self.players[self.playerid].moveup = True
			
			else :
				self.players[self.playerid].moveup = False

			if (pygame.key.get_pressed()[pygame.K_DOWN] != 0 or pygame.key.get_pressed()[pygame.K_s] != 0):
				self.players[self.playerid].movedown = True

			else:
				self.players[self.playerid].movedown = False

			if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0 or pygame.key.get_pressed()[pygame.K_d] != 0):
				self.players[self.playerid].moveright = True

			else:
				self.players[self.playerid].moveright = False
			
			if (pygame.key.get_pressed()[pygame.K_LEFT] != 0 or pygame.key.get_pressed()[pygame.K_a] != 0):
				self.players[self.playerid].moveleft = True

			else:
				self.players[self.playerid].moveleft = False

			for event in pygame.event.get():
				if event.type == QUIT:
					return
			


			for m in self.players:
				self.players[m].tick()
				
			for i in self.enemy:
				i.tick()	

			self.screen.fill(self.black)
			self.screen.blit(self.bg.image, self.bg.rect)
			for n in self.players:
				self.screen.blit(self.players[n].image, self.players[n].rect)
				
			for j in self.enemy:
				self.screen.blit(j.image, j.rect)	
				
			self.redtext = self.redfont.render(str(self.redpoints), 1, (250, 50, 50))
			self.redtextpos = self.redtext.get_rect()
			self.redtextpos.right = 475
			self.redtextpos.top = 25	
			self.screen.blit(self.redtext, self.redtextpos)
		
			self.bluetext = self.bluefont.render(str(self.bluepoints), 1, (150, 150, 255))
			self.bluetextpos = self.redtext.get_rect()
			self.bluetextpos.right = 475
			self.bluetextpos.top = 425	
			self.screen.blit(self.bluetext, self.bluetextpos)
		
		
			pygame.display.flip()		



if __name__ == '__main__':
	mygs = GameSpace()
	mygs.main()


