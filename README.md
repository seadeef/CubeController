# CubeController
CubeController is a collection of Python code to control and animate my Raspberry Pi 4x4x4 LED cube. You are free to use it for your own cube, though, which is what the following sections describe.
 
## Physical Requirements
* A Raspberry Pi
    * 20 usable GPIO pins
    * Able to light up 16 LEDs at once
* An LED cube
    * 4x4x4 in size
    * 16 anode-columns wired up to the Pi
    * 4 cathode-layers wired up to Pi-controlled transistors

## Software Requirements
* [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
* Python 3

## Using CubeController
1. Before using CubeController, you must tell it which pins to use to turn on certain LEDs. Inside `points_display.py`, update the `transistor_layers` and `column_grid` arrays to match with your cube. If done correctly, turning on the pins contained in `transistor_layers[y]` and `column_grid[x][z]` should light up the LED at those coordinates, with the x coordinate starting at the back of the cube, the y coordinate starting at the bottom of the cube, and the z coordinate starting at the right of the cube.

2. Next, you may want to create additional animations for your cube. To do so, create a new file inside `patterns/` and import the `Pattern` base class from `pattern.py`, the plotting functions from `plotting.py`, and the `sleep()` function from `time`, along with anything animation-specific. Then, create a new class that inherits from `Pattern`. The `__init__()` function inside of `Pattern` automatically takes two arguments: `max_iters`, which tells your animation how many loops to run for, and `frame_delay`, which tells your animation how long to wait between frames (this is where `sleep()` becomes handy). Adding any extra arguments requires you to override the `__init__()` function. Then, create a `run()` method inside your class, which will automatically be called when it's your animation's turn to run. Inside of this, create a `while self.running:` block, add your animation code (making use of the `plotting.py` functions), and add a call to `self.update_iters()` at the end, which will decide when your animation has run for long enough and update `self.running` accordingly. Once you're done, go into `led_cube.py` and update the `sequence` object with an instance of your animation class.

3. Finally, when you want to run CubeController, execute `python3 led_cube.py`. You may wait until the entire sequence has finished, or you may `Ctrl+C` early.
