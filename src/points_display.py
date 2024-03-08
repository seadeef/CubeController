import RPi.GPIO as GPIO
from time import sleep

points = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
		  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
		  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
		  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

transistor_layers = [17, 4, 3, 2]

column_grid = [[9, 11, 0, 5], [1, 27, 22, 10], [24, 25, 8, 7], [14, 15, 18, 23]]

all_pins = transistor_layers + [pin for row in column_grid for pin in row]

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(all_pins, GPIO.OUT)

class PointsDisplay:
	def __init__(self, delay):
		self.running = True
		self.delay = delay
	
	def start(self):
		while self.running:
			for y in range(4):
				layer_active = False
				for x in range(4):
					for z in range(4):
						if points[y][x][z]:
							GPIO.output(column_grid[x][z], 1)
							layer_active = True        
				if layer_active:
					GPIO.output(transistor_layers[y], 1)
					sleep(self.delay)
					GPIO.output(all_pins, 0)
		GPIO.cleanup(all_pins)