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
import spritesheet

class Player(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		ss = spritesheet.spritesheet("./media/frog.png")
		self.image = ss.image_at((0,0,24,24))		
		self.images = []
		self.rect = self.image.get_rect()
		self.rect.centerx = 100.0
		self.rect.centery = 100.0

	def tick(self):
		# get the mouse x and y position on the screen
		for event in pygame.event.get():
			# determin if X was clicked, or Ctrl+W or Alt+F4 was used
			if event.type == pygame.QUIT:
				return
			else:
				pass

		#orig_rect = self.image.get_rect()
		x = float(mx - self.rect.center[0])
		y = float(my - self.rect.center[1])
		self.image = self.rot_center(self.orig_image, 315 - 180*math.atan2(y, x)/math.pi)
		if pressed[pygame.K_w]:
			self.rect.y -= self.rect.height/50.
			self.image = self.playerImages[self.w%9]
			self.w = self.w + 1
   		elif pressed[pygame.K_s]:
			self.rect.y += self.rect.height/50.
			self.image = self.playerImages[self.s%9+18]
			self.s = self.s + 1
		elif pressed[pygame.K_a]:
			self.rect.x -= self.rect.width/50.
			self.image = self.playerImages[self.a%9+9]
			seld.a = self.a + 1
    		elif pressed[pygame.K_d]:
			self.rect.x += self.rect.width/50.
			self.image = self.playerImages[self.d%9+27]
			self.d = self.d + 1
			# code to calculate the angle between my current
			# direction and the mouse position (see math.atan2)
			# ... use this angle to rotate the image so that it
			# faces the mouse
class Enemy(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		#self.image = pygame.image.load("media/something.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = 640
		self.rect.centery = 640

	def tick(self):
			pass


class GameSpace: 
	def main(self):
		pygame.init()
		bg = pygame.image.load("./media/6657.png")
		self.size = self.width, self.height = 480, 360
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)
		self.clock = pygame.time.Clock()
		#self.lasersound = pygame.mixer.Sound("media/something.wav")
		self.player = Player(self)

		while 1:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == QUIT:
					return

			self.player.tick()
			self.screen.fill(self.black)
			self.screen.blit(bg, (0,0))
			self.screen.blit(self.player.image, self.player.rect)
			pygame.display.flip()
			pygame.display.update()


