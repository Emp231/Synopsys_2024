import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors 
import caffé

#input_asc = "/Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/pajaro2nd.asc" # Add directory to .asc file
# /Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/pajaro2nd.asc

def set_elevation_height(input_asc):
    with open(input_asc, 'r') as file:
        for _ in range(6):
            file.readline()
        
        data = np.loadtxt(file)
    
    return data

#elevation_height = set_elevation_height(input_asc)
water_height = np.zeros([5,5])    
visited_cells = np.full((13, 20), '', dtype='str')

#user_x = int(input("Enter x value: "))

rgb_values = np.full((13, 20, 3), 255, dtype=int)


# Set RGB values for the single pixel
#rgb_values[3, 4] = [150, 170, 200]  # Set cell (3, 4) to the specified RGB color
#rgb_values[8, 12] = [255, 0, 0]
x = 2
y = 2
water_height[x,y] = 20

increment_height = 1 # Change to user input later
# dangerous_level will be used for calculating which areas require evacuation more urgently
dangerous_level = 6 #change to user input later
"""
def recursion_checking(water_height, elevation_height, x, y):
    
    if water_height[x,y] < dangerous_level and water_height[x,y] > 0:
        rgb_values[x,y] = [255,255,0]
    elif water_height[x,y] > dangerous_level:
        rgb_values[x,y] = [255,0,0]
    elif water_height[x,y] == 0:
        rgb_values[x,y] = [0,0,0]

    if caffé.is_do_nothing(water_height, x, y):
        return
    elif caffé.is_ponding(water_height, elevation_height, x, y):
        caffé.is_ponding_action(water_height, elevation_height, x, y)

        if water_height[x, y] > 0:
            recursion_checking(water_height, elevation_height, x, y)

    elif caffé.is_spreading(water_height, elevation_height, x, y):
        caffé.is_spreading_action(water_height, elevation_height, x, y)
        right_neighbor_water_height = caffé.find_neighbor_water_height(x, y, "right", water_height)
        left_neighbor_water_height = caffé.find_neighbor_water_height(x, y, "left", water_height)
        up_neighbor_water_height = caffé.find_neighbor_water_height(x, y, "up", water_height)
        down_neighbor_water_height = caffé.find_neighbor_water_height(x, y, "down", water_height)
        
        if right_neighbor_water_height != -1:
            recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x, y, "right", elevation_height))
        if left_neighbor_water_height != -1:
            recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x, y, "left", elevation_height))
        if up_neighbor_water_height != -1:

            recursion_checking(water_height, elevation_height, caffé.find_neighbor(x, y, "up", elevation_height), y)
        if down_neighbor_water_height != -1:
            recursion_checking(water_height, elevation_height, caffé.find_neighbor(x, y, "down", elevation_height), y)

        if water_height[x,y] != -1 and water_height[x,y] > 2:
            recursion_checking(water_height, elevation_height, x, y)

    elif caffé.is_increasing_level(water_height, elevation_height, x, y):
        equal_neighbors = caffé.get_equal_neighbors_dirs(x, y, elevation_height)

        caffé.is_increasing_level_action(water_height, elevation_height, x, y, increment_height)

        if "right" in equal_neighbors:

            recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x, y, "right", elevation_height))

        if "left" in equal_neighbors:

            recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x, y, "left", elevation_height))

        if "up" in equal_neighbors:

            recursion_checking(water_height, elevation_height, caffé.find_neighbor(x, y, "up", elevation_height), y)

        if "down" in equal_neighbors:
            recursion_checking(water_height, elevation_height, caffé.find_neighbor(x, y, "right", elevation_height), y)
    else:
        caffé.is_partitioning_action(water_height, elevation_height, x, y)

        if water_height[x, caffé.find_neighbor(x,y,"right", elevation_height)] > 0:

            recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x,y,"right", elevation_height))

        if water_height[x, caffé.find_neighbor(x,y,"left", elevation_height)] > 0:

            recursion_checking(water_height, elevation_height, x, caffé.find_neighbor(x,y,"left", elevation_height))

        if water_height[caffé.find_neighbor(x,y,"up", elevation_height), y] > 0:

            recursion_checking(water_height, elevation_height, caffé.find_neighbor(x,y,"up", elevation_height), y)
        
        if water_height[caffé.find_neighbor(x,y,"down", elevation_height), y] > 0:

            recursion_checking(water_height, elevation_height, caffé.find_neighbor(x,y,"down", elevation_height), y)


recursion_checking(water_height, elevation_height, x, y)
#print(caffé.is_partitioning_action(water_height, elevation_height, 0, 0))
print(water_height[0,0])
"""
"""
def recursion_checking(water_height, elevation_height, x, y):
    if caffé.is_do_nothing(water_height, x, y):
        print(0)
        return
    elif caffé.is_ponding(water_height, elevation_height, x, y):
        caffé.is_ponding_action(water_height, elevation_height, x, y)
        print(1)
    elif caffé.is_spreading(water_height, elevation_height, x, y):
        print(2)
    elif caffé.is_increasing_level(water_height, elevation_height, x, y):
        print(3)
    else:
        caffé.is_partitioning_action(water_height, elevation_height, x, y)
        differences = []
        right_neighbor_elevation_height = caffé.find_neighbor_elevation_height(x, y, "right", elevation_height)
        left_neighbor_elevation_height = caffé.find_neighbor_elevation_height(x, y, "left", elevation_height)
        up_neighbor_elevation_height = caffé.find_neighbor_elevation_height(x, y, "up", elevation_height)
        down_neighbor_elevation_height = caffé.find_neighbor_elevation_height(x, y, "down", elevation_height)

        if right_neighbor_elevation_height != -1:
            differences.append(elevation_height[x,y] - right_neighbor_elevation_height)
        if left_neighbor_elevation_height != -1:
            differences.append(elevation_height[x,y] - left_neighbor_elevation_height)
        if up_neighbor_elevation_height != -1:
            differences.append(elevation_height[x,y] - up_neighbor_elevation_height)
        if down_neighbor_elevation_height != -1:
            differences.append(elevation_height[x,y] - down_neighbor_elevation_height)
        
        max_val = max(differences)
        if differences[0] == max_val:
            print(0)
            #recursive method
        if differences[1] == max_val:
            print(1)
            #recursive method
        if differences[2] == max_val:
            print(2)
            #recursive method
        if differences[3] == max_val:
            print(3)
            #recursive method
"""
def recursion_checking(water_height, elevation_height, list_points):
    new_list_points = np.empty((0, 2), dtype=int)
    print(list_points)
    for point in list_points:
        x = point[0]
        y = point[1]
        if water_height[x,y] == 0:
            return
        elif caffé.is_ponding(water_height, elevation_height, x, y):
            caffé.is_ponding_action(water_height, elevation_height, x, y)
            equal_neighbors = caffé.get_equal_neighbors_dirs(x, y, elevation_height)

            if "right" in equal_neighbors:
                new_list_points = np.append(new_list_points, np.array([[x, caffé.find_neighbor(x, y, "right", elevation_height)]]), axis=0)
            if "left" in equal_neighbors:
                new_list_points = np.append(new_list_points, np.array([[x, caffé.find_neighbor(x, y, "left", elevation_height)]]), axis=0)
            if "up" in equal_neighbors:
                new_list_points = np.append(new_list_points, np.array([[caffé.find_neighbor(x, y, "up", elevation_height), y]]), axis=0)
            if "down" in equal_neighbors:
                new_list_points = np.append(new_list_points, np.array([[caffé.find_neighbor(x, y, "down", elevation_height), y]]), axis=0)
        elif caffé.is_spreading(water_height, elevation_height, x, y):
            caffé.is_spreading_action(water_height, elevation_height, x, y)
            existing_neighbors = caffé.get_existing_neighbors(x,y, elevation_height)
            if "right" in existing_neighbors:
                new_list_points = np.append(new_list_points, np.array([[x, caffé.find_neighbor(x, y, "right", elevation_height)]]), axis=0)
            if "left" in existing_neighbors:
                new_list_points = np.append(new_list_points, np.array([[x, caffé.find_neighbor(x, y, "left", elevation_height)]]), axis=0)
            if "up" in existing_neighbors:
                new_list_points = np.append(new_list_points, np.array([[caffé.find_neighbor(x, y, "up", elevation_height), y]]), axis=0)
            if "down" in existing_neighbors:
                new_list_points = np.append(new_list_points, np.array([[caffé.find_neighbor(x, y, "down", elevation_height), y]]), axis=0)
            
            new_list_points = np.append(new_list_points, np.array([[x,y]]), axis=0)

        elif caffé.is_increasing_level(water_height, elevation_height, x, y):
            equal_neighbors = caffé.get_equal_neighbors_dirs(x, y, elevation_height)
            caffé.is_increasing_level_action(water_height, elevation_height, x, y, increment_height)
            if "right" in equal_neighbors:
                new_list_points = np.append(new_list_points, np.array([[x, caffé.find_neighbor(x, y, "right", elevation_height)]]), axis=0)
            if "left" in equal_neighbors:
                new_list_points = np.append(new_list_points, np.array([[x, caffé.find_neighbor(x, y, "left", elevation_height)]]), axis=0)
            if "up" in equal_neighbors:
                new_list_points = np.append(new_list_points, np.array([[caffé.find_neighbor(x, y, "up", elevation_height), y]]), axis=0)
            if "down" in equal_neighbors:
                new_list_points = np.append(new_list_points, np.array([[caffé.find_neighbor(x, y, "down", elevation_height), y]]), axis=0)
        else:
            caffé.is_partitioning_action(water_height, elevation_height, x, y)
            existing_neighbors = caffé.get_existing_neighbors(x,y, elevation_height)
            if "right" in existing_neighbors:
                new_list_points = np.append(new_list_points, np.array([[x, caffé.find_neighbor(x, y, "right", elevation_height)]]), axis=0)
            if "left" in existing_neighbors:
                new_list_points = np.append(new_list_points, np.array([[x, caffé.find_neighbor(x, y, "left", elevation_height)]]), axis=0)
            if "up" in existing_neighbors:
                new_list_points = np.append(new_list_points, np.array([[caffé.find_neighbor(x, y, "up", elevation_height), y]]), axis=0)
            if "down" in existing_neighbors:
                new_list_points = np.append(new_list_points, np.array([[caffé.find_neighbor(x, y, "down", elevation_height), y]]), axis=0)
        print(water_height)
    print("-----")
    new_list_points = np.unique(new_list_points, axis = 0)
    if new_list_points.shape[0] > 0:
        recursion_checking(water_height, elevation_height, new_list_points)

orig_points = np.array([[x,y]])
elevation_height = np.array([
    [9, 8, 11,12,7],
    [8, 8, 8, 11,14],
    [7, 8, 10,7, 8],
    [8, 9, 7, 7, 7],
    [10,9, 8, 7, 8]
])

recursion_checking(water_height, elevation_height, orig_points)
#print(caffé.get_equal_neighbors_dirs(3,2, elevation_height))
"""
plt.figure()

plt.imshow(rgb_values, extent=[0, 20, 0, 13], origin='upper')
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='black')
plt.xticks(range(20 + 1))
plt.yticks(range(13 + 1))
plt.xlim(0, 20) 
plt.ylim(0, 13)
plt.show()
"""


