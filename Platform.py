import pygame, os
from pygame.locals import *

class Platform():

	def __init__(self, x, y, orientation, distance):
		self.distance = 1
		self.rect = Rect(x, y)
		self.pauseTime = 40
		self.finalD = distance
		self.start = (self.rect.getX(), self.rect.getY())
		if orientation == 0:
			end_y = self.rect.getY() - distance * 80
			self.end = (self.rect.getX(), end_y)
		if orientation == 1:
			end_y = self.rect.getY() + distance * 80
			self.end = (self.rect.getX(), end_y)
		if orientation == 2:
			end_x = self.rect.getX() - distance * 60
			self.end = (end_x, self.rect.getY())
		if orientation == 3:
			end_x = self.rect.getX() + distance * 60
			self.end = (end_x, self.rect.getY())
		self.orientation = orientation
		path = os.path.dirname(__file__) + r"\Images\Platform.gif"
		self.image = pygame.image.load(path)
		self.image.convert()
	
	def getPosition(self):
		return self.rect.getPosition()

	def toString(self):
		return '4' + str(self.orientation) + str(self.finalD)

	def collide(self, x, y):
		return self.rect.contains(x, y)

	def isAlive(self):
		return True

	def draw(self):
		return self.image
	
	def getX(self):
		return self.rect.getX()

	def getRX(self):
		return self.rect.getRX()

	def pushPlayer(self, player):
		if player.getY() <= self.rect.getBY() and player.isJumping():
			player.fall()
			player.moveY(self.rect.getBY() - player.getY() + 1)
			

		if self.isMoving:
			if self.orientation == 0:
				player.moveUp(self.distance * -1)
			elif self.orientation == 2:
				player.moveX(-1 * self.distance)
			elif self.orientation == 3:
				player.moveX(self.distance)

	def pullPlayer(self, player):
		if self.isMoving:
			if self.orientation == 0:
				player.moveUp(self.distance)
			elif self.orientation == 2:
				player.moveX(self.distance)
			elif self.orientation == 3:
				player.moveX(-1 * self.distance)

	def getY(self):
		return self.rect.getY()

	def tick(self, player):
		if self.rect.getX() != self.end[0] or self.rect.getY() != self.end[1]:
			self.isMoving = True
			if self.orientation == 0:
				self.rect.moveY(self.distance * -1)
			elif self.orientation == 1:
				self.rect.moveY(self.distance)
			elif self.orientation == 2:
				self.rect.moveX(self.distance * -1)
			elif self.orientation == 3:
				self.rect.moveX(self.distance)
		else:
			if self.pauseTime > 0:
				self.isMoving = False;
				self.pauseTime-=1
			else:
				self.pauseTime = 40
				self.start, self.end = self.end, self.start
				self.orientation ^= 1

	def contains(self, x, y):
		return self.rect.contains(x, y)

	def collide(self, player):
		return not(player.getY() >= self.rect.getBY() or player.getBottom() <= self.rect.getY() or player.getX() >= self.rect.getRX() or player.getRight() <= self.rect.getX())

class Rect:

	def __init__(self, x, y):
		self.leftX = x * 60
		self.rightX = (x + 1) * 60
		self.topY = y * 80
		self.bottomY = (y + 1) * 80
	
	def getPosition(self):
		return (self.leftX, self.topY)

	def contains(self, x, y):
		return self.leftX < x < self.rightX and self.topY < y < self.bottomY 

	def getX(self):
		return self.leftX
	
	def getY(self):
		return self.topY

	def getRX(self):
		return self.rightX

	def getBY(self):
		return self.bottomY

	def moveY(self, distance):
		self.topY += distance
		self.bottomY += distance
	
	def moveX(self, distance):
		self.leftX +=distance
		self.rightX += distance


