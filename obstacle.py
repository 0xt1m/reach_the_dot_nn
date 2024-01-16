import pygame
import properties as props

from utils import Point, Segment

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


	def get_segments(self):
		top_left = Point(self.x, self.y)
		top_right = Point(self.x + self.width, self.y)
		bottom_left = Point(self.x, self.y + self.height)
		bottom_right = Point(self.x + self.width, self.y + self.height)

		segment_a = Segment(top_left, top_right)
		segment_b = Segment(top_left, bottom_left)
		segment_c = Segment(bottom_left, bottom_right)
		segment_d = Segment(bottom_right, top_right)

		return (segment_a, segment_b, segment_c, segment_d)