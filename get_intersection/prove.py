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

WIDTH = 800
HEIGHT = 800

FPS = 60


# VARS
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()


# FUNCS
def draw_line(start_point, end_point):
	pygame.draw.line(screen, WHITE, start_point, end_point, width=2)


def draw_dot(point, radius=13, color=GREEN):
	pygame.draw.circle(screen, color, (point.x, point.y), radius)


def lerp(A, B, t):
	return A+(B-A)*t


A = Point(70, 150)
B = Point(500, 400)
C = Point(60, 300)
D = Point(550, 300)


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(WHITE)

	draw_dot(A)
	draw_dot(B)
	draw_dot(C)
	draw_dot(D)

	pygame.display.flip()

	clock.tick(FPS)



pygame.quit()
sys.exit()





