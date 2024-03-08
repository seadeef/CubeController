from pattern import Pattern
from random import randint
from time import sleep
from plotting import *

class Rain(Pattern):
	def run(self):
		points = []
		while self.running:
			for point in points:
				if point[1] > 0:
					point[1] -= 1
				else:
					points.remove(point)

			points.append([randint(0, 3), 3, randint(0, 3)])

			plot_list(points)
			sleep(self.frame_delay)
			plot_cube(val=0)
			self.update_iters()