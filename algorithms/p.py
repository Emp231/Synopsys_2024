@ -0,0 +1,75 @@
import folium
import webbrowser
from folium import plugins
from selenium import webdriver
import os
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import test

elevation_height = test.get_elevation_height()
water_height = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])


west_longitude = -121.7519
east_longitude = -121.7456
north_latitude = 36.9052
south_latitude = 36.9022

bounding_box = [(south_latitude, west_longitude), (north_latitude, east_longitude)]

width = abs(east_longitude - west_longitude)
height = abs(north_latitude - south_latitude)

average_latitude = (north_latitude + south_latitude) / 2

zoom_level = 15 - max(width, height) * 2

m = folium.Map(location=[average_latitude, (west_longitude + east_longitude) / 2], zoom_start=zoom_level, zoomControl=False)
m.fit_bounds(bounding_box)

mapFname = 'output.html'
m.save(mapFname)

mapUr1 = 'file://{0}/{1}'.format(os.getcwd(), mapFname)
driver = webdriver.Chrome()
driver.get(mapUr1)
time.sleep(5)
driver.save_screenshot('output.png')
driver.quit()

image = mpimg.imread('output.png')

fig, ax = plt.subplots()

ax.imshow(image)

grid = np.zeros_like(image)
grid[::20, :] = 1 
grid[:, ::20] = 1 


grid = np.flipud(grid)

ax.imshow(grid, cmap='gray', alpha=0.3, extent=[0, image.shape[1], image.shape[0], 0])

ax.axis('off')

plt.show(block=True)