import numpy as np

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
print(empty_array)

with open('DEM.tif', 'r') as file:
    content = file.read()
    print(content)

