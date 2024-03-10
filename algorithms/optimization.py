#When finished flood simulation

import numpy as np
import heapq
import json
import test
from scipy.ndimage import gaussian_filter
from scipy.ndimage import map_coordinates
from collections import deque    

normal_speed = 1.4
start = (0,0) # change accordingly
building_map = []
filepath = "" # specify path to building data
elevation = []
water_levels = []
building_data = []
safezones = []
safezones_coords = []

def find_path():
    global normal_speed, start, building_map, filepath, elevation, water_levels, building_data, safezones, safezones_coords
    normal_speed = 1.4
    start = (0, 1) # change accordingly
    end = (2, 7)
    building_map = []

    filepath = "C:/Users/saman/OneDrive/Documents/GitHub/Synopsys_2024/algorithms/plesbuildings.geojson" # specify path to building data

    elevation = test.get_elevation_height()
    water_levels = test.get_water_heights()
    building_data = []

    load_building_data()
    
    building_map = test.get_bmap()    

    safezones = np.where(water_levels <= 0.1)
    safezones_coords = list(zip(safezones[0], safezones[1]))

    np.savetxt("elevation_height.txt", building_map, fmt='%d', delimiter=' ', newline='\n')

    #for end in safezones_coords:
     #   shortest = find_paths(building_map, start, end)
      #  print(shortest)
    
    #print(shortest)


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
    

"""
def calculate_time(speed, elevation, water_depth):
    walking_speed = 2 - 0.011 * water_depth
    
    if elevation >= 0:
        time = speed / walking_speed + 0.1 * elevation
    elif -5 <= elevation < 0:
        time = speed / walking_speed
    elif -12 <= elevation < -5:
        time = speed / walking_speed - 0.03 * elevation
    else:
        time = speed / walking_speed + 0.03 * elevation
        
    return time
"""

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

def calculate_time(path):
    return len(path) * 30 / 1.4  # Each cell is 30m, walking speed is 1.4 m/s

def find_paths(building_map, start, end):
    rows = len(building_map)
    cols = len(building_map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    paths = []
    queue = [((start[0], start[1]), [start])]  # Queue of (coordinate, path) tuples

    while queue:
        (current_row, current_col), current_path = queue.pop(0)
        visited[current_row][current_col] = True

        if (current_row, current_col) == end:
            paths.append((current_path, str(calculate_time(current_path)) + "s"))
            continue

        for neighbor_row, neighbor_col in get_neighbors(building_map, visited, current_row, current_col):
            queue.append(((neighbor_row, neighbor_col), current_path + [(neighbor_row, neighbor_col)]))

    return paths







        
