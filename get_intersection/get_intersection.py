import pygame
import sys

pygame.init()


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


# CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

WIDTH = 600
HEIGHT = 600

FPS = 60


# VARS
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()


A = Point(70, 150)
B = Point(500, 200)
C = Point(60, 300)
D = Point(550, 300)

t = -0.1


# FUNCS
def draw_line(start_point, end_point):
	pygame.draw.line(screen, WHITE, start_point, end_point, width=2)


def draw_dot(point, radius=13, color=GREEN):
	pygame.draw.circle(screen, color, point, radius)


def lerp(A, B, t):
	return A+(B-A)*t


def get_intersection(A, B, C, D):
	top = (D.x - C.x) * (A.y - C.y) - (D.y - C.y) * (A.x - C.x)
	bottom = (D.y - C.y) * (B.x - A.x) - (D.x - C.x) * (B.y - A.y)

	t = top/bottom

	return Point(lerp(A.x, B.x, t), lerp(A.y, B.y, t))


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(BLACK)

	# draw_dot((WIDTH/2, HEIGHT/2))
	draw_line((A.x, A.y), (B.x, B.y))
	draw_line((C.x, C.y), (D.x, D.y))


	# dot_x = lerp(A.x, B.x, t)
	# dot_y = lerp(A.y, B.y, t)
	# draw_dot((dot_x, dot_y))

	intersection = get_intersection(A, B, C, D)
	draw_dot((intersection.x, intersection.y), color=BLUE)

	t+=0.003


	pygame.display.flip()

	clock.tick(FPS)



pygame.quit()
sys.exit()