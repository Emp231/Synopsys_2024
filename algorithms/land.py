import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import test
import inputs


x = 24
y = 10
increment_constant = 1
dangerous_level = 6 
elevation_height = inputs.get_elevation_height()

water_height = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells[x,y] = 12

rgb_values = np.full((elevation_height.shape[0], elevation_height.shape[1], 3), 255, dtype=int)

# image_path = 'plesOSM.png'
# image = plt.imread(image_path)
image = inputs.get_image()

grid_width = elevation_height.shape[1]
grid_height = elevation_height.shape[0]
fig, ax = plt.subplots()

ax.imshow(image, extent=[0, grid_width, 0, grid_height], origin='upper')

grid = np.full((grid_height, grid_width, 4), [255, 255, 255, 128], dtype=np.uint8)  # Set magenta with transparency (alpha=128)
grid_image = ax.imshow(grid, extent=[0, grid_width, 0, grid_height], origin='upper')

ax.grid(True, which='both', linestyle='-', linewidth=0.5, color='black')
ax.set_xticks(np.arange(0, grid_width + 1, 1))
ax.set_yticks(np.arange(0, grid_height + 1, 1))
ax.set_xlim(0, grid_width) 
ax.set_ylim(0, grid_height)
ax.axis('off')


list_points = np.empty((0, 2))
point1 = [x, y]
point2 = [10, 21]

list_points = np.append(list_points, [point1], axis=0)
list_points = np.append(list_points, [point2], axis=0)

final_array = test.final_image_recursion(water_height, elevation_height, np.array([[x,y]]), EV_cells, increment_constant, rgb_values, dangerous_level, grid_image, fig)
#test.test_method(water_height, elevation_height, np.array([[x, y]]), EV_cells, increment_constant, rgb_values, dangerous_level, grid_image, fig)

plt.axis('off') 
plt.show()  

def get_EV_cells():
    return EV_cells
