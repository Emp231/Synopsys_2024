import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors 

input_asc = "C:/Users/saman/OneDrive/Documents/GitHub/Synopsys_2024/.asc files/pajaro2nd.asc" # Add directory to .asc file
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

user_x = int(input("Enter x value: "))


plt.figure()
plt.xticks(range(20 + 1))
plt.yticks(range(13 + 1))
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='black')
plt.xlim(0, 20)
plt.ylim(0, 13)


plt.show()


