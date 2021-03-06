import pygame, os
from pygame.locals import *
class Ladder:

	def __init__(self, x, y):
		pygame.init()
		self.x_location = x
		self.y_location = y
		self.rect = Rect(x, y)
		path = os.path.dirname(__file__) + "\Images\ladder.gif"
		self.image = pygame.image.load(path)
		self.image.convert()

	def draw(self):
		return self.image

	def getX(self):
		return self.rect.getX()

	def getY(self):
		return self.rect.getY()

	def pullPlayer(self, player):
		pass

	def pushPlayer(self, player):
		pass
	def contains(self, x, y):
		return self.rect.contains(x, y)

	def collide(self, player):
		return False

	def toString(self):
		return '3'
	
class Rect:

	def __init__(self, x, y):
		self.leftX = x * 60
		self.rightX = (x + 1) * 60
		self.topY = y * 80
		self.bottomY = (y + 1) * 80

	def contains(self, x, y):
		return self.leftX < x < self.rightX and self.topY <= y <= self.bottomY 

	def getX(self):
		return self.leftX
	
	def getY(self):
		return self.topY

	def getRX(self):
		return self.rightX

	def getBY(self):
		return self.bottomY

