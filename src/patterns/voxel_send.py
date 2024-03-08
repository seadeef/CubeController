from pattern import Pattern
from random import randint
from time import sleep
from plotting import *

class VoxelSend(Pattern):
	def __init__(self, max_iters, frame_delay, send_delay):
		super().__init__(max_iters, frame_delay)
		self.send_delay = send_delay
	
	def run(self):
		for x in range(4):
			for z in range(4):
				if randint(0, 1):
					plot((x, 3, z))
				else:
					plot((x, 0, z))
		
		while self.running:
			rand_x, rand_z = randint(0, 3), randint(0, 3)
			
			if get_state((rand_x, 0, rand_z)):
				rand_point = [rand_x, 0, rand_z]
				is_bottom_point = True
			else:
				rand_point = [rand_x, 3, rand_z]
				is_bottom_point = False

			for _ in range(3):
				plot(rand_point, val=0)
				rand_point[1] += 1 if is_bottom_point else -1
				plot(rand_point)
				sleep(self.frame_delay)
			
			sleep(self.send_delay)
			self.update_iters()
		plot_cube(val=0)