from points_display import points

def get_state(point_coords):
	x, y, z = point_coords
	return points[y][x][z]
	
def plot(point_coords, val=1):
	x, y, z = point_coords
	points[y][x][z] = val

def plot_area(point1, point2, val=1):
	x1, y1, z1 = point1
	x2, y2, z2 = point2

	if x1 > x2:
		x1, x2 = x2, x1
	if y1 > y2:
		y1, y2 = y2, y1
	if z1 > z2:
		z1, z2 = z2, z1
	
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			for z in range(z1, z2+1):
				plot((x, y, z), val)

def plot_list(point_list, val=1):
	for point in point_list:
		plot(point, val)
		
def plot_cube(val=1):
	plot_area((0, 0, 0), (3, 3, 3), val)