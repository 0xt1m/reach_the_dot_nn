import pygame
import sys

pygame.init()


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

line_A = ((70, 150), (550, 330))
line_B = ((60, 300), (550, 250))

t = -0.1


# FUNCS
def draw_line(start_point, end_point):
	pygame.draw.line(screen, WHITE, start_point, end_point, width=2)


def draw_dot(point, radius=13, color=GREEN):
	pygame.draw.circle(screen, color, point, radius)


def lerp(A, B, t):
	return A+(B-A)*t


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(BLACK)

	# draw_dot((WIDTH/2, HEIGHT/2))
	draw_line(line_A[0], line_A[1])
	draw_line(line_B[0], line_B[1])


	dot_x = lerp(line_A[0][0], line_A[1][0], t)
	dot_y = lerp(line_A[0][1], line_A[1][1], t)
	draw_dot((dot_x, dot_y))

	t+=0.003


	pygame.display.flip()

	clock.tick(FPS)



pygame.quit()
sys.exit()