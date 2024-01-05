import caffé
import numpy as np

input_asc = "/Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/pajaro2nd.asc" # Add directory to .asc file

def set_elevation_height(input_asc):
    with open(input_asc, 'r') as file:
        for _ in range(6):
            file.readline()
        
        data = np.loadtxt(file)
    
    return data

elevation_height = set_elevation_height(input_asc)
water_height = np.zeros([13,20])
water_height[5,5] = 4.72



