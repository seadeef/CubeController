from pattern import Pattern
from random import shuffle
from time import sleep
from plotting import *

class RandFill(Pattern):
	def __init__(self, max_iters, frame_delay, new_iter_delay):
		super().__init__(max_iters, frame_delay)
		self.new_iter_delay = new_iter_delay
	
	def run(self):
		point_list = []
		for x in range(4):
			for y in range(4):
				for z in range(4):
					point_list.append((x, y, z))
		
		while self.running:
			shuffle(point_list)
			for point in point_list:
				plot(point)
				sleep(self.frame_delay)
			sleep(self.new_iter_delay)
			plot_cube(val=0)
			self.update_iters()