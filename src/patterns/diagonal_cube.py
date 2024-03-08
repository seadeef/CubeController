from pattern import Pattern
from random import choice
from time import sleep
from plotting import *

class DiagonalCube(Pattern):
	def __init__(self, max_iters, frame_delay, new_diagonal_delay):
		super().__init__(max_iters, frame_delay)
		self.new_diagonal_delay = new_diagonal_delay

	def run(self):
		last_corner = [0, 0, 0]
		corner = [0, 0, 0]
		while self.running:
			while corner == last_corner:
				corner = [choice([0, 3]) for _ in range(3)]
			last_corner = corner[:]

			new_coords = corner[:]
			plot(corner)
			sleep(self.frame_delay)
			
			for frame in range(3):	
				for i in range(len(corner)):
					if corner[i] == 0:
						new_coords[i] += 1
					else:
						new_coords[i] -= 1

				plot_area(corner, new_coords)
				sleep(self.frame_delay)
			sleep(self.new_diagonal_delay)
			
			new_coords = [0 if coord==3 else 3 for coord in corner]
			plot_cube(val=0)

			for frame in range(3):
				for i in range(len(corner)):
					if corner[i] == 0:
						new_coords[i] -= 1
					else:
						new_coords[i] += 1
				
				plot_area(corner, new_coords)
				sleep(self.frame_delay)
				plot_cube(val=0)
			
			sleep(self.new_diagonal_delay)
			self.update_iters()

