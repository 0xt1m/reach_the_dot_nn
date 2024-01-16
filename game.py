import pygame
import sys
import random
import numpy as np

import properties as props

from dot import Dot, Goal
from obstacle import Obstacle


pygame.init()


# VARS
screen = pygame.display.set_mode([props.WIDTH, props.HEIGHT])
clock = pygame.time.Clock()

dot = Dot(screen)
goal = Goal(screen)

# obstacle_x = random.randint(0, 400)
# obstacle_y = random.randint(100, 500)
obstacle_width = 300
obstacle_height = 20
# obstacle_x = props.WIDTH / 2 - obstacle_width / 2
obstacle_x = 550
obstacle_y = 350


obstacles = [
	Obstacle(screen, obstacle_x, obstacle_y, obstacle_width, obstacle_height)
]

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	if dot.dead:
		print("[+] GAME OVER")
		dot = Dot(screen)


	screen.fill(props.COLORS["black"])

	for obstacle in obstacles:
		obstacle.show()

	dot.show()
	dot.move()
	dot.update(obstacles)

	goal.show()

	pygame.display.flip()

	clock.tick(props.FPS)



pygame.quit()
sys.exit()



