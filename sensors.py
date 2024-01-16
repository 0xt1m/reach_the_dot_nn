import numpy as np
import pygame
import math
import properties as props

from utils import Point, lerp, get_intersection, draw_dot

class Sensors:
	def __init__(self, dot, count=12):
		self.dot = dot

		self.ray_count = count
		self.ray_length = 100
		self.ray_spread = 2*math.pi

		self.ray_width = 3

		self.rays = []


	def update(self, obstacles):
		self.rays = []

		for i in range(self.ray_count):
			# ray_angle = utils.lerp(self.ray_spread/2, -self.ray_spread/2, i/(self.ray_count-1))
			ray_angle = i * self.ray_spread / self.ray_count

			start = Point(self.dot.x, self.dot.y)
			end = Point(self.dot.x - math.sin(ray_angle) * self.ray_length, self.dot.y - math.cos(ray_angle) * self.ray_length)

			intersections = []
			for obs in obstacles:
				segments = obs.get_segments()
				for seg in segments:
					intersection = get_intersection(start, end, seg.start, seg.end)
					if intersection:
						intersections.append(intersection)

			self.rays.append((start, end, intersections))



	def show(self, screen):
		for ray in self.rays:
			pygame.draw.line(self.dot.screen, props.COLORS["yellow"], (ray[0].x, ray[0].y), (ray[1].x, ray[1].y), width=self.ray_width)
			for intr in ray[2]:
				draw_dot(screen, intr)
