from time import sleep

class Sequence:
	def __init__(self, delay, patterns):
		self.delay = delay
		self.patterns = patterns

	def run(self):
		for pattern in self.patterns:
			pattern.run()
			sleep(self.delay)
