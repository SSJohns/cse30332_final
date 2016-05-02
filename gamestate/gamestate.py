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


class Player(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		#self.image = pygame.image.load("media/something.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = 100.0
		self.rect.centery = 100.0

	def tick(self):
		pass


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
		self.size = self.width, self.height = 640, 640
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)
		self.clock = pygame.time.Clock()
		#self.lasersound = pygame.mixer.Sound("media/something.wav")


		while 1:
			self.clock.tick(60)
			for event in pygame.event.get():
				if event.type == QUIT:
					return


			#tick everything
			self.screen.fill(self.black)
			pygame.display.flip()		


