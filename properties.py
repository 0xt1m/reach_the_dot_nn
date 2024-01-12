import numpy as np

WIDTH, HEIGHT = 800, 600

FPS = 60

DOT_RADIUS = 10

GOAL_X = 400
GOAL_Y = 80

DOT_X = WIDTH / 2
DOT_Y = HEIGHT - 100

DOT_SPEED = 4
DOT_STEP = 30

MOVES = np.array([
	0, # UP
	0, # DOWN
	0, # LEFT
	0, # RIGHT
	0, # UP LEFT
	0, # UP RIGHT
	0, # DOWN LEFT
	0, # DOWN RIGHT
])

COLORS = {
	"black": (0, 0, 0),
	"white": (255, 255, 255),
	"red": (255, 0, 0),
	"blue": (0, 0, 255),
	"green": (0, 255, 0),
	"yellow": (255, 255, 0)
}
