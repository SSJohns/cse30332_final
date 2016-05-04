#Nathan Kowaleski
#Shaquille Johnson
#Final Project
#4/4/16
#gamestate.py

import math
import json
import sys
import os
import pygame
from pygame.locals import *
import spritesheet

enemies = []

def sprite_sheet_load(colorKey, spriteLocX, spriteLocY, spriteSizeX, spriteSizeY, fileName):
    '''Purpose: to extract a sprite from a sprite sheet at the chosen location'''
    '''credit to Stackover flow user hammyThePig for original code'''

    sheet = pygame.image.load(fileName).convert() #loads up the sprite sheet. convert makes sure the pixel format is coherent
    sheet.set_colorkey(colorKey) #sets the color key

    sprite = sheet.subsurface(pygame.Rect(spriteLocX, spriteLocY, spriteSizeX, spriteSizeY)) #grabs the sprite at this location

    return sprite


class Player(pygame.sprite.Sprite):
	def __init__(self, gs,cliFac):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.cliFac = cliFac
		ss = spritesheet.spritesheet("./media/frog.png")
		self.image = ss.image_at((0,0,24,24),(0,0,0))		
		self.images = []
		self.rect = self.image.get_rect()
		self.rect.centerx = 100.0
		self.rect.centery = 100.0

		spriteXLoc = 0 #starting x location for the sprite
		spriteYLoc = 0 #starting y location for the sprite
		spriteXSize = 38
		spriteYSize = 35

		#Grab the images for the main character's walking poses
		#for y in range(0,2): #handle the columns of sprite sheet
		#	for x in range(0,10): #handle the rows of sprite sheet
		#		print spriteXLoc, spriteYLoc, spriteXSize,spriteYSize
		#		self.images.append(sprite_sheet_load((0,0,0), spriteXLoc, spriteYLoc, spriteXSize, spriteYSize, "./media/frog.png"))
		#		spriteXLoc += spriteXSize
		#		spriteXLoc = 0 #reset the inital x value
		#		spriteYLoc += spriteYSize #increment the y value

	def tick(self):
		# get the mouse x and y position on the screen
		for event in pygame.event.get():
			# determin if X was clicked, or Ctrl+W or Alt+F4 was used
			if event.type == pygame.QUIT:
				return
			else:
				pass
		pressed = pygame.key.get_pressed()
		#self.image = self.rot_center(self.orig_image, 315 - 180*math.atan2(y, x)/math.pi)
		if pressed[pygame.K_w]:
			self.rect.y -= 5
			#self.image = self.images[13]
   		elif pressed[pygame.K_s]:
			self.rect.y += 5
			#self.image = self.images[13]
		elif pressed[pygame.K_a]:
			self.rect.x -= 5
			#self.image = self.images[31]
    		elif pressed[pygame.K_d]:
			self.rect.x += 5
		self.cliFac.transport.getHandle().sendall(json.dumps({
						"x":self.rect.x,
						"y":self.rect.y}) + "\r\n")


class Enemy(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		ss = spritesheet.spritesheet("./media/frog.png")
		self.image = ss.image_at((0,0,24,24),(0,0,0))		
		self.images = []
		self.rect = self.image.get_rect()
		self.rect.centerx = 100.0
		self.rect.centery = 100.0
		self.x = 0
		self.y = 0

		spriteXLoc = 0 #starting x location for the sprite
		spriteYLoc = 0 #starting y location for the sprite
		spriteXSize = 38
		spriteYSize = 35

	def tick(self):
		self.rect.y = self.x
		self.rect.x = self.y
		#self.image = self.images[31]
		# code to calculate the angle between my current
		# direction and the mouse position (see math.atan2)
		# ... use this angle to rotate the image so that it
		# faces the mouse



class GameSpace: 
	#def enemyUpdate(self,data):
	#	self.enemies[int(data['id'])]
	def newEnemy(self,name):
		name = Enemy()
		enemies.append(name)
	def main(self,cliFac):
		pygame.init()
		bg = pygame.image.load("./media/6657.png")
		self.size = self.width, self.height = 480, 360
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)
		self.clock = pygame.time.Clock()
		self.player = Player(self,cliFac)

		opening = pygame.image.load("./media/Frogger.jpg")

		i = 255
		while i > 0:
			self.screen.fill(self.black)
			opening = pygame.image.load("./media/Frogger.jpg")
			opening.set_alpha(i)
			logoimage = self.screen.blit(opening,(60,self.height/2 - 90))
			pygame.display.flip()
			pygame.display.update()
			pygame.time.wait(60)
			i = i-5

		while 1:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == QUIT:
					return
			self.player.tick()
			self.screen.fill(self.black)
			self.screen.blit(bg, (0,0))
			for enemy in enemies:
				enemy.tick()
				self.screen.blit(enemy.image, enemy.rect)
			self.screen.blit(self.player.image, self.player.rect)
			pygame.display.flip()
			pygame.display.update()


