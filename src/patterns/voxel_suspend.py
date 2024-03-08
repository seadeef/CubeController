from pattern import Pattern
from random import randint, shuffle
from time import sleep
from plotting import *

class VoxelSuspend(Pattern):
    def __init__(self, max_iters, frame_delay, suspend_delay):
        super().__init__(max_iters, frame_delay)
        self.suspend_delay = suspend_delay

    def run(self):        
        while self.running:
            suspend_points = []
            while not(0 in suspend_points and 1 in suspend_points and 2 in suspend_points):
                suspend_points = [randint(0, 3) for i in range(16)]

            if self.iters%3 == 0:
                points = [[0, y, z] for y in range(4) for z in range(4)]
                change_index = 0

            elif self.iters%3 == 1:
                points = [[x, 0, z] for x in range(4) for z in range(4)]
                change_index = 1
                
            else:
                points = [[x, y, 0] for x in range(4) for y in range(4)]
                change_index = 2

            for _ in range(4):
                do_not_update = []
                plot_cube(val=0)
                plot_list(points)
                sleep(self.frame_delay)

                for i in range(16):
                    if i not in do_not_update:
                        if points[i][change_index] == suspend_points[i]:
                            do_not_update.append(i)
                        else:
                            points[i][change_index] += 1

            self.update_iters()
            sleep(self.suspend_delay)
            plot_cube(val=0)
