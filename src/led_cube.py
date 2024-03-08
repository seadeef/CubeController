import sys 
sys.path.append("./")

from patterns.rain import Rain
from patterns.voxel_send import VoxelSend
from patterns.rand_fill import RandFill
from patterns.plane_bounce import PlaneBounce
from patterns.rand_snake import RandSnake
from patterns.rand_lines import RandLines
from patterns.diagonal_cube import DiagonalCube
from patterns.voxel_suspend import VoxelSuspend

from sequence import Sequence
from points_display import PointsDisplay
from threading import Thread

try:
	sequence = Sequence(
					0.5,
					(VoxelSuspend(17, 0.0825, 0.75),
					DiagonalCube(21, 0.0725, 0.1),
					RandSnake(332, 0.055),
					Rain(172, 0.075),
					PlaneBounce(32, 0.06),
					VoxelSend(27, 0.075, 0.25),
					RandLines(112, 0.1),
					RandFill(7, 0.025, 0.25)))

	points_display = PointsDisplay(0.001)
	points_display_thread = Thread(target=points_display.start)
	points_display_thread.start()

	sequence.run()
except KeyboardInterrupt:
	pass	
finally:
	points_display.running = False
