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

input_asc = "/Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/fremont_updated.asc" # Add directory to .asc file
#input_asc = select_asc_file()


# dangerous_level will be used for calculating which areas require evacuation more urgently

x = 0
y = 0


# elevation_height = np.array([
#     [3, 5, 4, 3, 6],
#     [3, 7, 3, 3, 8],
#     [3, 3, 3, 4, 7],
#     [5, 3, 3, 3, 3],
#     [9, 8, 6, 3, 3]
# ])

elevation_height = set_elevation_height(input_asc)
#caffé.pre_processing(elevation_height, boundary_map)
boundary_map = np.zeros((elevation_height.shape[0], elevation_height.shape[1]))
boundary_map[0,10] = 1
boundary_map[1,10] = 1
boundary_map[2,10] = 1
boundary_map[3,10] = 1
boundary_map[4,10] = 1
boundary_map[5,10] = 1
boundary_map[6,10] = 1
boundary_map[7,10] = 1
boundary_map[8,10] = 1
boundary_map[9,10] = 1
boundary_map[10,10] = 1
boundary_map[11,10] = 1
boundary_map[12,10] = 1
boundary_map[13,10] = 1
boundary_map[14,10] = 1
boundary_map[15,10] = 1
boundary_map[16,10] = 1
boundary_map[17,10] = 1
boundary_map[18,10] = 1
boundary_map[19,10] = 1
boundary_map[20,10] = 1
boundary_map[21,10] = 1
boundary_map[22,10] = 1
boundary_map[23,10] = 1
boundary_map[24,10] = 1
boundary_map[25,10] = 1
boundary_map[26,10] = 1
boundary_map[27,9] = 1
boundary_map[26,9] = 1
boundary_map[28,9] = 1
boundary_map[29,9] = 1
boundary_map[30,9] = 1
boundary_map[30,8] = 1
boundary_map[31,8] = 1
boundary_map[32,8] = 1
boundary_map[32,7] = 1
boundary_map[33,7] = 1
boundary_map[34,7] = 1
boundary_map[34,6] = 1
boundary_map[35,6] = 1
boundary_map[35,7] = 1
boundary_map[36,6] = 1
boundary_map[36,5] = 1
boundary_map[35,8] = 1
boundary_map[35,9] = 1
boundary_map[37,5] = 1
boundary_map[38,4] = 1
boundary_map[38,5] = 1
boundary_map[38,4] = 1
boundary_map[39,4] = 1
boundary_map[40,3] = 1
boundary_map[41,3] = 1
boundary_map[42,3] = 1
boundary_map[43,3] = 1
boundary_map[44,3] = 1
boundary_map[44,2] = 1
boundary_map[39,3] = 1
boundary_map[39,2] = 1
boundary_map[39,1] = 1
boundary_map[38,1] = 1
boundary_map[38,0] = 1
boundary_map[16,3] = 1
boundary_map[16,2] = 1
boundary_map[16,1] = 1
boundary_map[16,4] = 1
boundary_map[16,5] = 1
boundary_map[16,6] = 1
boundary_map[16,7] = 1
boundary_map[16,8] = 1
boundary_map[16,9] = 1
boundary_map[16,10] = 1
boundary_map[16,11] = 1
boundary_map[16,12] = 1
boundary_map[16,13] = 1
boundary_map[16,14] = 1
boundary_map[16,15] = 1
boundary_map[16,16] = 1
boundary_map[16,17] = 1
boundary_map[16,18] = 1
boundary_map[16,19] = 1
boundary_map[16,20] = 1
boundary_map[15,20] = 1 
boundary_map[15,21] = 1
boundary_map[15,22] = 1
boundary_map[15,23] = 1
boundary_map[15,24] = 1
boundary_map[15,25] = 1
boundary_map[15,26] = 1
boundary_map[15,27] = 1
boundary_map[16,27] = 1
boundary_map[16,28] = 1
boundary_map[16,29] = 1
boundary_map[16,30] = 1
boundary_map[16,31] = 1
boundary_map[16,32] = 1
boundary_map[15,32] = 1
boundary_map[15,33] = 1
boundary_map[15,34] = 1
boundary_map[15,35] = 1
boundary_map[15,36] = 1
boundary_map[15,37] = 1
boundary_map[15,38] = 1
boundary_map[15,39] = 1
boundary_map[15,40] = 1
boundary_map[15,41] = 1
boundary_map[16,41] = 1
boundary_map[16,42] = 1
boundary_map[16,43] = 1
boundary_map[16,44] = 1
boundary_map[16,45] = 1
boundary_map[16,46] = 1
boundary_map[16,47] = 1
boundary_map[16,48] = 1
boundary_map[16,49] = 1
boundary_map[16,50] = 1
boundary_map[16,51] = 1
boundary_map[16,52] = 1
boundary_map[16,53] = 1
boundary_map[16,54] = 1
boundary_map[16,55] = 1
boundary_map[16,56] = 1
boundary_map[16,57] = 1
boundary_map[16,58] = 1
boundary_map[16,59] = 1
boundary_map[16,60] = 1
boundary_map[16,61] = 1
boundary_map[15,61] = 1
boundary_map[14,61] = 1
boundary_map[13,61] = 1
boundary_map[12,61] = 1
boundary_map[11,61] = 1
boundary_map[10,61] = 1
boundary_map[9,61] = 1
boundary_map[8,61] = 1
boundary_map[7,61] = 1
boundary_map[6,61] = 1
boundary_map[5,61] = 1
boundary_map[4,61] = 1
boundary_map[3,61] = 1
boundary_map[2,61] = 1
boundary_map[1,61] = 1
boundary_map[0,61] = 1
boundary_map[17,61] = 1
boundary_map[18,61] = 1
boundary_map[19,61] = 1
boundary_map[20,61] = 1
boundary_map[21,61] = 1
boundary_map[22,61] = 1
boundary_map[23,61] = 1
boundary_map[24,61] = 1
boundary_map[25,61] = 1
boundary_map[26,61] = 1
boundary_map[27,61] = 1
boundary_map[28,61] = 1
boundary_map[29,61] = 1
boundary_map[30,61] = 1
boundary_map[31,61] = 1
boundary_map[32,61] = 1
boundary_map[33,61] = 1
boundary_map[34,61] = 1
boundary_map[35,61] = 1
boundary_map[36,61] = 1
boundary_map[37,61] = 1
boundary_map[38,61] = 1
boundary_map[39,61] = 1
boundary_map[40,61] = 1
boundary_map[41,61] = 1
boundary_map[42,61] = 1
boundary_map[43,61] = 1
boundary_map[44,60] = 1
boundary_map[45,60] = 1
boundary_map[46,60] = 1
boundary_map[47,60] = 1
boundary_map[48,60] = 1
boundary_map[44,61] = 1
boundary_map[45,61] = 1
boundary_map[46,61] = 1
boundary_map[47,61] = 1
boundary_map[48,61] = 1
boundary_map[4,59] = 1
boundary_map[4,58] = 1
boundary_map[4,57] = 1
boundary_map[4,56] = 1
boundary_map[4,55] = 1
boundary_map[4,54] = 1
boundary_map[4,53] = 1
boundary_map[4,52] = 1
boundary_map[4,51] = 1
boundary_map[0,37] = 1
boundary_map[1,37] = 1
boundary_map[2,37] = 1
boundary_map[3,37] = 1
boundary_map[4,37] = 1
boundary_map[5,37] = 1
boundary_map[6,37] = 1
boundary_map[7,37] = 1
boundary_map[8,37] = 1
boundary_map[9,37] = 1
boundary_map[10,37] = 1
boundary_map[11,37] = 1
boundary_map[12,37] = 1
boundary_map[13,37] = 1
boundary_map[14,37] = 1
boundary_map[15,37] = 1
boundary_map[0,23] = 1
boundary_map[1,23] = 1
boundary_map[2,23] = 1
boundary_map[3,23] = 1
boundary_map[4,23] = 1
boundary_map[5,23] = 1
boundary_map[6,23] = 1
boundary_map[7,23] = 1
boundary_map[7,22] = 1
boundary_map[8,22] = 1
boundary_map[9,22] = 1
boundary_map[10,22] = 1
boundary_map[11,22] = 1
boundary_map[12,22] = 1
boundary_map[13,22] = 1
boundary_map[14,22] = 1
boundary_map[15,22] = 1
boundary_map[16,23] = 1
boundary_map[17,23] = 1
boundary_map[18,23] = 1
boundary_map[19,23] = 1
boundary_map[20,23] = 1
boundary_map[21,23] = 1
boundary_map[22,23] = 1
boundary_map[23,22] = 1
boundary_map[23,23] = 1
boundary_map[24,22] = 1
boundary_map[25,22] = 1
boundary_map[26,22] = 1
boundary_map[27,22] = 1
boundary_map[28,22] = 1
boundary_map[29,22] = 1
boundary_map[30,22] = 1
boundary_map[30,23] = 1
boundary_map[31,23] = 1
boundary_map[31,24] = 1
boundary_map[31,25] = 1
boundary_map[31,26] = 1
boundary_map[31,27] = 1
boundary_map[31,28] = 1
boundary_map[32,28] = 1
boundary_map[32,29] = 1
boundary_map[32,30] = 1
boundary_map[32,31] = 1
boundary_map[32,32] = 1
boundary_map[32,33] = 1
boundary_map[32,34] = 1
boundary_map[32,35] = 1
boundary_map[32,36] = 1
boundary_map[32,37] = 1
boundary_map[32,38] = 1
boundary_map[31,38] = 1
boundary_map[32,39] = 1
boundary_map[32,40] = 1
boundary_map[32,41] = 1
boundary_map[32,42] = 1
boundary_map[32,43] = 1
boundary_map[32,44] = 1
boundary_map[32,45] = 1
boundary_map[32,46] = 1
boundary_map[32,47] = 1
boundary_map[32,48] = 1
boundary_map[32,49] = 1
boundary_map[32,50] = 1
boundary_map[32,51] = 1
boundary_map[31,52] = 1
boundary_map[31,53] = 1
boundary_map[31,51] = 1
boundary_map[32,53] = 1
boundary_map[32,54] = 1
boundary_map[32,55] = 1
boundary_map[32,56] = 1
boundary_map[32,57] = 1
boundary_map[32,58] = 1
boundary_map[32,59] = 1
boundary_map[32,60] = 1
boundary_map[44,11] = 1
boundary_map[45,11] = 1
boundary_map[46,11] = 1
boundary_map[47,11] = 1
boundary_map[46,10] = 1
boundary_map[17,43] = 1
boundary_map[18,43] = 1
boundary_map[19,43] = 1
boundary_map[19,44] = 1
boundary_map[20,43] = 1
boundary_map[20,44] = 1
boundary_map[21,44] = 1
boundary_map[22,44] = 1
boundary_map[23,44] = 1
boundary_map[23,45] = 1
boundary_map[24,45] = 1
boundary_map[25,45] = 1
boundary_map[26,45] = 1
boundary_map[27,45] = 1
boundary_map[28,45] = 1
boundary_map[29,45] = 1
boundary_map[30,45] = 1
boundary_map[31,45] = 1
boundary_map[32,45] = 1
boundary_map[16,35] = 1
boundary_map[17,35] = 1
boundary_map[18,35] = 1
boundary_map[19,35] = 1
boundary_map[20,35] = 1
boundary_map[21,35] = 1
boundary_map[22,35] = 1
boundary_map[23,35] = 1
boundary_map[33,34] = 1
boundary_map[34,34] = 1
boundary_map[34,35] = 1
boundary_map[35,35] = 1
boundary_map[36,35] = 1
boundary_map[37,35] = 1
boundary_map[38,35] = 1
boundary_map[39,35] = 1
boundary_map[40,35] = 1
boundary_map[41,35] = 1
boundary_map[41,36] = 1
boundary_map[4,60] = 1
boundary_map[33,45] = 1
boundary_map[34,45] = 1
boundary_map[34,44] = 1
boundary_map[35,44] = 1
boundary_map[36,44] = 1
boundary_map[37,44] = 1
boundary_map[38,44] = 1
boundary_map[39,44] = 1
boundary_map[40,45] = 1
boundary_map[40,44] = 1
boundary_map[41,45] = 1
boundary_map[42,45] = 1
boundary_map[43,45] = 1
boundary_map[44,45] = 1
boundary_map[45,45] = 1
boundary_map[46,45] = 1
boundary_map[47,45] = 1
boundary_map[48,45] = 1
boundary_map[48,27] = 1
boundary_map[47,27] = 1
boundary_map[46,27] = 1
boundary_map[48,35] = 1
boundary_map[47,35] = 1
boundary_map[46,35] = 1
boundary_map[45,35] = 1
boundary_map[44,35] = 1
boundary_map[44,34] = 1
boundary_map[0,68] = 1
boundary_map[1,68] = 1
boundary_map[2,68] = 1
boundary_map[3,67] = 1
boundary_map[3,68] = 1
boundary_map[4,67] = 1
boundary_map[5,67] = 1
boundary_map[6,67] = 1
boundary_map[7,67] = 1
boundary_map[8,67] = 1
boundary_map[9,67] = 1
boundary_map[10,67] = 1
boundary_map[11,67] = 1
boundary_map[12,67] = 1
boundary_map[13,67] = 1
boundary_map[14,67] = 1
boundary_map[15,67] = 1
boundary_map[16,67] = 1
boundary_map[17,67] = 1
boundary_map[18,67] = 1
boundary_map[19,67] = 1
boundary_map[20,67] = 1
boundary_map[21,67] = 1
boundary_map[22,67] = 1
boundary_map[23,67] = 1
boundary_map[24,67] = 1
boundary_map[25,67] = 1
boundary_map[26,67] = 1
boundary_map[27,67] = 1
boundary_map[28,67] = 1
boundary_map[29,67] = 1
boundary_map[30,67] = 1
boundary_map[31,67] = 1
boundary_map[32,67] = 1
boundary_map[33,67] = 1
boundary_map[34,67] = 1
boundary_map[35,67] = 1
boundary_map[36,67] = 1
boundary_map[37,67] = 1
boundary_map[38,67] = 1
boundary_map[39,67] = 1
boundary_map[40,67] = 1
boundary_map[41,67] = 1
boundary_map[42,67] = 1
boundary_map[43,67] = 1
boundary_map[43,68] = 1
boundary_map[44,68] = 1
boundary_map[44,69] = 1

water_height = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells[x,y] = 10

dangerous_level = 6 #change to user input later
#Set RGB values for the single pixel
increment_height = 1 # Change to user input later

rgb_values = np.full((elevation_height.shape[0], elevation_height.shape[1], 3), 255, dtype=int)

grid_width = elevation_height.shape[1]
grid_height = elevation_height.shape[0]

# fig, ax = plt.subplots()

# # Create an empty grid image
# grid_image = ax.imshow(rgb_values, extent=[0, elevation_height.shape[1], 0, elevation_height.shape[0]], origin='upper')

# # Customize the plot if needed
# ax.grid(True, which='both', linestyle='-', linewidth=0.5, color='black')
# ax.set_xticks(range(grid_width + 1))
# ax.set_yticks(range(grid_height + 1))
# ax.set_xlim(0, grid_width) 
# ax.set_ylim(0, grid_height)

def get_boundary_map():
    return boundary_map

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

        alpha_values = np.where(EV_cells == 0, 0.0, 1.0)
        alpha_values = np.expand_dims(alpha_values, axis=-1)
        rgba_values = np.concatenate((rgb_values / 255, alpha_values), axis=-1)
        
        grid_image.set_data(rgba_values)

        plt.pause(0.5)

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

def final_image_recursion(water_height, elevation_height, list_points, EV_cells, increment_constant, rgb_values, dangerous_level, grid_image, fig):
     # list_points is the list of points that the program will run through for simulation every iteration
    final_array = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
    while list_points.size > 0:
        new_list_points = np.empty((0, 2), dtype=object)

        if caffé.end_sim(EV_cells, 2):
            rgb_values[final_array >= dangerous_level] = [255, 0, 255]
            rgb_values[(final_array < dangerous_level) & (final_array > 0)] = [0, 0, 255]
            rgb_values[final_array == 0] = [255, 255, 255]

            alpha_values = np.where(final_array == 0, 0.0, 1.0)  # Set alpha to 0.0 for EV_cells == 0, 1.0 otherwise
            alpha_values = np.expand_dims(alpha_values, axis=-1)

            # Combine RGB and alpha values
            rgba_values = np.concatenate((rgb_values / 255, alpha_values), axis=-1)

            # Update the grid image with RGBA values
            grid_image.set_array(rgba_values)

            fig.canvas.draw()
            plt.pause(0.1)  # Adjust the delay as needed

            break
    
        for point in list_points:
            cur_x = np.atleast_1d(point)[0]
            cur_y = np.atleast_1d(point)[1]

            final_array = np.maximum(EV_cells, final_array)

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



def test_final_image_recursion(water_height, elevation_height, list_points, EV_cells, increment_constant, rgb_values, dangerous_level):
     # list_points is the list of points that the program will run through for simulation every iteration
    final_array = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
    while list_points.size > 0:
        new_list_points = np.empty((0, 2), dtype=object)
        final_array = np.maximum(EV_cells, final_array)

        
        if caffé.end_sim(EV_cells, 2):
            rgb_values[final_array >= dangerous_level] = [255, 0, 255]
            rgb_values[(final_array < dangerous_level) & (final_array > 0)] = [0, 0, 255]
            rgb_values[final_array == 0] = [255, 255, 255]

            return final_array
    
        for point in list_points:
            cur_x = np.atleast_1d(point)[0]
            cur_y = np.atleast_1d(point)[1]
            final_array = np.maximum(EV_cells, final_array)


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
        
        temp = set(map(tuple, new_list_points.tolist()))
        new_list_points = np.array(list(temp))
        list_points = new_list_points   




def get_elevation_height():
    return elevation_height

def test_method(water_height, elevation_height, list_points, EV_cells, increment_constant, rgb_values, dangerous_level, grid_image, fig):
        
    rgb_values[EV_cells >= dangerous_level] = [255, 0, 255]
    rgb_values[(EV_cells < dangerous_level) & (EV_cells > 0)] = [0, 0, 255]
    rgb_values[EV_cells == 0] = [255, 255, 255]


    alpha_values = np.where(EV_cells == 0, 0.0, 1.0)
    alpha_values = np.expand_dims(alpha_values, axis=-1)
    rgba_values = np.concatenate((rgb_values / 255, alpha_values), axis=-1)
    
    grid_image.set_data(rgba_values)

    plt.pause(0.5)

# recursion_checking(water_height, elevation_height, np.array([[x,y]]), EV_cells, increment_height, rgb_values, dangerous_level, grid_image, fig)
# plt.show(block=False)  # Show the plot without blocking
# plt.show()
# temp_grid[4, 7] = 1
# temp_grid[5, 8] = 1
# temp_grid[4, 8] = 1
# temp_grid[4, 9] = 1
# temp_grid[5, 9] = 1
# temp_grid[6, 9] = 1
# temp_grid[7, 10] = 1
# temp_grid[8, 10] = 1
# temp_grid[6, 10] = 1
# temp_grid[5, 10] = 1
# temp_grid[4, 10] = 1
# temp_grid[7, 9] = 1
# temp_grid[5, 4] = 1
# temp_grid[6, 5] = 1
# temp_grid[7, 6] = 1
# temp_grid[8, 7] = 1
# temp_grid[5, 5] = 1
# temp_grid[9, 8] = 1
# temp_grid[6, 6] = 1
# temp_grid[10, 8] = 1
# temp_grid[10, 9] = 1
# temp_grid[11, 10] = 1
# temp_grid[12, 10] = 1
# temp_grid[11, 9] = 1
# temp_grid[8, 4] = 1
# temp_grid[8, 3] = 1
# temp_grid[7, 4] = 1
# temp_grid[6, 3] = 1
# temp_grid[9, 4] = 1
# temp_grid[9, 5] = 1
# temp_grid[10, 5] = 1
# temp_grid[10, 6] = 1
# temp_grid[11, 6] = 1
# temp_grid[12, 7] = 1
# temp_grid[12, 6] = 1
# temp_grid[7, 3] = 1
# temp_grid[12, 4] = 1
# temp_grid[12, 2] = 1
# temp_grid[11, 3] = 1
# temp_grid[10, 3] = 1
# temp_grid[10, 2] = 1
# temp_grid[4, 12] = 1
# temp_grid[4, 13] = 1
# temp_grid[4, 14] = 1
# temp_grid[4, 15] = 1
# temp_grid[6, 12] = 1
# temp_grid[6, 13] = 1
# temp_grid[6, 14] = 1
# temp_grid[6, 15] = 1
# temp_grid[7, 12] = 1
# temp_grid[7, 13] = 1
# temp_grid[7, 14] = 1
# temp_grid[7, 15] = 1
# temp_grid[9, 12] = 1
# temp_grid[9, 13] = 1
# temp_grid[9, 14] = 1
# temp_grid[9, 15] = 1
# temp_grid[10, 12] = 1
# temp_grid[10, 13] = 1
# temp_grid[10, 14] = 1
# temp_grid[10, 15] = 1
# temp_grid[12, 12] = 1
# temp_grid[12, 13] = 1
# temp_grid[12, 14] = 1
# temp_grid[12, 15] = 1
# temp_grid[2, 12] = 1
# temp_grid[1, 12] = 1
# temp_grid[0, 12] = 1
# temp_grid[2, 11] = 1
# temp_grid[1, 11] = 1
# temp_grid[0, 11] = 1
# temp_grid[2, 14] = 1
# temp_grid[1, 14] = 1
# temp_grid[0, 14] = 1
# temp_grid[2, 16] = 1
# temp_grid[1, 16] = 1
# temp_grid[0, 16] = 1
# temp_grid[2, 18] = 1
# temp_grid[1, 18] = 1
# temp_grid[0, 18] = 1
# temp_grid[2, 19] = 1
# temp_grid[1,19] = 1
# temp_grid[0,19] = 1
# temp_grid[2,10] = 1
# temp_grid[1,10] = 1
# temp_grid[0,10] = 1
# temp_grid[2,8] = 1
# temp_grid[1,8] = 1
# temp_grid[0,8] = 1
# temp_grid[12,9] = 1
# temp_grid[5,4] = 1
# temp_grid[4,5] = 1
# temp_grid[4,4] = 1
# temp_grid[9,3] = 1
# temp_grid[9,2] = 1

# caffé.pre_processing(elevation_height, temp_grid)
