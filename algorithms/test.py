import numpy as np
import matplotlib.pyplot as plt
import caffé
import tkinter as tk
from tkinter import filedialog

# /Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/pajaro2nd.asc

def set_elevation_height(input_asc):
    with open(input_asc, 'r') as file:
        for _ in range(6):
            file.readline()
        
        data = np.loadtxt(file)
    
    return data

def select_asc_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select ASC File",
        filetypes=[("ASC files", "*.asc"), ("All files", "*.*")]
    )

    return file_path


#user_x = int(input("Enter x value: "))

input_asc = "/Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/pajaro2nd.asc" # Add directory to .asc file
#input_asc = select_asc_file()


# dangerous_level will be used for calculating which areas require evacuation more urgently

x = 0
y = 0


elevation_height = np.array([
    [3, 5, 4, 3, 6],
    [3, 7, 3, 3, 8],
    [3, 3, 3, 4, 7],
    [5, 3, 3, 3, 3],
    [9, 8, 6, 3, 3]
])

boundary_map = np.array([
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0]
])
caffé.pre_processing(elevation_height, boundary_map)

water_height = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells[x,y] = 10

dangerous_level = 6 #change to user input later
#Set RGB values for the single pixel
increment_height = 1 # Change to user input later

rgb_values = np.full((elevation_height.shape[0], elevation_height.shape[1], 3), 255, dtype=int)


plt.figure()

img = plt.imshow(rgb_values, extent=[0, elevation_height.shape[1], 0, elevation_height.shape[0]], origin='upper')
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='black')
plt.xticks(range(elevation_height.shape[1] + 1))
plt.yticks(range(elevation_height.shape[0] + 1))
plt.xlim(0, elevation_height.shape[1]) 
plt.ylim(0, elevation_height.shape[0])


def recursion_checking(water_height, elevation_height, list_points, EV_cells, increment_constant, rgb_values, dangerous_level, grid_image, fig):
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
        rgb_values[EV_cells == 0] = [255, 255, 255]

        # Set alpha values based on conditions
        alpha_values = np.where(EV_cells == 0, 0.0, 1.0)  # Set alpha to 0.0 for EV_cells == 0, 1.0 otherwise
        alpha_values = np.expand_dims(alpha_values, axis=-1)

        # Combine RGB and alpha values
        rgba_values = np.concatenate((rgb_values / 255, alpha_values), axis=-1)

        # Update the grid image with RGBA values
        grid_image.set_array(rgba_values)
        
        fig.canvas.draw()
        plt.pause(0.1)  # Adjust the delay as needed


                # Update the displayed data


        temp = set(map(tuple, new_list_points.tolist()))
        new_list_points = np.array(list(temp))
        list_points = new_list_points

def test_recursion_checking(water_height, elevation_height, list_points, EV_cells, increment_constant, rgb_values, dangerous_level):
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
        rgb_values[EV_cells == 0] = [255, 255, 255]

        # Update the imshow object with new colors
        img.set_array(rgb_values)

        plt.pause(1)  # Pause for a short duration to allow visualization


                # Update the displayed data


        temp = set(map(tuple, new_list_points.tolist()))
        new_list_points = np.array(list(temp))
        list_points = new_list_points

def final_image_recursion(water_height, elevation_height, list_points, EV_cells, increment_constant, rgb_values, dangerous_level):
     # list_points is the list of points that the program will run through for simulation every iteration
    final_array = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
    while list_points.size > 0:
        final_array = np.maximum(EV_cells, final_array)
        new_list_points = np.empty((0, 2), dtype=object)

        if caffé.end_sim(EV_cells, 2):
            rgb_values[final_array >= dangerous_level] = [255, 0, 255]
            rgb_values[(final_array < dangerous_level) & (final_array > 0)] = [0, 0, 255]
            rgb_values[final_array == 0] = [255, 255, 255]

            img.set_array(rgb_values)

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



        
        # Update the imshow object with new colors



                # Update the displayed data


        temp = set(map(tuple, new_list_points.tolist()))
        new_list_points = np.array(list(temp))
        list_points = new_list_points   






def get_elevation_height():
    return elevation_height




final_image_recursion(water_height, elevation_height, np.array([[x,y]]), EV_cells, increment_height, rgb_values, dangerous_level)
test_1 = np.array([
    [1, 2, 5],
    [3, 10, 2],
    [6, 9, 7]
])

test_2 = np.array([
    [5, 2, 9],
    [1, 3, 2],
    [9, 7, 4]
])

plt.show()

def temp(grid):

    grid[0][0] = [100, 50, 200]
