import numpy as np
from PIL import Image
import os

file_path = "C:/Users/saman/OneDrive/Documents/GitHub/Synopsys_2024/algorithms/DEM.tif"

# 9 x 9 square grid - 81 cells total
# central cell is literally middle cell (# 40)
# ordering is from 0 to 80 going left to right starting
# again at end of each row
#
#
#
#
#


water_central = 100
cur_cell_analyzed = 40
# every iteration has to check 4 cells around central: n-1, n+1, n+9, n-9
empty_array = np.empty((9, 9))
empty_array[4][4] = water_central
#print(empty_array)

with Image.open(file_path) as img:
    img_array = np.array(img)

    # Display the shape of the array (height, width, channels)
    print("Image Shape:", img_array.shape)

    # Access pixel values, for example, the pixel at row 4, column 4
    pixel_value = img_array[5, 5]
    print("Pixel Value at (4, 4):", pixel_value)


