'''
from osgeo import gdal
dataset = gdal.Open("C:/Users/fastp/OneDrive/Documents/GitHub/Synopsys_2024/algorithms", gdal.GA_ReadOnly)

print("Driver: {}/{}".format(dataset.GetDriver().ShortName,
                            dataset.GetDriver().LongName))
print("Size is {} x {} x {}".format(dataset.RasterXSize,
                                    dataset.RasterYSize,
                                    dataset.RasterCount))
print("Projection is {}".format(dataset.GetProjection()))
geotransform = dataset.GetGeoTransform()
if geotransform:
    print("Origin = ({}, {})".format(geotransform[0], geotransform[3]))
    print("Pixel Size = ({}, {})".format(geotransform[1], geotransform[5]))
'''

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
import math

#water_height is EV

def calc_cell_height(x, y):
  return elevation_height[x,y] + water_height[x,y]

def is_do_nothing(water_height, x, y):
    return water_height[x,y] == 0 # EV is not always water height! We need to figure out how to represent EV!

def end_sim(water_height):
    array_x = np.size(water_height, 1)
    array_y = np.size(water_height, 0)
    for x in range(array_x):
        for y in range(array_y):
            if water_height[x,y] > 1:
                return False

    return True

def is_ponding(water_height, elevation_height, x, y, EV_cell):
    # right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    # left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    # up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    # down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)

    # num = 0

    # existing_neighbors = get_existing_neighbors(x, y, elevation_height)

    # current_cell_elevation_height = elevation_height[x, y]
    
    # # sets num equal to the number of cells around the central cell that the central cell is less than
    # if right_neighbor_elevation_height != -1 and current_cell_elevation_height < right_neighbor_elevation_height:
    #     num += 1
    # if left_neighbor_elevation_height != -1 and current_cell_elevation_height < left_neighbor_elevation_height:
    #     num += 1
    # if up_neighbor_elevation_height != -1 and current_cell_elevation_height < up_neighbor_elevation_height:
    #     num += 1
    # if down_neighbor_elevation_height != -1 and current_cell_elevation_height < down_neighbor_elevation_height:
    #     num += 1
    
    # # checks if the number of cells that the central cell is less than is all the cells around the central cell
    # if num == existing_neighbors.size:
    #     return True
    # else:
    #     return False

    right_neighbor_cell_height = find_neighbor_cell_height(x, y, "right", water_height, elevation_height)
    left_neighbor_cell_height = find_neighbor_cell_height(x, y, "left", water_height, elevation_height)
    up_neighbor_cell_height = find_neighbor_cell_height(x, y, "up", water_height, elevation_height)
    down_neighbor_cell_height = find_neighbor_cell_height(x, y, "down", water_height, elevation_height)
    this_cell_height = water_height[x,y] + elevation_height[x, y]

    if this_cell_height < right_neighbor_cell_height and this_cell_height < left_neighbor_cell_height and this_cell_height < up_neighbor_cell_height and this_cell_height < down_neighbor_cell_height:
        return True
    else:
        return False

    



    
def is_ponding_action(water_height, elevation_height, x, y, EV_cell):
    # right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    # left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    # up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    # down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)
    # current_cell_elevation_height = elevation_height[x,y]
    # min_value = min(value for value in [right_neighbor_elevation_height, left_neighbor_elevation_height, up_neighbor_elevation_height, down_neighbor_elevation_height] if value != -1)
    # difference = min_value - current_cell_elevation_height
    # cell_EV = water_height[x,y]

    # # if the distance between the lowest neighbor cell and the central cell is less than the EV of the central cell, then it will add all the EV to the elevation of the central cell
    # if difference > cell_EV:
    #     elevation_height[x,y] += cell_EV
    #     water_height[x,y] = 0
    # # otherwise, the elevation height of the central cell becomes the elevatino height of the lowest neighbor cell and the difference is subtracted from the EV of the cell
    # else:
    #     elevation_height[x,y] += difference
    #     water_height[x,y] -= difference
    #     water_height[x,y] = np.round(water_height[x,y], decimals=8)
    right_neighbor_cell_height = find_neighbor_cell_height(x, y, "right", water_height, elevation_height)
    left_neighbor_cell_height = find_neighbor_cell_height(x, y, "left", water_height, elevation_height)
    up_neighbor_cell_height = find_neighbor_cell_height(x, y, "up", water_height, elevation_height)
    down_neighbor_cell_height = find_neighbor_cell_height(x, y, "down", water_height, elevation_height)
    this_cell_height = water_height[x,y] + elevation_height[x, y]
    min_val = min(right_neighbor_cell_height, left_neighbor_cell_height, up_neighbor_cell_height, down_neighbor_cell_height)
    difference = this_cell_height - min_val
    if EV_cell > difference:
        water_height[x,y] += difference
        EV_cell[x,y] -= difference
    else:
        water_height += EV_cell[x,y]
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
    # existing_neighbors = get_existing_neighbors(x,y,elevation_height)
    # num = existing_neighbors.size()
    # # num is the number of neighbors that exist
    # split = 0
    # # checks if the condition is one where there is water level on each of the neighbour cells (1st condition) or not and splits the water level based on that
    # if water_height[x, find_neighbor(x,y,existing_neighbors[0], elevation_height)] > 0:
    #     split = ((water_height[x,y] + elevation_height[x,y]) - find_neighbor_cell_height(x,y,existing_neighbors[0], water_height, elevation_height)) / (existing_neighbors.size + 1)
    # else:
    #     split = (water_height[x,y]) / (existing_neighbors.size + 1)

        
    # if "right" in existing_neighbors:
    #     water_height[x, find_neighbor(x, y, "right", elevation_height)] += split
    #     water_height[x, find_neighbor(x, y, "right", elevation_height)] = np.round(water_height[x, find_neighbor(x, y, "right", elevation_height)], decimals=8)

    # if "left" in existing_neighbors:
    #     water_height[x, find_neighbor(x, y, "left", elevation_height)] += split
    #     water_height[x, find_neighbor(x, y, "left", elevation_height)] = np.round(water_height[x, find_neighbor(x, y, "left", elevation_height)], decimals=8)


    # if "up" in existing_neighbors:
    #     water_height[find_neighbor(x, y, "up", elevation_height), y] += split
    #     water_height[find_neighbor(x, y, "up", elevation_height), y] = np.round(water_height[find_neighbor(x, y, "up", elevation_height), y], decimals=8)


    # if "down" in existing_neighbors:
    #     water_height[find_neighbor(x, y, "down", elevation_height), y] += split
    #     water_height[find_neighbor(x, y, "down", elevation_height), y] = np.round(water_height[find_neighbor(x, y, "down", elevation_height), y], decimals=8)

    # if water_height[x, find_neighbor(x, y, "right", elevation_height)] < 0:
    #     water_height[x, find_neighbor(x,y, "right", elevation_height)]= 0
    # if water_height[x, find_neighbor(x, y, "left", elevation_height)] < 0:
    #     water_height[x, find_neighbor(x,y, "right", elevation_height)]= 0
    # if water_height[find_neighbor(x, y, "up", elevation_height), y] < 0:
    #     water_height[find_neighbor(x,y, "up", elevation_height), y]= 0
    # if water_height[find_neighbor(x, y, "down", elevation_height), y] < 0:
    #     water_height[find_neighbor(x,y, "down", elevation_height), y]= 0
    # if water_height[x,y] < 0:
    #     water_height[x,y] = 0

    # # the water height at the cell will become the water height originally minus the amount of water sent to the cells around it
    # water_height[x,y] -= existing_neighbors.size * split

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
    # this_elevation_height = elevation_height[x,y]
    # right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    # left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    # up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    # down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)

    # this_water_height = water_height[x,y]
    # right_neighbor_water_height = find_neighbor_water_height(x,y,"right", water_height)
    # left_neighbor_water_height = find_neighbor_water_height(x,y,"left", water_height)
    # up_neighbor_water_height = find_neighbor_water_height(x,y,"up", water_height)
    # down_neighbor_water_height = find_neighbor_water_height(x,y,"down", water_height)

    # equal_neighbors = get_equal_neighbors_dirs(x, y, elevation_height)
    # # if the number of equal neighbours is (0, 3]
    # if equal_neighbors.size <= 3 and equal_neighbors.size > 0:
    #     num = get_existing_neighbors(x, y, elevation_height).size - equal_neighbors.size
    #     num_less = 0
    #     # checks whether the values that the central cell does not equal are greater than the central cell
    #     if "right" not in equal_neighbors and right_neighbor_elevation_height > this_elevation_height:
    #         num_less += 1
    #     if "left" not in equal_neighbors and left_neighbor_elevation_height > this_elevation_height:
    #         num_less += 1
    #     if "up" not in equal_neighbors and up_neighbor_elevation_height > this_elevation_height:
    #         num_less += 1
    #     if "down" not in equal_neighbors and down_neighbor_elevation_height > this_elevation_height:
    #         num_less += 1


    #     if num_less == num:
    #         return True
    #     else:
    #         return False

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
    if "down" in  existing_neighbors and "down" not in equal_neighbors:
        if this_cell_height < down_neighbor_cell_height:
            num += 1

    if num + equal_neighbors.size == existing_neighbors.size:
        return True
    else:
        return False
    


        
# precondition is that the water_height of the central cell will always be greater than the increment constant
def is_increasing_level_action(water_height, elevation_height, x, y, increment_constant, EV_cell):
    # equal_neighbors = get_equal_neighbors_dirs(x, y, elevation_height)

    # orig_elevation_height = elevation_height[x,y]
    # orig_water_height = water_height[x,y]

    # elevation_height[x,y] += increment_constant 
    # water_height[x,y] -= increment_constant
    # water_height[x,y] = np.round(water_height[x,y], decimals=8)


    # right_neighbor_water_height = find_neighbor_water_height(x,y,"right", water_height)
    # left_neighbor_water_height = find_neighbor_water_height(x,y,"left", water_height)
    # up_neighbor_water_height = find_neighbor_water_height(x,y,"up", water_height)
    # down_neighbor_water_height = find_neighbor_water_height(x,y,"down", water_height)

    # if equal_neighbors.size != 0:
    #     split_val = water_height[x,y] / len(equal_neighbors)
    #     # checks all the values in equal neighbor and whether the original cell water height was greater than the neighbor cell water height
    #     # if so then it splits the water height into the amount necessary
    #     if "right" in equal_neighbors and orig_water_height > right_neighbor_water_height:
    #         water_height[x, find_neighbor(x,y,"right", elevation_height)] += split_val
    #         water_height[x, find_neighbor(x,y,"right", elevation_height)] = np.round(water_height[x, find_neighbor(x,y,"right", elevation_height)], decimals=8)

    #         water_height[x,y] -= split_val
    #         water_height[x,y] = np.round(water_height[x,y], decimals=8)

    #     if "left" in equal_neighbors and orig_water_height > left_neighbor_water_height:
    #         water_height[x, find_neighbor(x,y,"left", elevation_height)] += split_val
    #         water_height[x,find_neighbor(x,y,"left", elevation_height)] = np.round(water_height[x,find_neighbor(x,y,"left", elevation_height)], decimals=8)

    #         water_height[x,y] -= split_val
    #         water_height[x,y] = np.round(water_height[x,y], decimals=8)

    #     if "up" in equal_neighbors and orig_water_height > up_neighbor_water_height:
    #         water_height[find_neighbor(x,y,"up", elevation_height), y] += split_val
    #         water_height[find_neighbor(x,y,"up", elevation_height), y] = np.round(water_height[find_neighbor(x,y,"up", elevation_height), y], decimals=8)

    #         water_height[x,y] -= split_val
    #         water_height[x,y] = np.round(water_height[x,y], decimals=8)

    #     if "down" in equal_neighbors and orig_water_height > down_neighbor_water_height:
    #         water_height[find_neighbor(x,y,"down", elevation_height), y] += split_val
    #         water_height[find_neighbor(x,y,"down", elevation_height), y] = np.round(water_height[find_neighbor(x,y,"down", elevation_height), y], decimals=8)

    #         water_height[x,y] -= split_val
    #         water_height[x,y] = np.round(water_height[x,y], decimals=8)
        
    # if water_height[x, find_neighbor(x, y, "right", elevation_height)] < 0:
    #     water_height[x, find_neighbor(x,y, "right", elevation_height)]= 0
    # if water_height[x, find_neighbor(x, y, "left", elevation_height)] < 0:
    #     water_height[x, find_neighbor(x,y, "right", elevation_height)]= 0
    # if water_height[find_neighbor(x, y, "up", elevation_height), y] < 0:
    #     water_height[find_neighbor(x,y, "up", elevation_height), y]= 0
    # if water_height[find_neighbor(x, y, "down", elevation_height), y] < 0:
    #     water_height[find_neighbor(x,y, "down", elevation_height), y]= 0
    # if water_height[x,y] < 0:
    #     water_height[x,y] = 0
    water_height[x,y] += increment_constant
    EV_cell -= increment_constant
    equal_neighbors = get_equal_cell_height_neighbors(x,y,water_height, elevation_height)
    split = EV_cell /equal_neighbors.size
    
    if "right" in equal_neighbors:
        EV_cell[x, find_neighbor(x,y,"right", elevation_height)] += split

    if "left" in equal_neighbors:
        EV_cell[x, find_neighbor(x,y,"left", elevation_height)] += split


    if "up" in equal_neighbors:
        EV_cell[find_neighbor(x,y,"up", elevation_height), y] += split

    if "down" in equal_neighbors:
        EV_cell[find_neighbor(x,y,"down", elevation_height), y] += split

# i = 1 is northern cell
# i = 2 is eastern cell
# i = 3 is southern cell
# i = 4 is western cell
def is_partitioning_action(water_height, elevation_height, x, y, EV_cell):
    # right_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"right", elevation_height)
    # left_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"left", elevation_height)
    # up_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"up", elevation_height)
    # down_neighbor_elevation_height = find_neighbor_elevation_height(x,y,"down", elevation_height)

    # right_neighbor_water_height = find_neighbor_water_height(x,y,"right", water_height)
    # left_neighbor_water_height = find_neighbor_water_height(x,y,"left", water_height)
    # up_neighbor_water_height = find_neighbor_water_height(x,y,"up", water_height)
    # down_neighbor_water_height = find_neighbor_water_height(x,y,"down", water_height)

    # this_elevation_height = elevation_height[x,y]
    # this_water_height = water_height[x,y]

    # right_depth = 0
    # left_depth = 0
    # up_depth = 0
    # down_depth = 0

    # a = 0.09
    # b = 0.25

    # # calculates the increased height, hf
    # increased_height = a * water_height[x,y] ** b
    # increased_height = np.round(increased_height, decimals=8)

    # existing_sides = []

    # # calculates the d function in the caffé model
    # if right_neighbor_elevation_height != -1 and right_neighbor_elevation_height + right_neighbor_water_height < this_elevation_height + this_water_height:
    #     right_depth = max(0, this_elevation_height + increased_height - right_neighbor_elevation_height)
    #     right_depth = np.round(right_depth, decimals = 8)
    #     existing_sides.append("right")

    # if left_neighbor_elevation_height != -1 and left_neighbor_elevation_height + left_neighbor_water_height < this_elevation_height + this_water_height:
    #     left_depth = max(0, this_elevation_height + increased_height - left_neighbor_elevation_height)
    #     left_depth = np.round(left_depth, decimals = 8)
    #     existing_sides.append("left")

    # if up_neighbor_elevation_height != -1 and up_neighbor_elevation_height + up_neighbor_water_height < this_elevation_height + this_water_height:
    #     up_depth = max(0, this_elevation_height + increased_height - up_neighbor_elevation_height)
    #     up_depth = np.round(up_depth, decimals = 8)
    #     existing_sides.append("up")

    # if down_neighbor_elevation_height != -1 and down_neighbor_elevation_height + down_neighbor_water_height < this_elevation_height + this_water_height:
    #     down_depth = max(0, this_elevation_height + increased_height - down_neighbor_elevation_height)
    #     down_depth = np.round(down_depth, decimals = 8)
    #     existing_sides.append("down")

    # sum_depths = 0
    # # sums all the water depths up if the cell is indeed downstream
    # if "right" in existing_sides and right_depth > 0:
    #     sum_depths += right_depth
    # if "left" in existing_sides and left_depth > 0:
    #     sum_depths += left_depth
    # if "up" in existing_sides and up_depth > 0:
    #     sum_depths += up_depth
    # if "down" in existing_sides and down_depth > 0:
    #     sum_depths += down_depth
    
    # sum_depths = np.round(sum_depths, decimals = 8)
    # if sum_depths != 0:
    #     # calculates the weights of each neighbor cell and the water height at those cells after calculation
    #     if "right" in existing_sides:
    #         right_weight = right_depth / sum_depths
    #         water_height[x, find_neighbor(x,y,"right", elevation_height)] += right_weight * water_height[x,y]
    #         water_height[x, find_neighbor(x,y,"right", elevation_height)] = np.round(water_height[x, find_neighbor(x,y,"right", elevation_height)], decimals = 8)

    #     if "left" in existing_sides:
    #         left_weight = left_depth / sum_depths
    #         water_height[x, find_neighbor(x,y,"left", elevation_height)] = left_weight * water_height[x,y]
    #         water_height[x, find_neighbor(x,y,"left", elevation_height)] = np.round(water_height[x, find_neighbor(x,y,"left", elevation_height)], decimals = 8)

    #     if "up" in existing_sides:
    #         up_weight = up_depth / sum_depths
    #         water_height[find_neighbor(x,y,"up", elevation_height), y] = up_weight * water_height[x,y]
    #         water_height[find_neighbor(x,y,"up", elevation_height), y] = np.round(water_height[find_neighbor(x,y,"up", elevation_height), y], decimals = 8)

    #     if "down" in existing_sides:
    #         down_weight = down_depth / sum_depths
    #         water_height[find_neighbor(x,y,"down", elevation_height), y] = down_weight * water_height[x,y]
    #         water_height[find_neighbor(x,y,"down", elevation_height), y] = np.round(water_height[find_neighbor(x,y,"down", elevation_height), y], decimals = 8)

    #     water_height[x,y] = 0

    #     if water_height[x, find_neighbor(x, y, "right", elevation_height)] < 0:
    #         water_height[x, find_neighbor(x,y, "right", elevation_height)]= 0
    #     if water_height[x, find_neighbor(x, y, "left", elevation_height)] < 0:
    #         water_height[x, find_neighbor(x,y, "right", elevation_height)]= 0
    #     if water_height[find_neighbor(x, y, "up", elevation_height), y] < 0:
    #         water_height[find_neighbor(x,y, "up", elevation_height), y]= 0
    #     if water_height[find_neighbor(x, y, "down", elevation_height), y] < 0:
    #         water_height[find_neighbor(x,y, "down", elevation_height), y]= 0
    #     if water_height[x,y] < 0:
    #         water_height[x,y] = 0
    # else:
    #     return
    right_neighbor_cell_height = find_neighbor_cell_height(x,y,"right", water_height, elevation_height)
    left_neighbor_cell_height = find_neighbor_cell_height(x,y,"left", water_height, elevation_height)
    up_neighbor_cell_height = find_neighbor_cell_height(x,y,"up", water_height, elevation_height)
    down_neighbor_cell_height = find_neighbor_cell_height(x,y,"down", water_height, elevation_height)
    this_cell_height = water_height[x,y] + elevation_height[x,y]

    a = 0.09
    b = 0.25
    increased_height = a * EV_cell[x,y] ** b

    right_depth = -1
    left_depth = -1
    up_depth = -1
    down_depth = -1

    if right_neighbor_cell_height != -1:
        right_depth = max(0, right_neighbor_cell_height + increased_height - this_cell_height)
    if left_neighbor_cell_height != -1:
        right_depth = max(0, left_neighbor_cell_height + increased_height - this_cell_height)
    if up_neighbor_cell_height != -1:
        right_depth = max(0, up_neighbor_cell_height + increased_height - this_cell_height)
    if down_neighbor_cell_height != -1:
        right_depth = max(0, down_neighbor_cell_height + increased_height - this_cell_height)

    vals = [right_depth, left_depth, up_depth, down_depth]
    sum_result = sum(val for val in vals if val != -1)

    if right_depth != -1:
        weight = right_depth / sum_result
        EV_cell[x, find_neighbor(x,y,"right", elevation_height)] = weight * EV_cell[x,y]
    if left_depth != -1:
        weight = left_depth / sum_result
        EV_cell[x, find_neighbor(x,y,"left", elevation_height)] = weight * EV_cell[x,y]
    if up_depth != -1:
        weight = up_depth / sum_result
        EV_cell[find_neighbor(x,y,"up", elevation_height), y] = weight * EV_cell[x,y]
    if down_depth != -1:
        weight = down_depth / sum_result
        EV_cell[find_neighbor(x,y,"down", elevation_height), y] = weight * EV_cell[x,y]

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

def find_neighbor_cell_height(x,y,direction, water_height, elevation):
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


elevation_height = np.array([[2540, 2548, 2525, 2530, 2530, 2534, 2512, 2522, 2538], 
                             [2543, 2533, 2530, 2530, 2521, 2520, 2527, 2509, 2519],
                             [2533, 2533, 2533, 2523, 2523, 2536, 2507, 2510, 2527], 
                             [2509, 2533, 2509, 2530, 2502, 2514, 2527, 2510, 2522],
                             [2533, 2525, 2517, 2532, 2541, 2517, 2501, 2503, 2515], 
                             [2529, 2548, 2535, 2528, 2520, 2519, 2512, 2525, 2506],
                             [2529, 2508, 2533, 2506, 2549, 2523, 2546, 2509, 2514], 
                             [2533, 2508, 2508, 2503, 2526, 2508, 2530, 2541, 2547],
                             [2539, 2525, 2506, 2541, 2507, 2522, 2503, 2547, 2547]])
water_height = np.zeros((9,9))
x = 8
y = 8
water_height[8][8] = 20
water_height[7][8] = 10