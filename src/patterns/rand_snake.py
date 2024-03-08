from pattern import Pattern
from random import randint
from time import sleep
from plotting import *

class RandSnake(Pattern):
	def run(self):
		body = []
		curr_pos = [0, 0, 0]
		backup_pos = [0, 0, 0]
		tries = 0
		while self.running:
			tries += 1
			direction = randint(0, 5)
			if direction < 3:
				curr_pos[direction] += 1
			else:
				curr_pos[direction%3] -= 1
			
			if not any(coord<0 or coord>3 for coord in curr_pos) and (not curr_pos in body or tries > 20):
				tries = 0
				backup_pos = curr_pos[:]
				body.append(curr_pos[:])
				plot(curr_pos)

				if len(body) > 12:
					plot(body[0], val=0)
					del body[0]

				sleep(self.frame_delay)
				self.update_iters()

			else:
				tries += 1
				curr_pos = backup_pos[:]

		plot_cube(val=0)