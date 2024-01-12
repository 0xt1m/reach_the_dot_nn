import numpy as np
import pygame
import math
import utils
import properties as props

class Sensors:
	def __init__(self, dot, count=8):
		self.dot = dot

		self.ray_count = 8
		self.ray_length = 100
		self.ray_spread = 2*math.pi

		self.ray_width = 3

		self.rays = []


	def update(self):
		self.rays = []

		for i in range(self.ray_count):
			# ray_angle = utils.lerp(self.ray_spread/2, -self.ray_spread/2, i/(self.ray_count-1))
			ray_angle = i * self.ray_spread / self.ray_count

			start = (self.dot.x, self.dot.y)
			end = (self.dot.x - math.sin(ray_angle) * self.ray_length, self.dot.y - math.cos(ray_angle) * self.ray_length)

			self.rays.append((start, end))



	def show(self):
		for ray in self.rays:
			pygame.draw.line(self.dot.screen, props.COLORS["yellow"], ray[0], ray[1], width=self.ray_width)
