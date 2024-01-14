import numpy as np
import time
import matplotlib
import math

input_asc = "C:/Users/saman/OneDrive/Documents/GitHub/Synopsys_2024/.asc files/sunnyvale.asc"
increment_constant = 5 # Change to user input
a = 5 # constant
b = 5 # constant
elevation = [[]]
num_rows = 0
num_cols = 0
water_height = [[]]
cell_height = [[]]
cell_EV = [[]]

def initialize():
    elevation = [[]]
    with open(input_asc, 'r') as file:
        for _ in range(6):
            content = file.readline()
        
        elevation = np.loadtxt(file)

    num_rows = len(elevation)
    num_cols = len(elevation[0]) if num_rows > 0 else 0

    water_height = [[0] * num_cols for _ in range(num_rows)]
    cell_height = [[0] * num_cols for _ in range(num_rows)]
    cell_EV = [[0] * num_cols for _ in range(num_rows)]

def define_cellheight():
    for x in num_rows:
        for y in num_cols:
            cell_height[x, y] = elevation[x, y] + water_height[x, y]


# EV is defined by surrounding neighbor height
# Cell height = cell elevation + water height

def find_neighbor_elevation(x, y, string):
    if string == "right":
        return elevation[x + 1, y]
    elif string == "left":
        return elevation[x - 1, y] 
    elif string == "up":
        return elevation[x, y - 1]
    elif string == "down":
        return elevation[x, y + 1]

def define_cellEV(): 
    for x in num_rows:
        for y in num_cols:
            cc_cellheight = cell_height[x, y]
            right_neighbour_height = find_neighbor_elevation(x, y, "right")
            left_neighbour_height = find_neighbor_elevation(x, y, "left")
            up_neighbour_height = find_neighbor_elevation(x, y, "up")
            down_neighbour_height = find_neighbor_elevation(x, y, "down")

            smallest_height = min(cc_cellheight, right_neighbour_height, left_neighbour_height, up_neighbour_height, down_neighbour_height)

            if smallest_height == cc_cellheight:
                cell_EV[x, y] = 0
            else:
                difference = cc_cellheight - smallest_height
                if difference > water_height[x, y]:
                    cell_EV[x, y] = water_height[x, y]
                else:
                    cell_EV[x, y] = difference



#Rule 0
def do_nothing(x, y):
    if cell_EV[x, y] == 0:
        return True # End Sim
    return False

#Rule 1

def check_ponding(x, y): # Check
    cc_cellheight = elevation[x, y] + water_height[x, y]
    right_neighbour_height = find_neighbor_elevation(x, y, "right")
    left_neighbour_height = find_neighbor_elevation(x, y, "left")
    up_neighbour_height = find_neighbor_elevation(x, y, "up")
    down_neighbour_height = find_neighbor_elevation(x, y, "down")

    if right_neighbour_height > cc_cellheight and left_neighbour_height > cc_cellheight and up_neighbour_height > cc_cellheight and down_neighbour_height > cc_cellheight:
        lowest_neighbour_height = min(right_neighbour_height, left_neighbour_height, up_neighbour_height, down_neighbour_height)
        difference = lowest_neighbour_height - cc_cellheight

        if difference > cell_EV[x, y]:
            water_height[x, y] = cell_EV[x, y]

        water_height[x, y] += difference 
        cell_EV[x, y] -= difference

    else:
        return

def check_spreading(x, y):
    cc_cellheight = elevation[x, y] + water_height[x, y]
    right_neighbour_height = find_neighbor_elevation(x, y, "right")
    left_neighbour_height = find_neighbor_elevation(x, y, "left")
    up_neighbour_height = find_neighbor_elevation(x, y, "up")
    down_neighbour_height = find_neighbor_elevation(x, y, "down")

    if right_neighbour_height == left_neighbour_height == up_neighbour_height == down_neighbour_height == cc_cellheight:
        cell_to_spread = cell_EV[x, y] // 5
        cell_EV[x, y] = cell_to_spread
        cell_EV[x + 1, y] = cell_to_spread
        cell_EV[x - 1, y] = cell_to_spread
        cell_EV[x, y + 1] = cell_to_spread
        cell_EV[x, y - 1] = cell_to_spread
    else:
        return

def check_increasinglevel(x, y):
    cc_cellheight = elevation[x, y] + water_height[x, y]
    right_neighbour_height = find_neighbor_elevation(x, y, "right")
    left_neighbour_height = find_neighbor_elevation(x, y, "left")
    up_neighbour_height = find_neighbor_elevation(x, y, "up")
    down_neighbour_height = find_neighbor_elevation(x, y, "down")

    variables_to_compare = [right_neighbour_height, left_neighbour_height, up_neighbour_height, down_neighbour_height]
    count = 0
    for v in variables_to_compare:
        if cc_cellheight == v: 
            count += 1 # Must know which ones are here

    
    
def check_partioning(x, y):
    # Calculate downstream neighbors?
    cc_cellheight = elevation[x, y] + water_height[x, y]
    right_neighbour_height = find_neighbor_elevation(x, y, "right")
    left_neighbour_height = find_neighbor_elevation(x, y, "left")
    up_neighbour_height = find_neighbor_elevation(x, y, "up")
    down_neighbour_height = find_neighbor_elevation(x, y, "down")

    # Calculating downstream neighbours
    sum_result = 0
    hf = a * cell_EV[x, y] ** b
    di = max(0, cell_height[x, y] + hf - right_neighbour_height) # For right neighbor, do for all

    sum_result += di
    sum_result += max(0, cell_height[x, y] + hf - left_neighbour_height)
    sum_result += max(0, cell_height[x, y] + hf - up_neighbour_height)
    sum_result += max(0, cell_height[x, y] + hf - down_neighbour_height)

    wi = di / sum_result
    cell_EV[x + 1, y] += wi * cell_EV[x + 1, y] # Do this for neighbors?



def main():
    initialize()
    define_cellheight()
    define_cellEV()

    run = True

    while run:
        if do_nothing() == False:
            run = False
        
        check_ponding()

        # Update visual

        check_spreading()

        # update visual

        check_increasinglevel()

        # update visual

        check_partioning()
        # update visual



