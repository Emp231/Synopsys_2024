import pandas as pd
import numpy as np
import plotly.express as px
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import test
from skimage.transform import resize
from PIL import Image, ImageDraw
import plotly.graph_objects as go
from staticmap import StaticMap, CircleMarker
import io
import caffé


x = 16
y = 41
increment_constant = 1
dangerous_level = 6 
elevation_height = test.get_elevation_height()

water_height = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells[16,3] = 15
EV_cells[16,2] = 15
EV_cells[16,1] = 15
EV_cells[16,4] = 15
EV_cells[16,5] = 15
EV_cells[16,6] = 15
EV_cells[16,7] = 15
EV_cells[16,8] = 15
EV_cells[16,9] = 15
EV_cells[16,10] = 15
EV_cells[16,11] = 15
EV_cells[16,12] = 15
EV_cells[16,13] = 15
EV_cells[16,14] = 15
EV_cells[16,15] = 15
EV_cells[16,16] = 15
EV_cells[16,17] = 15
EV_cells[16,18] = 15
EV_cells[16,19] = 15
EV_cells[16,20] = 15
EV_cells[15,20] = 15
EV_cells[15,21] = 15
EV_cells[15,22] = 15
EV_cells[15,23] = 15
EV_cells[15,24] = 15
EV_cells[15,25] = 15
EV_cells[15,26] = 15
EV_cells[15,27] = 15
EV_cells[16,27] = 15
EV_cells[16,28] = 15
EV_cells[16,29] = 15
EV_cells[16,30] = 15
EV_cells[16,31] = 15
EV_cells[16,32] = 15
EV_cells[15,32] = 15
EV_cells[15,33] = 15
EV_cells[15,34] = 15
EV_cells[15,35] = 15
EV_cells[15,36] = 15
EV_cells[15,37] = 15
EV_cells[15,38] = 15
EV_cells[15,39] = 15
EV_cells[15,40] = 15
EV_cells[15,41] = 15
EV_cells[16,41] = 15
EV_cells[16,42] = 15
EV_cells[16,43] = 15
EV_cells[16,44] = 15
EV_cells[16,45] = 15
EV_cells[16,46] = 15
EV_cells[16,47] = 15
EV_cells[16,48] = 15
EV_cells[16,49] = 15
EV_cells[16,50] = 15
EV_cells[16,51] = 15
EV_cells[16,52] = 15
EV_cells[16,53] = 15
EV_cells[16,54] = 15
EV_cells[16,55] = 15
EV_cells[16,56] = 15
EV_cells[16,57] = 15
EV_cells[16,58] = 15
EV_cells[16,59] = 15
EV_cells[16,60] = 15
EV_cells[16,61] = 15
rgb_values = np.full((elevation_height.shape[0], elevation_height.shape[1], 3), 255, dtype=int)
boundary_map = test.get_boundary_map()
# west = -121.868240
# north = 37.686555
# east = -121.861586
# south = 37.682008



# # Run your test_final_image_recursion function to get the final array
# final_array = test.test_final_image_recursion(water_height, elevation_height, np.array([[x,y]]), EV_cells, increment_constant, rgb_values, dangerous_level)

# # Create the grid image
# grid = np.full((final_array.shape[0], final_array.shape[1], 4), [255, 255, 255, 128], dtype=np.uint8)  # Set magenta with transparency (alpha=128)
# grid[final_array >= 0.5] = [255, 0, 255, 128]  # Set magenta with transparency (alpha=128) for values >= 0.5
# grid[(final_array < 0.5) & (final_array > 0)] = [0, 0, 255, 128]  # Set blue with transparency (alpha=128) for 0 < values < 0.5
# grid[final_array == 0] = [255, 255, 255, 0]  # Set white with full transparency (alpha=0) for values == 0
# # grid[0,0] = [255,0,255,128]

# grid = grid / 255.0

# plt.imshow(image)
# plt.axis('off')  # Turn off axis
# plt.tight_layout()  # Make layout tight

# # Add the grid on top of the image
# grid_size = grid.shape[:2]
# image_size = image.size
# cell_width = image_size[0] / grid_size[1]
# cell_height = image_size[1] / grid_size[0]

# # Set aspect ratio to be equal
# plt.gca().set_aspect('equal', adjustable='box')

# for i in range(grid_size[0]):
#     for j in range(grid_size[1]):
#         rect = plt.Rectangle((j * cell_width, i * cell_height), cell_width, cell_height,
#                              linewidth=1, edgecolor='none', facecolor=grid[i, j])
#         plt.gca().add_patch(rect)

# plt.show()

image_path = 'plesOSM.png'
image = plt.imread(image_path)

# Set up the grid plot
grid_width = elevation_height.shape[1]
grid_height = elevation_height.shape[0]
fig, ax = plt.subplots()

# Display the image as the background
ax.imshow(image, extent=[0, grid_width, 0, grid_height], origin='upper')

# Create an empty grid image
grid = np.full((grid_height, grid_width, 4), [255, 255, 255, 128], dtype=np.uint8)  # Set magenta with transparency (alpha=128)
grid_image = ax.imshow(grid, extent=[0, grid_width, 0, grid_height], origin='upper')

# Customize the plot if needed
ax.grid(True, which='both', linestyle='-', linewidth=0.5, color='black')
ax.set_xticks(np.arange(0, grid_width + 1, 1))
ax.set_yticks(np.arange(0, grid_height + 1, 1))
ax.set_xlim(0, grid_width) 
ax.set_ylim(0, grid_height)
ax.axis('off')

# Call your function for updating the grid image
test.final_image_recursion(water_height, elevation_height, np.array([[x, y]]), EV_cells, increment_constant, rgb_values, dangerous_level, grid_image, fig)
#test.final_image_recursion(water_height, elevation_height, np.array([[x, y]]), EV_cells, increment_constant, rgb_values, dangerous_level, grid_image, fig)
#test.test_method(water_height, elevation_height, np.array([[x, y]]), EV_cells, increment_constant, rgb_values, dangerous_level, grid_image, fig)

plt.axis('off')  # Turn off axis
plt.show()  # Show the plot