#When finished flood simulation

import numpy as np
import heapq
import matplotlib.pyplot as plt
import json
import test
from scipy.ndimage import gaussian_filter
from scipy.ndimage import map_coordinates
from collections import deque    
import math

normal_speed = 1.4
start = (32,23)
building_map = []
filepath = "" 
elevation = []
water_levels = []
building_data = []
safezones = []
safezones_coords = []
evac_time = 0

def find_path():
    all_paths = []
    global normal_speed, start, building_map, filepath, elevation, water_levels, building_data, safezones, safezones_coords, evac_time
    normal_speed = 1.4
    start = (32, 23) # change accordingly
    building_map = []

    filepath = "C:/Users/saman/OneDrive/Documents/GitHub/Synopsys_2024/algorithms/plesbuildings.geojson" # specify path to building data

    elevation = test.get_elevation_height()
    water_levels = test.get_water_heights()
    building_data = []
    evac_time = 0

    load_building_data()
    
    building_map = test.get_bmap()    

    safezones = np.where(water_levels <= 0.1)
    safezones_coords = list(zip(safezones[0], safezones[1]))

    np.savetxt("elevation_height.txt", building_map, fmt='%d', delimiter=' ', newline='\n')

    for end in safezones_coords:
        if building_map[end] == 1:
            path = find_paths(building_map, start, end)
            all_paths.append(path)

    shortest_t = 10000000000
    shortest_path = []

    for path_group in all_paths:
    # Iterate over each path in the group
        for path_info in path_group:
            # Unpack the path coordinates and time
            path, time_taken = path_info[0], path_info[1]
            # Update shortest_time and shortest_path if current path has shorter time
            if time_taken < shortest_t:
                shortest_t = time_taken
                shortest_path = path

    return shortest_path

def load_building_data():
    global building_data
    with open(filepath, 'r') as file:
        data = json.load(file)
        building_data = np.array([feature['geometry']['coordinates'] for feature in data['features']])

def map_buildings():
    global building_map
    min_lat = min(coord[0] for coord in building_data)
    max_lat = max(coord[0] for coord in building_data)
    min_lon = min(coord[1] for coord in building_data)
    max_lon = max(coord[1] for coord in building_data)

    lat_diff = max_lat - min_lat
    lon_diff = max_lon - min_lon
    num_rows = len(elevation)
    num_cols = len(elevation[0]) 

    array = np.zeros((num_rows, num_cols))
    for lat, lon in building_data:
        row = int((lat - min_lat) / 0.0003)
        col = int((lon - min_lon) / 0.0003)
        
        if row >= 0 and row < num_rows and col >= 0 and col < num_cols:
            array[row, col] = 1  

    building_map = array


def is_valid_move(building_map, visited, row, col):
    rows = len(building_map)
    cols = len(building_map[0])
    return (row >= 0 and row < rows and col >= 0 and col < cols and building_map[row][col] != 0 and not visited[row][col])

def get_neighbors(building_map, visited, row, col):
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if is_valid_move(building_map, visited, new_row, new_col):
            neighbors.append((new_row, new_col))
    return neighbors

def calculate_time(diff, water_depth):
    angle = math.degrees(math.atan2(diff, 30))
    x = 0
    walk_time = 30 / 1.4

    if angle > 0:
        x = walk_time + 0.1 * diff
    elif -5 <= angle <= 0:
        x = walk_time
    elif -12 <= angle < -5:
        x = walk_time - 0.03 * diff
    else:
        x = walk_time + 0.03 * diff

    walkspeed = 2 - 0.011 * water_depth
    x += 30 / walkspeed
    return x


def find_paths(building_map, start, end):
    global evac_time
    rows = len(building_map)
    cols = len(building_map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    paths = []
    queue = [((start[0], start[1]), [start])]

    while queue:
        (current_row, current_col), current_path = queue.pop(0)
        visited[current_row][current_col] = True

        if (current_row, current_col) == end:
            paths.append((current_path, evac_time))
            evac_time = 0
            continue

        for neighbor_row, neighbor_col in get_neighbors(building_map, visited, current_row, current_col):
            elev_diff = elevation[current_row][current_col] - elevation[neighbor_row][neighbor_col]
            evac_time += calculate_time(elev_diff, water_levels[current_row][current_col])
            queue.append(((neighbor_row, neighbor_col), current_path + [(neighbor_row, neighbor_col)]))

    return paths







        
