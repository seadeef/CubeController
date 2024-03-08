from pattern import Pattern
from random import randint
from time import sleep
from plotting import *

class PlaneBounce(Pattern):
	def run(self):
		while self.running:
			for n in range(7):
				n = min(n, 6-n)
				self.draw_plane(n)
			self.update_iters()

	def draw_plane(self, n):
		if self.iters%3 == 0:
			plot_area((0, n, 0), (3, n, 3))
		elif self.iters%3 == 1:
			plot_area((n, 0, 0), (n, 3, 3))
		else:
			plot_area((0, 0, n), (3, 3, n))
		sleep(self.frame_delay)
		plot_cube(val=0)