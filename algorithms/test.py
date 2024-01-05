import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors 
import caffé

input_asc = "/Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/pajaro2nd.asc" # Add directory to .asc file
# /Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/pajaro2nd.asc

def set_elevation_height(input_asc):
    with open(input_asc, 'r') as file:
        for _ in range(6):
            file.readline()
        
        data = np.loadtxt(file)
    
    return data

elevation_height = set_elevation_height(input_asc)
water_height = np.zeros([13,20])    
water_height[5,5] = 4.72
visited_cells = np.full((13, 20), '', dtype='str')

#user_x = int(input("Enter x value: "))

rgb_values = np.full((13, 20, 3), 255, dtype=int)


# Set RGB values for the single pixel
#rgb_values[3, 4] = [150, 170, 200]  # Set cell (3, 4) to the specified RGB color
#rgb_values[8, 12] = [255, 0, 0]
x = 1
y = 1
if "" in visited_cells:
    visited_cells[1, 1] = "visited"
    if caffé.is_do_nothing(water_height, x, y):
        print(0)
    elif caffé.is_ponding(water_height, elevation_height, x, y):
        print(1)


plt.figure()

plt.imshow(rgb_values, extent=[0, 20, 0, 13], origin='upper')
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='black')
plt.xticks(range(20 + 1))
plt.yticks(range(13 + 1))
plt.xlim(0, 20)
plt.ylim(0, 13)


plt.show()


