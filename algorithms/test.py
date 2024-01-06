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
x = 5
y = 19
water_height[x,y] = 20
increment_height = 7 # Change to user input later
# dangerous_level will be used for calculating which areas require evacuation more urgently
dangerous_level = 6 #change to user input later

def recursion_checking(water_height, elevation_height, x, y):
    if water_height[x,y] < dangerous_level and water_height[x,y] > 0:
        rgb_values[x,y] = [255,255,0]
    elif water_height[x,y] > dangerous_level:
        rgb_values[x,y] = [255,0,0]
    else:
        rgb_values[x,y] = [0,0,0]

    if caffé.is_do_nothing(water_height, x, y):
        print(1)
        return
    elif caffé.is_ponding(water_height, elevation_height, x, y):
        caffé.is_ponding_action(water_height, elevation_height, x, y)

        if water_height[x, y] > 0:
            print(water_height[x,y])
            print(elevation_height[x,y])
            #recursion_checking(water_height, elevation_height, x, y)=
    elif caffé.is_spreading(water_height, elevation_height, x, y):
        caffé.is_spreading_action(water_height, elevation_height, x, y)
        right_neighbor_water_height = caffé.find_neighbor_water_height(x, y, "right", water_height)
        left_neighbor_water_height = caffé.find_neighbor_water_height(x, y, "left", water_height)
        up_neighbor_water_height = caffé.find_neighbor_water_height(x, y, "up", water_height)
        down_neighbor_water_height = caffé.find_neighbor_water_height(x, y, "down", water_height)
        
        if right_neighbor_water_height != -1:
            print(1)
            #recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x, y, "right", elevation_height))
        if left_neighbor_water_height != -1:
            print(2)
            #recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x, y, "left", elevation_height))
        if up_neighbor_water_height != -1:
            print(3)
            #recursion_checking(water_height, elevation_height, caffé.find_neighbor(x, y, "up", elevation_height), y)
        if down_neighbor_water_height != -1:
            print(4)
            #recursion_checking(water_height, elevation_height, caffé.find_neighbor(x, y, "down", elevation_height), y)
    elif caffé.is_increasing_level(water_height, elevation_height, x, y):
        equal_neighbors = caffé.get_equal_neighbors_dirs(x, y, elevation_height)

        caffé.is_increasing_level_action(water_height, elevation_height, x, y, increment_height)

        if "right" in equal_neighbors:
            print(1)
            #recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x, y, "right", elevation_height))

        if "left" in equal_neighbors:
            print(2)
            #recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x, y, "left", elevation_height))

        if "up" in equal_neighbors:
            print(3)
            #recursion_checking(water_height, elevation_height, caffé.find_neighbor(x, y, "up", elevation_height), y)

        if "down" in equal_neighbors:
            print(4)
            #recursion_checking(water_height, elevation_height, caffé.find_neighbor(x, y, "right", elevation_height), y)
    else:
        caffé.is_partitioning_action(water_height, elevation_height, x, y)
        print(5)

        if water_height[x, caffé.find_neighbor(x,y,"right", elevation_height)] > 0:
            print(1)
            #recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x,y,"right", elevation_height))

        if water_height[x, caffé.find_neighbor(x,y,"left", elevation_height)] > 0:
            print(2)
            #recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x,y,"left", elevation_height))

        if water_height[caffé.find_neighbor(x,y,"up", elevation_height), y] > 0:
            print(3)
            #recursion_checking(water_height, elevation_height, caffé.find_neighbor(x,y,"up", elevation_height), y)
        
        if water_height[caffé.find_neighbor(x,y,"down", elevation_height), y] > 0:
            print(4)
            #recursion_checking(water_height, elevation_height, caffé.find_neighbor(x,y,"down", elevation_height), y)


print(recursion_checking(water_height, elevation_height, x, y))
#print(caffé.is_increasing_level(water_height, elevation_height, x, y))

plt.figure()

plt.imshow(rgb_values, extent=[0, 20, 0, 13], origin='upper')
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='black')
plt.xticks(range(20 + 1))
plt.yticks(range(13 + 1))
plt.xlim(0, 20) 
plt.ylim(0, 13)


plt.show()


