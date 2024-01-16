import pygame
import properties as props

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Segment:
	def __init__(self, start, end):
		self.start = start
		self.end = end


def lerp(A, B, t):
	return A+(B-A)*t


def get_intersection(A, B, C, D):
	top = (D.x - C.x) * (A.y - C.y) - (D.y - C.y) * (A.x - C.x)
	bottom = (D.y - C.y) * (B.x - A.x) - (D.x - C.x) * (B.y - A.y)
	# top = (D.y - C.y) * (A.x - C.x) - (D.x - C.x) * (A.y - C.y)
	# bottom = (D.x - C.x) * (B.y - A.y) - (D.y - C.y) * (B.x - A.x)

	if bottom != 0:
		t = top/bottom
		if t <= 1 and t >= 0:
			return Point(lerp(A.x, B.x, t), lerp(A.y, B.y, t))

	return 0


def draw_dot(screen, point, radius=13, color=props.COLORS["green"]):
	pygame.draw.circle(screen, color, (point.x, point.y), radius)