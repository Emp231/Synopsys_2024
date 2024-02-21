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
boundary_map = np.array(elevation_height.shape[0], elevation_height.shape[1])
boundary_map[0,0,] = 0
boundary_map[0,10] = 10
boundary_map[1,10] = 10
boundary_map[2,10] = 10
boundary_map[3,10] = 10
boundary_map[4,10] = 10
boundary_map[5,10] = 10
boundary_map[6,10] = 10
boundary_map[7,10] = 10
boundary_map[8,10] = 10
boundary_map[9,10] = 10
boundary_map[10,10] = 10
boundary_map[11,10] = 10
boundary_map[12,10] = 10
boundary_map[13,10] = 10
boundary_map[14,10] = 10
boundary_map[15,10] = 10
boundary_map[16,10] = 10
boundary_map[17,10] = 10
boundary_map[18,10] = 10
boundary_map[19,10] = 10
boundary_map[20,10] = 10
boundary_map[21,10] = 10
boundary_map[22,10] = 10
boundary_map[23,10] = 10
boundary_map[24,10] = 10
boundary_map[25,10] = 10
boundary_map[26,10] = 10
boundary_map[27,9] = 10
boundary_map[28,9] = 10
boundary_map[29,9] = 10
boundary_map[30,8] = 10
boundary_map[31,8] = 10
boundary_map[32,8] = 10
boundary_map[33,7] = 10
boundary_map[34,7] = 10
boundary_map[35,6] = 10
boundary_map[36,6] = 10
boundary_map[35,8] = 10
boundary_map[35,9] = 10
boundary_map[37,5] = 10
boundary_map[38,4] = 10
boundary_map[38,5] = 10
boundary_map[38,4] = 10
boundary_map[39,4] = 10
boundary_map[40,3] = 10
boundary_map[41,3] = 10
boundary_map[42,3] = 10
boundary_map[43,3] = 10
boundary_map[44,3] = 10
boundary_map[44,2] = 10
boundary_map[39,3] = 10
boundary_map[39,2] = 10
boundary_map[38,1] = 10
boundary_map[38,0] = 10
boundary_map[16,3] = 10
boundary_map[16,2] = 10
boundary_map[16,1] = 10
boundary_map[16,4] = 10
boundary_map[16,5] = 10
boundary_map[16,6] = 10
boundary_map[16,7] = 10
boundary_map[16,8] = 10
boundary_map[16,9] = 10
boundary_map[16,10] = 10
boundary_map[16,11] = 10
boundary_map[16,12] = 10
boundary_map[16,13] = 10
boundary_map[16,14] = 10
boundary_map[16,15] = 10
boundary_map[16,16] = 10
boundary_map[16,17] = 10
boundary_map[16,18] = 10
boundary_map[16,19] = 10
boundary_map[16,20] = 10
boundary_map[15,21] = 10
boundary_map[15,22] = 10
boundary_map[15,23] = 10
boundary_map[15,24] = 10
boundary_map[15,25] = 10
boundary_map[15,26] = 10
boundary_map[15,27] = 10
boundary_map[16,28] = 10
boundary_map[16,29] = 10
boundary_map[16,30] = 10
boundary_map[16,31] = 10
boundary_map[16,32] = 10
boundary_map[15,33] = 10
boundary_map[15,34] = 10
boundary_map[15,35] = 10
boundary_map[15,36] = 10
boundary_map[15,37] = 10
boundary_map[15,38] = 10
boundary_map[15,39] = 10
boundary_map[15,40] = 10
boundary_map[15,41] = 10
boundary_map[16,41] = 10
boundary_map[16,42] = 10
boundary_map[16,43] = 10
boundary_map[16,44] = 10
boundary_map[16,45] = 10
boundary_map[16,46] = 10
boundary_map[16,47] = 10
boundary_map[16,48] = 10
boundary_map[16,49] = 10
boundary_map[16,50] = 10
boundary_map[16,51] = 10
boundary_map[16,52] = 10
boundary_map[16,53] = 10
boundary_map[16,54] = 10
boundary_map[16,55] = 10
boundary_map[16,56] = 10
boundary_map[16,57] = 10
boundary_map[16,58] = 10
boundary_map[16,59] = 10
boundary_map[16,60] = 10
boundary_map[16,61] = 10
boundary_map[15,61] = 10
boundary_map[14,61] = 10
boundary_map[13,61] = 10
boundary_map[12,61] = 10
boundary_map[11,61] = 10
boundary_map[10,61] = 10
boundary_map[9,61] = 10
boundary_map[8,61] = 10
boundary_map[7,61] = 10
boundary_map[6,61] = 10
boundary_map[5,61] = 10
boundary_map[4,61] = 10
boundary_map[3,61] = 10
boundary_map[2,61] = 10
boundary_map[1,61] = 10
boundary_map[0,61] = 10
boundary_map[17,61] = 10
boundary_map[18,61] = 10
boundary_map[19,61] = 10
boundary_map[20,61] = 10
boundary_map[21,61] = 10
boundary_map[22,61] = 10
boundary_map[23,61] = 10
boundary_map[24,61] = 10
boundary_map[25,61] = 10
boundary_map[26,61] = 10
boundary_map[27,61] = 10
boundary_map[28,61] = 10
boundary_map[29,61] = 10
boundary_map[30,61] = 10
boundary_map[31,61] = 10
boundary_map[32,61] = 10
boundary_map[33,61] = 10
boundary_map[34,61] = 10
boundary_map[35,61] = 10
boundary_map[36,61] = 10
boundary_map[37,61] = 10
boundary_map[38,61] = 10
boundary_map[39,61] = 10
boundary_map[40,61] = 10
boundary_map[41,61] = 10
boundary_map[42,61] = 10
boundary_map[43,61] = 10
boundary_map[44,60] = 10
boundary_map[45,60] = 10
boundary_map[46,60] = 10
boundary_map[47,60] = 10
boundary_map[48,60] = 10
boundary_map[44,61] = 10
boundary_map[45,61] = 10
boundary_map[46,61] = 10
boundary_map[47,61] = 10
boundary_map[48,61] = 10
boundary_map[4,59] = 10
boundary_map[4,58] = 10
boundary_map[4,57] = 10
boundary_map[4,56] = 10
boundary_map[4,55] = 10
boundary_map[4,54] = 10
boundary_map[4,53] = 10
boundary_map[4,52] = 10
boundary_map[4,51] = 10
boundary_map[0,37] = 10
boundary_map[1,37] = 10
boundary_map[2,37] = 10
boundary_map[3,37] = 10
boundary_map[4,37] = 10
boundary_map[5,37] = 10
boundary_map[6,37] = 10
boundary_map[7,37] = 10
boundary_map[8,37] = 10
boundary_map[9,37] = 10
boundary_map[10,37] = 10
boundary_map[11,37] = 10
boundary_map[12,37] = 10
boundary_map[13,37] = 10
boundary_map[14,37] = 10
boundary_map[15,37] = 10
boundary_map[0,23] = 10
boundary_map[1,23] = 10
boundary_map[2,23] = 10
boundary_map[3,23] = 10
boundary_map[4,23] = 10
boundary_map[5,23] = 10
boundary_map[6,23] = 10
boundary_map[7,23] = 10
boundary_map[8,22] = 10
boundary_map[9,22] = 10
boundary_map[10,22] = 10
boundary_map[11,22] = 10
boundary_map[12,22] = 10
boundary_map[13,22] = 10
boundary_map[14,22] = 10
boundary_map[15,22] = 10
boundary_map[16,23] = 10
boundary_map[17,23] = 10
boundary_map[18,23] = 10
boundary_map[19,23] = 10
boundary_map[20,23] = 10
boundary_map[21,23] = 10
boundary_map[22,23] = 10
boundary_map[23,23] = 10
boundary_map[24,22] = 10
boundary_map[25,22] = 10
boundary_map[26,22] = 10
boundary_map[27,22] = 10
boundary_map[28,22] = 10
boundary_map[29,22] = 10
boundary_map[30,23] = 10
boundary_map[31,23] = 10
boundary_map[31,24] = 10
boundary_map[31,25] = 10
boundary_map[31,26] = 10
boundary_map[31,27] = 10
boundary_map[31,28] = 10
boundary_map[32,28] = 10
boundary_map[32,29] = 10
boundary_map[32,30] = 10
boundary_map[32,31] = 10
boundary_map[32,32] = 10
boundary_map[32,33] = 10
boundary_map[32,34] = 10
boundary_map[32,35] = 10
boundary_map[32,36] = 10
boundary_map[32,37] = 10
boundary_map[31,38] = 10
boundary_map[32,39] = 10
boundary_map[32,40] = 10
boundary_map[32,41] = 10
boundary_map[32,42] = 10
boundary_map[32,43] = 10
boundary_map[32,44] = 10
boundary_map[32,45] = 10
boundary_map[32,46] = 10
boundary_map[32,47] = 10
boundary_map[32,48] = 10
boundary_map[32,49] = 10
boundary_map[32,50] = 10
boundary_map[32,51] = 10
boundary_map[31,52] = 10
boundary_map[32,53] = 10
boundary_map[32,54] = 10
boundary_map[32,55] = 10
boundary_map[32,56] = 10
boundary_map[32,57] = 10
boundary_map[32,58] = 10
boundary_map[32,59] = 10
boundary_map[32,60] = 10
boundary_map[44,11] = 10
boundary_map[45,11] = 10
boundary_map[46,11] = 10
boundary_map[47,11] = 10
boundary_map[46,10] = 10
boundary_map[17,43] = 10
boundary_map[18,43] = 10
boundary_map[19,43] = 10
boundary_map[20,43] = 10
boundary_map[21,44] = 10
boundary_map[22,44] = 10
boundary_map[23,44] = 10
boundary_map[24,45] = 10
boundary_map[25,45] = 10
boundary_map[26,45] = 10
boundary_map[27,45] = 10
boundary_map[28,45] = 10
boundary_map[29,45] = 10
boundary_map[30,45] = 10
boundary_map[31,45] = 10
boundary_map[32,45] = 10
boundary_map[16,35] = 10
boundary_map[17,35] = 10
boundary_map[18,35] = 10
boundary_map[19,35] = 10
boundary_map[20,35] = 10
boundary_map[21,35] = 10
boundary_map[22,35] = 10
boundary_map[23,35] = 10
boundary_map[33,34] = 10
boundary_map[34,34] = 10
boundary_map[35,35] = 10
boundary_map[36,35] = 10
boundary_map[37,35] = 10
boundary_map[38,35] = 10
boundary_map[39,35] = 10
boundary_map[40,35] = 10
boundary_map[41,36] = 10
boundary_map[4,60] = 10
boundary_map[33,45] = 10
boundary_map[34,44] = 10
boundary_map[35,44] = 10
boundary_map[36,44] = 10
boundary_map[37,44] = 10
boundary_map[38,44] = 10
boundary_map[39,44] = 10
boundary_map[40,45] = 10
boundary_map[40,44] = 10
boundary_map[41,45] = 10
boundary_map[42,45] = 10
boundary_map[43,45] = 10
boundary_map[44,45] = 10
boundary_map[45,45] = 10
boundary_map[46,45] = 10
boundary_map[47,45] = 10
boundary_map[48,45] = 10
boundary_map[48,27] = 10
boundary_map[47,27] = 10
boundary_map[46,27] = 10
boundary_map[48,35] = 10
boundary_map[47,35] = 10
boundary_map[46,35] = 10
boundary_map[45,35] = 10
boundary_map[44,35] = 10
boundary_map[44,34] = 10
boundary_map[0,68] = 10
boundary_map[1,68] = 10
boundary_map[2,68] = 10
boundary_map[3,67] = 10
boundary_map[4,67] = 10
boundary_map[5,67] = 10
boundary_map[6,67] = 10
boundary_map[7,67] = 10
boundary_map[8,67] = 10
boundary_map[9,67] = 10
boundary_map[10,67] = 10
boundary_map[11,67] = 10
boundary_map[12,67] = 10
boundary_map[13,67] = 10
boundary_map[14,67] = 10
boundary_map[15,67] = 10
boundary_map[16,67] = 10
boundary_map[17,67] = 10
boundary_map[18,67] = 10
boundary_map[19,67] = 10
boundary_map[20,67] = 10
boundary_map[21,67] = 10
boundary_map[22,67] = 10
boundary_map[23,67] = 10
boundary_map[24,67] = 10
boundary_map[25,67] = 10
boundary_map[26,67] = 10
boundary_map[27,67] = 10
boundary_map[28,67] = 10
boundary_map[29,67] = 10
boundary_map[30,67] = 10
boundary_map[31,67] = 10
boundary_map[32,67] = 10
boundary_map[33,67] = 10
boundary_map[34,67] = 10
boundary_map[35,67] = 10
boundary_map[36,67] = 10
boundary_map[37,67] = 10
boundary_map[38,67] = 10
boundary_map[39,67] = 10
boundary_map[40,67] = 10
boundary_map[41,67] = 10
boundary_map[42,67] = 10
boundary_map[43,68] = 10
boundary_map[44,69] = 10

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
