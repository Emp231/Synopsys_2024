"""
[[2540 2548 2525 2530 2530 2534 2512 2522 2538]
 [2543 2533 2530 2530 2521 2520 2527 2509 2519]
 [2533 2533 2533 2523 2523 2536 2507 2510 2527]
 [2509 2533 2509 2530 2502 2514 2527 2510 2522]
 [2533 2525 2517 2532 2541 2517 2501 2503 2515]
 [2529 2548 2535 2528 2520 2519 2512 2525 2506]
 [2529 2508 2533 2506 2549 2523 2546 2509 2514]
 [2513 2508 2518 2503 2526 2508 2530 2541 2511]
 [2539 2549 2506 2541 2507 2522 2503 2543 2547]]

"""

# flood starts from [8][4] and is 35 feet
import numpy as np

def calc_cell_height(x, y):
  return elevation_height[x,y] + water_height[x,y]

def is_do_nothing(water_height, x, y):
    return water_height[x,y] == 0

def end_sim(water_height):
    array_x = np.size(water_height, 1)
    array_y = np.size(water_height, 0)
    for x in range(array_x):
        for y in range(array_y):
            if water_height[x,y] != 0:
                return False

    return True

def is_ponding(water_height, elevation_height, x, y):
    right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)
    num = 0

    current_cell_elevation_height = elevation_height[x, y]
    
    if right_neighbor_elevation_height != -1 and current_cell_elevation_height < right_neighbor_elevation_height:
        num += 1
    if left_neighbor_elevation_height != -1 and current_cell_elevation_height < left_neighbor_elevation_height:
        num += 1
    if up_neighbor_elevation_height != -1 and current_cell_elevation_height < up_neighbor_elevation_height:
        num += 1
    if down_neighbor_elevation_height != -1 and current_cell_elevation_height < down_neighbor_elevation_height:
        num += 1
    
    if num == 4:
        return True
    else:
        return False
    
def is_ponding_action(water_height, elevation_height, x, y):
    right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)
    current_cell_elevation_height = elevation_height[x,y]
    min_value = min(value for value in [right_neighbor_elevation_height, left_neighbor_elevation_height, up_neighbor_elevation_height, down_neighbor_elevation_height] if value != -1)
    difference = min_value - current_cell_elevation_height
    cell_EV = water_height[x,y]

    if difference > cell_EV:
        elevation_height[x,y] += cell_EV
        water_height[x,y] = 0
    else:
        elevation_height[x,y] += difference
        water_height[x,y] -= difference


def is_spreading(water_height, elevation_height, x, y):
    right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)

    
    if right_neighbor_elevation_height == left_neighbor_elevation_height == up_neighbor_elevation_height == down_neighbor_elevation_height:
        return True
    else:
        return False
    
def is_spreading_action(water_height, elevation_height, x, y):
    split = water_height[x,y] / 5
    water_height[x, find_neighbor(x,y,"right", elevation_height)] = split
    water_height[x, find_neighbor(x,y,"left", elevation_height)] = split
    water_height[find_neighbor(x,y,"up", elevation_height), y] = split
    water_height[find_neighbor(x,y,"down", elevation_height), y] = split
    water_height[x,y] = split
    
def is_increasing_level(water_height, elevation_height, x, y):
    this_elevation_height = elevation_height[x,y]
    right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)

    equal_values_array = get_equal_neighbors_dirs(x,y,elevation_height)
    original_dirs_array = np.array(["right", "left", "up", "down"])

    if equal_values_array.size <= 3:
        values_not_equal_array = np.setdiff1d(original_dirs_array, equal_values_array)
        num = 0
        if "right" in values_not_equal_array and right_neighbor_elevation_height > this_elevation_height:
            num = num + 1

        if "left" in values_not_equal_array and left_neighbor_elevation_height > this_elevation_height:
            num = num + 1

        if "up" in values_not_equal_array and up_neighbor_elevation_height > this_elevation_height:
            num = num + 1

        if "down" in values_not_equal_array and down_neighbor_elevation_height > this_elevation_height:
            num = num + 1

        if num == 4 - equal_values_array.size:
            return True
        else:
            return False
        
# precondition is that the water_height of the central cell will always be greater than the increment constant
def is_increasing_level_action(water_height, elevation_height, x, y, increment_constant):
    equal_neighbors = get_equal_neighbors_dirs(x, y, elevation_height)
    elevation_height[x,y] += increment_constant 
    water_height[x,y] -= increment_constant

    split_val = water_height[x,y] / equal_neighbors.size
    
    if "right" in equal_neighbors:
        water_height[x, find_neighbor(x,y,"right", elevation_height)] = split_val
        water_height[x,y] -= split_val
    if "left" in equal_neighbors:
        water_height[x, find_neighbor(x,y,"left", elevation_height)] = split_val
        water_height[x,y] -= split_val
    if "up" in equal_neighbors:
        water_height[find_neighbor(x,y,"up", elevation_height), y] = split_val
        water_height[x,y] -= split_val
    if "down" in equal_neighbors:
        water_height[find_neighbor(x,y,"down", elevation_height), y] = split_val
        water_height[x,y] -= split_val

# i = 1 is northern cell
# i = 2 is eastern cell
# i = 3 is southern cell
# i = 4 is western cell
def is_partitioning_action(water_height, elevation_height, x, y):
    right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)
    this_elevation_height = elevation_height[x,y]

    a = 1
    b = 1

    increased_height = a * water_height[x,y]^b

        
    if right_neighbor_elevation_height < this_elevation_height:
        water_height[x, find_neighbor(x,y,"right", elevation_height)] = max(0, elevation_height[x,y] + increased_height - elevation_height[x, find_neighbor(x,y,"right", elevation_height)])
    
    if left_neighbor_elevation_height < this_elevation_height:
        water_height[x, find_neighbor(x,y,"left", elevation_height)] = max(0, elevation_height[x,y] + increased_height - elevation_height[x, find_neighbor(x,y,"left", elevation_height)])

    if up_neighbor_elevation_height < this_elevation_height:
        water_height[find_neighbor(x,y,"up", elevation_height), x] = max(0, elevation_height[x,y] + increased_height - elevation_height[find_neighbor(x,y,"up", elevation_height), y])

    if down_neighbor_elevation_height < this_elevation_height:
        water_height[find_neighbor(x,y,"down", elevation_height), x] = max(0, elevation_height[x,y] + increased_height - elevation_height[find_neighbor(x,y,"down", elevation_height), y])

    



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


elevation_height = np.array([[2540, 2548, 2525, 2530, 2530, 2534, 2512, 2522, 2538], 
                             [2543, 2533, 2530, 2530, 2521, 2520, 2527, 2509, 2519],
                             [2533, 2533, 2533, 2523, 2523, 2536, 2507, 2510, 2527], 
                             [2509, 2533, 2509, 2530, 2502, 2514, 2527, 2510, 2522],
                             [2533, 2525, 2517, 2532, 2541, 2517, 2501, 2503, 2515], 
                             [2529, 2548, 2535, 2528, 2520, 2519, 2512, 2525, 2506],
                             [2529, 2508, 2533, 2506, 2549, 2523, 2546, 2509, 2514], 
                             [2533, 2508, 2508, 2503, 2526, 2508, 2530, 2541, 2511],
                             [2539, 2525, 2506, 2541, 2507, 2522, 2503, 2543, 2547]])
water_height = np.zeros((9,9))
water_height[6, 7] = 35
water_height[2,1] = 15
water_height[7,1] = 40
increment_constant = 11
"""
if is_ponding(water_height, elevation_height, 6,7):
    is_ponding_action(water_height, elevation_height, 6,7)
"""
"""
if is_spreading(water_height, elevation_height, 2, 1):
    is_spreading_action(water_height, elevation_height, 2, 1)
"""

"""
if is_increasing_level(water_height, elevation_height, 7, 1):
    #print(get_equal_neighbors_dirs(7,1,elevation_height))
    is_increasing_level_action(water_height, elevation_height, 7, 1, increment_constant)
"""

x = 1
y = 2
"""
if is_do_nothing(water_height, x, y):
    print(0)
elif is_ponding(water_height, elevation_height, x, y):
    print(1)
elif is_spreading(water_height, elevation_height, x, y):
    print(2)
elif is_increasing_level(water_height, elevation_height, x, y):
    print(3)
else:
    print(4)
"""
