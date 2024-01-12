import pygame
import properties as props

class Obstacle:
	def __init__(self, screen, x, y, width, height):
		self.screen = screen

		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x, y, width, height)

		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


	def show(self):
		pygame.draw.rect(self.screen, props.COLORS["red"], self.rect)