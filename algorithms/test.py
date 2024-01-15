import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors 
import caffé
import time

input_asc = "/Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/pajaro2nd.asc" # Add directory to .asc file
# /Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/pajaro2nd.asc

def set_elevation_height(input_asc):
    with open(input_asc, 'r') as file:
        for _ in range(6):
            file.readline()
        
        data = np.loadtxt(file)
    
    return data


#user_x = int(input("Enter x value: "))




# dangerous_level will be used for calculating which areas require evacuation more urgently

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
"""
def recursion_checking(water_height, elevation_height, list_points):
    new_list_points = np.empty((0, 2), dtype=int)
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

    new_list_points = np.unique(new_list_points, axis = 0)
    if new_list_points.shape[0] > 0:
        recursion_checking(water_height, elevation_height, new_list_points)
"""


x = 0
y = 0


elevation_height = set_elevation_height(input_asc)

water_height = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells[x,y] = 10

dangerous_level = 6 #change to user input later
#Set RGB values for the single pixel
increment_height = 1 # Change to user input later

rgb_values = np.full((elevation_height.shape[0], elevation_height.shape[1], 3), 255, dtype=int)


plt.figure()

img = plt.imshow(rgb_values, extent=[0, 20, 0, 13], origin='upper')
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='black')
plt.xticks(range(20 + 1))
plt.yticks(range(13 + 1))
plt.xlim(0, 20) 
plt.ylim(0, 13)


def recursion_checking(water_height, elevation_height, list_points, EV_cells, increment_constant, rgb_values, dangerous_level):
    # list_points is the list of points that the program will run through for simulation every iteration
    while list_points.size > 0:
        new_list_points = np.empty((0, 2), dtype=object)

        if caffé.end_sim(EV_cells, 2):
            break
    
        for point in list_points:
            cur_x = np.atleast_1d(point)[0]
            cur_y = np.atleast_1d(point)[1]



            if caffé.is_do_nothing(EV_cells, cur_x, cur_y):
                continue
            elif caffé.is_ponding(water_height, elevation_height, cur_x, cur_y, EV_cells):
                caffé.is_ponding_action(water_height, elevation_height, cur_x, cur_y, EV_cells)
                existing_neighbors = caffé.get_existing_neighbors(cur_x,cur_y,elevation_height)
                if "right" in existing_neighbors and EV_cells[cur_x][caffé.find_neighbor(cur_x, cur_y, "right", elevation_height)] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, caffé.find_neighbor(cur_x, cur_y, "right", elevation_height)]])
                if "left" in existing_neighbors and EV_cells[cur_x][caffé.find_neighbor(cur_x, cur_y, "left", elevation_height)] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, caffé.find_neighbor(cur_x, cur_y, "left", elevation_height)]])
                if "up" in existing_neighbors and EV_cells[caffé.find_neighbor(cur_x, cur_y, "up", elevation_height)][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [caffé.find_neighbor(cur_x, cur_y, "up", elevation_height), cur_y]])
                if "down" in existing_neighbors and EV_cells[caffé.find_neighbor(cur_x, cur_y, "down", elevation_height)][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [caffé.find_neighbor(cur_x, cur_y, "down", elevation_height), cur_y]])

                if EV_cells[cur_x][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, cur_y]])
            elif caffé.is_spreading(water_height, elevation_height, cur_x, cur_y):
                caffé.is_spreading_action(water_height, elevation_height, cur_x, cur_y, EV_cells)
                existing_neighbors = caffé.get_existing_neighbors(cur_x,cur_y,elevation_height)
                if "right" in existing_neighbors and EV_cells[cur_x][caffé.find_neighbor(cur_x, cur_y, "right", elevation_height)] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, caffé.find_neighbor(cur_x, cur_y, "right", elevation_height)]])
                if "left" in existing_neighbors and EV_cells[cur_x][caffé.find_neighbor(cur_x, cur_y, "left", elevation_height)] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, caffé.find_neighbor(cur_x, cur_y, "left", elevation_height)]])
                if "up" in existing_neighbors and EV_cells[caffé.find_neighbor(cur_x, cur_y, "up", elevation_height)][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [caffé.find_neighbor(cur_x, cur_y, "up", elevation_height), cur_y]])
                if "down" in existing_neighbors and EV_cells[caffé.find_neighbor(cur_x, cur_y, "down", elevation_height)][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [caffé.find_neighbor(cur_x, cur_y, "down", elevation_height), cur_y]])

                if EV_cells[cur_x][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, cur_y]])

            elif caffé.is_increasing_level(water_height, elevation_height, cur_x, cur_y):
                caffé.is_increasing_level_action(water_height, elevation_height, cur_x, cur_y, increment_constant, EV_cells)
                existing_neighbors = caffé.get_existing_neighbors(cur_x,cur_y,elevation_height)
                if "right" in existing_neighbors and EV_cells[cur_x][caffé.find_neighbor(cur_x, cur_y, "right", elevation_height)] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, caffé.find_neighbor(cur_x, cur_y, "right", elevation_height)]])
                if "left" in existing_neighbors and EV_cells[cur_x][caffé.find_neighbor(cur_x, cur_y, "left", elevation_height)] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, caffé.find_neighbor(cur_x, cur_y, "left", elevation_height)]])
                if "up" in existing_neighbors and EV_cells[caffé.find_neighbor(cur_x, cur_y, "up", elevation_height)][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [caffé.find_neighbor(cur_x, cur_y, "up", elevation_height), cur_y]])
                if "down" in existing_neighbors and EV_cells[caffé.find_neighbor(cur_x, cur_y, "down", elevation_height)][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [caffé.find_neighbor(cur_x, cur_y, "down", elevation_height), cur_y]])

                if EV_cells[cur_x][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, cur_y]])
            else:
                caffé.is_partitioning_action(water_height, elevation_height, cur_x, cur_y, EV_cells)
                existing_neighbors = caffé.get_existing_neighbors(cur_x,cur_y,elevation_height)
                if "right" in existing_neighbors and EV_cells[cur_x][caffé.find_neighbor(cur_x, cur_y, "right", elevation_height)] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, caffé.find_neighbor(cur_x, cur_y, "right", elevation_height)]])
                if "left" in existing_neighbors and EV_cells[cur_x][caffé.find_neighbor(cur_x, cur_y, "left", elevation_height)] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, caffé.find_neighbor(cur_x, cur_y, "left", elevation_height)]])
                if "up" in existing_neighbors and EV_cells[caffé.find_neighbor(cur_x, cur_y, "up", elevation_height)][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [caffé.find_neighbor(cur_x, cur_y, "up", elevation_height), cur_y]])
                if "down" in existing_neighbors and EV_cells[caffé.find_neighbor(cur_x, cur_y, "down", elevation_height)][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [caffé.find_neighbor(cur_x, cur_y, "down", elevation_height), cur_y]])

                if EV_cells[cur_x][cur_y] > 0:
                    new_list_points = np.vstack([new_list_points, [cur_x, cur_y]])
            np.set_printoptions(precision=8, suppress=True)  # Set precision and suppress small values

        rgb_values[EV_cells >= dangerous_level] = [255, 0, 255]
        rgb_values[(EV_cells < dangerous_level) & (EV_cells > 0)] = [0, 0, 255]
        rgb_values[EV_cells == 0] = [255,255,255]

        # Update the imshow object with new colors
        img.set_array(rgb_values)

        plt.pause(0.5)  # Pause for a short duration to allow visualization


        temp = set(map(tuple, new_list_points.tolist()))
        new_list_points = np.array(list(temp))
        list_points = new_list_points




def numpy_array_to_list(numpy_array):
    if isinstance(numpy_array, np.ndarray):
        return numpy_array.tolist()
    else:
        return numpy_array

def deter_rgb_vals(EV_cells, x, y, dangerous_level):
    if EV_cells[x][y] > dangerous_level:
        return np.array([0,255,255])
    elif EV_cells[x,y] > 0:
        return np.array(255, 0, 255)
    else:
        return np.array(255, 255, 255)
    


# elevation_height = np.array([
#    [9, 8, 11,12,7],
#    [8, 8, 8, 11,14],
#    [7, 8, 10,7, 8],
#    [8, 9, 7, 7, 7],
#    [10,9, 8, 7, 8]
# ]

elevation_height_values = np.array([
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.4e-7, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.06e-6, 0.0, 1.99e-6, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.39123742, 0.05713265, 0.0111295, 0.0, 0.0, 0.0, 3.7503e-4, 2.2031e-4, 0.0, 3.06e-6, 3.48e-6, 4.08e-6, 1.03e-6, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.12373146, 0.0, 0.04202727, 0.0037667, 0.0, 0.00120124, 0.0, 9.6906e-4, 0.0, 6.41e-6, 0.0, 3.64e-6, 8.9e-7, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.51993617, 0.0, 9.065e-5, 0.00133511, 0.0, 5.2379e-4, 0.0, 4.33e-5, 0.0, 9.64e-6, 0.0, 1.85e-6, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.787318e-2, 0.0, 1.3212e-4, 0.0, 1.3228e-4, 6.7542e-4, 0.0, 2.2643e-4, 0.0, 4.138e-5, 0.0, 2.94e-6, 2.0e-7, 0.0],
    [0.0, 0.0, 0.0, 9.8043582e-1, 0.0, 0.0, 0.0, 0.0, 0.0, 1.3228e-4, 2.1207e-4, 0.0, 1.8791e-4, 0.0, 8.959e-5, 0.0, 7.47e-6, 1.86e-6, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.1491e-4, 5.6528e-4, 0.0, 5.7617e-4, 0.0, 5.415e-5, 0.0, 1.566e-5, 1.66e-6, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 2.48846e-3, 0.0, 0.0, 0.0, 0.0, 0.0, 3.7329e-4, 3.0999e-4, 0.0, 5.321e-5, 0.0, 9.33e-6, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 1.01276e-3, 0.0, 2.92578e-3, 0.0, 6.2826e-4, 0.0, 0.0, 0.0, 2.617e-5, 0.0, 3.366e-5, 0.0, 0.0, 7e-8, 0.0, 0.0, 0.0, 0.0, 0.0],
    [8.4306e-4, 0.0, 3.55674e-3, 0.0, 9.10631e-3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00002622, 0, 0.00000749, 0, 0, 0, 0, 0, 0],
    [0, 0.00126918, 0, 0.00659247, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])



recursion_checking(water_height, elevation_height, np.array([[x,y]]), EV_cells, increment_height, rgb_values, dangerous_level)


plt.show()
