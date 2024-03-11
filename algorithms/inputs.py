import numpy as np
import matplotlib.pyplot as plt

input_asc = ""
input_asc = "/Users/siddharthbalaji/Documents/Github_Home/Untitled/Synopsys_2024/.asc files/fremont_updated.asc"

def set_elevation_height(input_asc):
    with open(input_asc, 'r') as file:
        for _ in range(6):
            file.readline()
        
        data = np.loadtxt(file)
    
    return data

elevation_height = set_elevation_height(input_asc)

def get_elevation_height():
    return elevation_height

image_path = "plesOSM.png"
image = plt.imread(image_path)

def get_image():
    return image


def make_boundary_height(input_asc):
    with open(input_asc, 'r') as file:
        for _ in range(6):
            file.readline()
        
        data = np.loadtxt(file)
    
    return data

# Type in "Yes" or "No" in that format for the optional keyword
# if you do not want to use a boundary map, please enter the parameter of input_asc as ""
def set_boundary_height(optional, input_asc):
    if optional == "Yes":
        if input_asc != "":
            return make_boundary_height(input_asc)
        else:
            return "Please enter a valid asc file location or do not use a boundary map"
    elif optional == "No":
        return np.zeros((elevation_height.shape[0], elevation_height.shape[1]))
    else:  
        return "Please enter a valid input for the method."


boundary_height = set_boundary_height("No", "")

def get_boundary_map():
    return boundary_height


def set_EV_cells(input_asc):
    with open(input_asc, 'r') as file:
        for _ in range(6):
            file.readline()
        
        data = np.loadtxt(file)
    
    return data

#EV_cells = set_EV_cells("")

    