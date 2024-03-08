class Pattern:
	def __init__(self, max_iters, frame_delay):
		self.max_iters = max_iters
		self.frame_delay = frame_delay
		
		self.running = True
		self.iters = 0
	
	def update_iters(self):
		self.iters += 1
		if self.iters == self.max_iters:
			self.running = False
	
	def run(self):
		raise NotImplementedError

		