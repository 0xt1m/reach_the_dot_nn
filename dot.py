import pygame
import random
import numpy as np

import sensors
import properties as props

class Dot:
	def __init__(self, screen, radius=props.DOT_RADIUS, color=props.COLORS["white"], speed=props.DOT_SPEED, step=props.DOT_STEP):
		self.screen = screen
		self.radius = radius
		self.color = color
		
		self.speed = speed
		self.step = step

		self.dead = False
		self.moves = np.array([])
		
		self.score = 0

		self.sensors = sensors.Sensors(self)

		self.x = props.DOT_X
		self.y = props.DOT_Y

		self.step_completion = 0
		self.current_move = self.next_move()

		self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)


	def move(self):
		# For now it is gonna move just randomly
		if not self.dead:
			if self.step_completion >= self.step:
				self.current_move = self.next_move()
			else:
				if self.current_move[0]:
					self.y -= self.speed
				elif self.current_move[1]:
					self.y += self.speed
				elif self.current_move[2]:
					self.x -= self.speed
				elif self.current_move[3]:
					self.x += self.speed
				elif self.current_move[4]:
					self.y -= self.speed
					self.x -= self.speed
				elif self.current_move[5]:
					self.y -= self.speed
					self.x += self.speed
				elif self.current_move[6]:
					self.y += self.speed
					self.x -= self.speed
				elif self.current_move[7]:
					self.y += self.speed
					self.x += self.speed

				self.step_completion += self.speed


	def next_move(self):
		self.step_completion = 0
		moves = np.array([
			0, # UP
			0, # DOWN
			0, # LEFT
			0, # RIGHT
			0, # UP LEFT
			0, # UP RIGHT
			0, # DOWN LEFT
			0, # DOWN RIGHT
		])

		rand = random.randint(0, 7)
		moves[rand] = 1

		return moves


	def show(self):
		pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
		self.sensors.show()


	def update(self):
		self.out()
		self.sensors.update()


	def out(self):
		if self.y < 0 or self.x < 0:
			self.dead = True
		elif self.y > props.HEIGHT - props.DOT_RADIUS or self.x > props.WIDTH - props.DOT_RADIUS:
			self.dead = True


class Goal:
	def __init__(self, screen):
		self.screen = screen

		self.x = props.GOAL_X
		self.y = props.GOAL_Y

		self.color = props.COLORS["green"]


	def show(self):
		pygame.draw.circle(self.screen, self.color, (self.x, self.y), props.DOT_RADIUS)


# TRAINING DATA
# data from 8 axes that tell what is around the dot.
#
# A set of training data creates every time when the dot moves.
#
# LABELS
# Right move (the move is right if the dot did not touch the obstacle)
# The rewarding system will be needed to create the labels.
#
# AXE
# the axe will check every pixel from the dot in particular direction
# if it sees just black pixels it puts 0
# if it sees the pixels of an obstacle it puts 1
# if it see the pixesls of the goal it puts 2

# Do I need to put current move in the inputs?
# Nope. The neural network will give me a direction where to move based on its vision!
# I do not need current move there. 
# The neural network will compare the right move with the predicted one.

# I need to store current move and look if the dot was rewarded. If the dot was rewarded ^%$^%$^

# Actually my moves look like this:
# [0, 0, 0, 1, 0, 0, 0, 0]

# For example 
# when according to axe[0]↑ distance to an obstacle is less then 10
# the right move is [0, 0, 0, 1, 0, 0, 0, 0]

# Dots that did not touch the obstacle will be added to the training data.
# Dots that reached the goal will be added to the training data a couple of times.

# I AM STUPID

# I do not add the dots that did not reach the goal to the training data.
# I am adding only those dots that reached the goal.

# But I still have the problem that I need a way to reward better those dots that reached the goal.











