# flood starts from [8][4] and is 35 feet
import numpy as np
import math

#water_height is EV
def is_do_nothing(EV_cells, x, y):
    return EV_cells[x,y] == 0 # EV is not always water height! We need to figure out how to represent EV!

def end_sim(EV_cells, threshold):
    EV_cells_array = np.array(EV_cells)
    rows = EV_cells.shape[0]
    columns = EV_cells.shape[1]
    for i in range(rows):
        for j in range(columns):
            if EV_cells[i][j] > threshold:
                return False
    return True


def is_ponding(water_height, elevation_height, x, y, EV_cell):

    right_neighbor_cell_height = find_neighbor_cell_height(x, y, "right", water_height, elevation_height)
    left_neighbor_cell_height = find_neighbor_cell_height(x, y, "left", water_height, elevation_height)
    up_neighbor_cell_height = find_neighbor_cell_height(x, y, "up", water_height, elevation_height)
    down_neighbor_cell_height = find_neighbor_cell_height(x, y, "down", water_height, elevation_height)
    this_cell_height = water_height[x,y] + elevation_height[x, y]  
    existing_neighbors = get_existing_neighbors(x, y, elevation_height)
    num = 0
    for dir in existing_neighbors:
        if dir == "right" and right_neighbor_cell_height != -1 and this_cell_height < right_neighbor_cell_height:
            num += 1
        if dir == "left" and left_neighbor_cell_height != -1 and this_cell_height < left_neighbor_cell_height:
            num += 1
        if dir == "up" and up_neighbor_cell_height != -1 and this_cell_height < up_neighbor_cell_height:
            num += 1
        if dir == "down" and down_neighbor_cell_height != -1 and this_cell_height < down_neighbor_cell_height:
            num += 1
    return num == len(existing_neighbors)

def is_ponding_action(water_height, elevation_height, x, y, EV_cell):
    right_neighbor_cell_height = find_neighbor_cell_height(x, y, "right", water_height, elevation_height)
    left_neighbor_cell_height = find_neighbor_cell_height(x, y, "left", water_height, elevation_height)
    up_neighbor_cell_height = find_neighbor_cell_height(x, y, "up", water_height, elevation_height)
    down_neighbor_cell_height = find_neighbor_cell_height(x, y, "down", water_height, elevation_height)
    this_cell_height = water_height[x,y] + elevation_height[x, y]


    valid_neighbor_heights = [height for height in [right_neighbor_cell_height, left_neighbor_cell_height, up_neighbor_cell_height, down_neighbor_cell_height] if height != -1]

        # Check if there are valid neighbor heights
    if valid_neighbor_heights:
        min_val = min(valid_neighbor_heights)
        # Continue with your code using min_val
    else:
        # Handle the case where all neighbor heights are -1
        min_val = None  # or any other suitable default value or handling

    difference = min_val - this_cell_height
    if EV_cell[x,y] > difference:
        water_height[x,y] += difference
        EV_cell[x,y] -= difference
    else:
        water_height[x,y] += EV_cell[x,y]
        EV_cell[x,y] = 0


def is_spreading(water_height, elevation_height, x, y):
    existing_neighbors = get_existing_neighbors(x,y,elevation_height)
    right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)

    # makes an array of the neighbors of the central cell that exist with an elevation not equal to -1
    existing_values = [value for value in (right_neighbor_elevation_height, left_neighbor_elevation_height, up_neighbor_elevation_height, down_neighbor_elevation_height) if value != -1]
    
    right_neighbor_cell_height = find_neighbor_cell_height(x,y,"right", water_height, elevation_height)
    left_neighbor_cell_height = find_neighbor_cell_height(x,y,"left", water_height, elevation_height)
    up_neighbor_cell_height = find_neighbor_cell_height(x,y,"up", water_height, elevation_height)
    down_neighbor_cell_height = find_neighbor_cell_height(x,y,"down", water_height, elevation_height)
    this_cell_height = water_height[x,y] + elevation_height[x,y]

    cell_heights_equal = False

    if right_neighbor_cell_height == left_neighbor_cell_height == up_neighbor_cell_height == down_neighbor_cell_height:
        cell_heights_equal = True
    # checks if either (1): more than one neighbor exists and all the existing neighbors elevation heights equal the elevation height of the central cell
    # or (2): the cell heights (water + elevation) of all the neighboring cells are equal and the cell height of the central cell is equal than them
    return cell_heights_equal
    
def is_spreading_action(water_height, elevation_height, x, y, EV_cell):

    existing_neighbors = get_existing_neighbors(x, y, elevation_height)
    num_div = 1
    if "right" in existing_neighbors:
        num_div += 1
    if "left" in existing_neighbors:
        num_div += 1
    if "up" in existing_neighbors:
        num_div += 1
    if "down" in existing_neighbors:
        num_div += 1

    split = EV_cell[x,y] / num_div

    if "right" in existing_neighbors:
        EV_cell[x, find_neighbor(x,y,"right", elevation_height)] += split
    if "left" in existing_neighbors:
        EV_cell[x, find_neighbor(x,y,"left", elevation_height)] += split
    if "up" in existing_neighbors:
        EV_cell[find_neighbor(x,y,"up", elevation_height), y] += split
    if "down" in existing_neighbors:
        EV_cell[find_neighbor(x,y,"down", elevation_height), y] += split

    EV_cell[x,y] = split

    
def is_increasing_level(water_height, elevation_height, x, y):
    right_neighbor_cell_height = find_neighbor_cell_height(x,y,"right", water_height, elevation_height)
    left_neighbor_cell_height = find_neighbor_cell_height(x,y,"left", water_height, elevation_height)
    up_neighbor_cell_height = find_neighbor_cell_height(x,y,"up", water_height, elevation_height)
    down_neighbor_cell_height = find_neighbor_cell_height(x,y,"down", water_height, elevation_height)
    this_cell_height = water_height[x,y] + elevation_height[x,y]
    existing_neighbors = get_existing_neighbors(x,y, elevation_height)
    equal_neighbors = get_equal_cell_height_neighbors(x,y,elevation_height, water_height)
    num = 0


    if "right" in  existing_neighbors and "right" not in equal_neighbors:
        if this_cell_height < right_neighbor_cell_height:
            num += 1
    if "left" in  existing_neighbors and "left" not in equal_neighbors:
        if this_cell_height < left_neighbor_cell_height:
            num += 1
    if "up" in  existing_neighbors and "up" not in equal_neighbors:
        if this_cell_height < up_neighbor_cell_height:
            num += 1
    if "down" in existing_neighbors and "down" not in equal_neighbors:
        if this_cell_height < down_neighbor_cell_height:
            num += 1
    
    if equal_neighbors.size > 0 and (num + equal_neighbors.size) == len(existing_neighbors):
        return True
    else:
        return False
    


        
# precondition is that the water_height of the central cell will always be greater than the increment constant
def is_increasing_level_action(water_height, elevation_height, x, y, increment_constant, EV_cell):
    equal_neighbors = get_equal_cell_height_neighbors(x,y,water_height, elevation_height)
    if increment_constant > EV_cell[x,y]:
        water_height[x,y] += EV_cell[x,y]
        EV_cell[x,y] = 0
    else:
        water_height[x,y] += increment_constant
        EV_cell[x,y] -= increment_constant
        split = EV_cell[x,y] / equal_neighbors.size
        if "right" in equal_neighbors:
            EV_cell[x, find_neighbor(x,y,"right", elevation_height)] += split

        if "left" in equal_neighbors:
            EV_cell[x, find_neighbor(x,y,"left", elevation_height)] += split


        if "up" in equal_neighbors:
            EV_cell[find_neighbor(x,y,"up", elevation_height), y] += split

        if "down" in equal_neighbors:
            EV_cell[find_neighbor(x,y,"down", elevation_height), y] += split

        EV_cell[x,y] = 0
# i = 1 is northern cell
# i = 2 is eastern cell
# i = 3 is southern cell
# i = 4 is western cell
def is_partitioning_action(water_height, elevation_height, x, y, EV_cell):
    right_neighbor_cell_height = find_neighbor_cell_height(x,y,"right", water_height, elevation_height)
    left_neighbor_cell_height = find_neighbor_cell_height(x,y,"left", water_height, elevation_height)
    up_neighbor_cell_height = find_neighbor_cell_height(x,y,"up", water_height, elevation_height)
    down_neighbor_cell_height = find_neighbor_cell_height(x,y,"down", water_height, elevation_height)
    this_cell_height = water_height[x,y] + elevation_height[x,y]

    a = 0.09
    b = 0.25
    increased_height = a * EV_cell[x][y] ** b
    right_depth = -1
    left_depth = -1
    up_depth = -1
    down_depth = -1

    if right_neighbor_cell_height != -1:
        right_depth = max(0, this_cell_height + increased_height - right_neighbor_cell_height)
    if left_neighbor_cell_height != -1:
        left_depth = max(0, this_cell_height + increased_height - left_neighbor_cell_height)
    if up_neighbor_cell_height != -1:
        up_depth = max(0, this_cell_height + increased_height - up_neighbor_cell_height)
    if down_neighbor_cell_height != -1:
        down_depth = max(0, this_cell_height + increased_height - down_neighbor_cell_height)

    vals = [right_depth, left_depth, up_depth, down_depth]
    sum_result = 0
    for val in vals:
        if val != -1:
            sum_result += val

    if right_depth != -1:
        weight = right_depth / sum_result
        EV_cell[x, find_neighbor(x,y,"right", elevation_height)] += weight * EV_cell[x,y]
    if left_depth != -1:
        weight = left_depth / sum_result
        EV_cell[x, find_neighbor(x,y,"left", elevation_height)] += weight * EV_cell[x,y]
    if up_depth != -1:
        weight = up_depth / sum_result
        EV_cell[find_neighbor(x,y,"up", elevation_height), y] += weight * EV_cell[x,y]
    if down_depth != -1:
        weight = down_depth / sum_result
        EV_cell[find_neighbor(x,y,"down", elevation_height), y] += weight * EV_cell[x,y]

    EV_cell[x,y] = 0

def find_neighbor(x,y, direction, elevation_height):
    array_y = np.size(elevation_height, 1)
    array_x = np.size(elevation_height, 0)

    if direction == "right":
        if y < array_y - 1:
            return y+1
        else:
            return -1
    elif direction == "left":
        if y > 0:
            return y-1
        else:
            return -1
    elif direction == "up":
        if x > 0:
            return x-1
        else:
            return -1
    elif direction == "down":
        if x < array_x - 1:
            return x+1
        else:
            return -1
    
def find_neighbor_elevation_height(x,y, direction, elevation_height):
    if direction == "right" or direction == "left":
        if find_neighbor(x,y,direction,elevation_height) != -1:
            return elevation_height[x, find_neighbor(x,y,direction,elevation_height)]
        else:
            return -1
    elif direction == "up" or direction == "down":
        if find_neighbor(x,y,direction,elevation_height) != -1: 
          return elevation_height[find_neighbor(x,y,direction,elevation_height), y]
        else:
            return -1
        
def find_neighbor_water_height(x,y, direction, water_height):
    if direction == "right" or direction == "left":
        if find_neighbor(x,y,direction,water_height) != -1:
            return water_height[x, find_neighbor(x,y,direction,water_height)]
        else:
            return -1
    elif direction == "up" or direction == "down":
        if find_neighbor(x,y,direction,water_height) != -1: 
          return water_height[find_neighbor(x,y,direction,water_height), y]
        else:
            return -1

def find_neighbor_cell_height(x,y,direction, water_height, elevation_height):
    sum = find_neighbor_elevation_height(x,y,direction, elevation_height) + find_neighbor_water_height(x,y,direction, water_height)    
    if find_neighbor_elevation_height(x,y,direction, elevation_height) != -1 and find_neighbor_water_height(x,y,direction, water_height) != -1:
        return sum
    else:
        return -1
        
def get_equal_neighbors_dirs(x,y,elevation_height):
    this_elevation_height = elevation_height[x,y]
    right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)

    equal_values_array = np.array([])

    if this_elevation_height == right_neighbor_elevation_height:
        equal_values_array = np.append(equal_values_array, "right")

    if this_elevation_height == left_neighbor_elevation_height:
        equal_values_array = np.append(equal_values_array, "left")

    if this_elevation_height == up_neighbor_elevation_height:
        equal_values_array = np.append(equal_values_array, "up")

    if this_elevation_height == down_neighbor_elevation_height:
        equal_values_array = np.append(equal_values_array, "down")

    return equal_values_array

def get_equal_cell_height_neighbors(x,y, elevation_height, water_height):
    right_neighbor_cell_height = find_neighbor_cell_height(x,y,"right", water_height, elevation_height)
    left_neighbor_cell_height = find_neighbor_cell_height(x,y,"left", water_height, elevation_height)
    up_neighbor_cell_height = find_neighbor_cell_height(x,y,"up", water_height, elevation_height)
    down_neighbor_cell_height = find_neighbor_cell_height(x,y,"down", water_height, elevation_height)
    this_cell_height = water_height[x,y] + elevation_height[x,y]
                                                            
    equal_values_array = np.array([])
    if right_neighbor_cell_height == this_cell_height:
        equal_values_array = np.append(equal_values_array, "right")
    if left_neighbor_cell_height == this_cell_height:
        equal_values_array = np.append(equal_values_array, "left")
    if up_neighbor_cell_height == this_cell_height:
        equal_values_array = np.append(equal_values_array, "up")
    if down_neighbor_cell_height == this_cell_height:
        equal_values_array = np.append(equal_values_array, "down")

    return equal_values_array

def get_existing_neighbors(x, y, elevation_height):
    rows, columns = elevation_height.shape
    existing_neighbors = []
    if x > 0:
        existing_neighbors.append("up")

    if x != rows - 1:
        existing_neighbors.append("down")

    if y > 0:
        existing_neighbors.append("left")
    
    if y != columns - 1:
        existing_neighbors.append("right")
    
    return existing_neighbors



def haversine_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance

def calc_width(north_lat, south_lat, east_lon, west_lon):
    # Calculate distances between corners of the bounding box
    width = haversine_distance(north_lat, east_lon, north_lat, west_lon)

    return width

def calc_height(north_lat, south_lat, east_lon, west_lon):
    height = haversine_distance(north_lat, east_lon, south_lat, east_lon)
    return height
