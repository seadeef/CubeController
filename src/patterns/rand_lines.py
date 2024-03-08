from pattern import Pattern
from random import randint
from time import sleep
from plotting import *

class RandLine:
	def __init__(self, curr_pos, constant_index):
		self.curr_pos = curr_pos
		self.constant_index = constant_index
		self.changing_indices = [index for index in [0, 1, 2] if index != self.constant_index]

	def generate_rand_coords(self):
		temp_pos = self.curr_pos[:]
		direction = randint(0, 3)
		
		if direction < 2:
			temp_pos[self.changing_indices[direction]] += 1
		else:
			temp_pos[self.changing_indices[direction%2]] -= 1

		return temp_pos

	def draw(self):
		first_coord = self.curr_pos
		second_coord = self.curr_pos[:]
		second_coord[self.constant_index] = 3

		plot_area(first_coord, second_coord)

class RandLines(Pattern):
	def run(self):		
		lines = [[RandLine([0, 1, 1], 0), RandLine([0, 1, 2], 0)],
				 [RandLine([1, 0, 1], 1), RandLine([1, 0, 2], 1)],
				 [RandLine([1, 1, 0], 2), RandLine([1, 2, 0], 2)]]

		while self.running:
			for line_group in lines:
				used_coords = [line.curr_pos for line in line_group]
				for index, line in enumerate(line_group):
					tries = 0
					while True:
						tries += 1
						new_coords = line.generate_rand_coords()
						if not any(coord<0 or coord>3 for coord in new_coords) and (not new_coords in used_coords or tries > 20):
							used_coords[index] = new_coords
							line.curr_pos = new_coords
							line.draw()
							break
							
			sleep(self.frame_delay)
			self.update_iters()
			plot_cube(val=0)