"""
[[2540 2548 2525 2530 2530 2534 2512 2522 2538]
 [2543 2533 2530 2530 2521 2520 2527 2509 2519]
 [2533 2533 2533 2523 2523 2536 2507 2510 2527]
 [2509 2533 2509 2530 2502 2514 2527 2510 2522]
 [2533 2525 2517 2532 2541 2517 2501 2503 2515]
 [2529 2548 2535 2528 2520 2519 2512 2525 2506]
 [2529 2500 2533 2506 2549 2523 2546 2509 2514]
 [2513 2508 2518 2503 2526 2508 2530 2541 2511]
 [2539 2549 2506 2541 2507 2522 2503 2543 2547]]

"""

# flood starts from [8][4] and is 35 feet
import numpy as np

def calc_cell_height(x, y):
  return elevation_height[x,y] + water_height[x,y]

def is_do_nothing(water_height, x, y):
    if water_height[x,y] == 0:
        return True
    
    return False

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


elevation_height = np.array([[2540, 2548, 2525, 2530, 2530, 2534, 2512, 2522, 2538], [2543, 2533, 2530, 2530, 2521, 2520, 2527, 2509, 2519],
                             [2533, 2533, 2533, 2523, 2523, 2536, 2507, 2510, 2527], [2509, 2533, 2509, 2530, 2502, 2514, 2527, 2510, 2522],
                             [2533, 2525, 2517, 2532, 2541, 2517, 2501, 2503, 2515], [2529, 2548, 2535, 2528, 2520, 2519, 2512, 2525, 2506],
                             [2529, 2500, 2533, 2506, 2549, 2523, 2546, 2509, 2514], [2513, 2508, 2518, 2503, 2526, 2508, 2530, 2541, 2511],
                             [2539, 2549, 2506, 2541, 2507, 2522, 2503, 2543, 2547]])
water_height = np.zeros((9,9))
water_height[6, 7] = 35
water_height[2,1] = 15
"""
if is_ponding(water_height, elevation_height, 6,7):
    is_ponding_action(water_height, elevation_height, 6,7)
"""
if is_spreading(water_height, elevation_height, 2, 1):
    is_spreading_action(water_height, elevation_height, 2, 1)