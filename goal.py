class Goal:
	def __init__(self):
		self.x = GOAL_X
		self.y = GOAL_Y

		self.color = RED


	def show(self):
		pygame.draw.circle(screen, self.color, (self.x, self.y), DOT_RADIUS)