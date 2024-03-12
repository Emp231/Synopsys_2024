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
from IPython.display import display, clear_output
import caffé
import tkinter as tk
from tkinter import simpledialog

x = 4
y = 6
increment_constant = 1
dangerous_level = 6 
elevation_height = test.get_elevation_height()
water_height = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells = np.zeros([elevation_height.shape[0], elevation_height.shape[1]])
EV_cells[x][y] = 10
rgb_values = np.full((elevation_height.shape[0], elevation_height.shape[1], 3), 255, dtype=int)


west_longitude = -121.7519
east_longitude = -121.7456
north_latitude = 36.9052
south_latitude = 36.9022
 
root = tk.Tk()

def find_val(string):
  string = string.rstrip('\n')
  val = string[string.index(":") + 1:]
  return val

def read_coordinates_from_file(filename):
  file = open(filename, 'r')
  array_coords = np.empty(4)
  for line in file:
    if line.startswith("west_longitude"):
      array_coords[0] = find_val(line)
    if line.startswith("east_longitude"):
      array_coords[1] = find_val(line)
    if line.startswith("north_latitude"):
      array_coords[2] = find_val(line)
    if line.startswith("south_latitude"):
      array_coords[3] = find_val(line)
  
  return array_coords

def ask_for_input():
  
  filename = 'coords.txt'
  #coordinates = read_coordinates_from_file(filename)
  coordinates = read_coordinates_from_file(filename)
  # west_longitude = float(coordinates[0])
  # east_longitude = float(coordinates[1])
  # north_latitude = float(coordinates[2])
  # south_latitude = float(coordinates[3])
  west_longitude = -121.867272
  east_longitude = -121.862584
  north_latitude = 37.686560
  south_latitude = 37.682029
  
  lat = caffé.calc_lat_distance(north_latitude, south_latitude) * 1000
  long = caffé.calc_lon_distance(west_longitude, east_longitude) * 1000
  width_cell = long / elevation_height.shape[1]
  height_cell = lat / elevation_height.shape[0]
  root.withdraw()
  bounding_box = [(south_latitude, west_longitude), (north_latitude, east_longitude)]

  width = abs(east_longitude - west_longitude)
  height = abs(north_latitude - south_latitude)

  average_latitude = (north_latitude + south_latitude) / 2

  zoom_level = 15 - max(width, height) * 2

  m = folium.Map(location=[average_latitude, (west_longitude + east_longitude) / 2], zoom_start=zoom_level, zoomControl=False)
  m.fit_bounds([(south_latitude, west_longitude), (north_latitude, east_longitude)])

  print("Bounding Box:", bounding_box)

  mapFname = 'output.html'
  m.save(mapFname)

  mapUr1 = 'file://{0}/{1}'.format(os.getcwd(), mapFname)
  driver = webdriver.Chrome()
  driver.get(mapUr1)
  #time.sleep(5)
  driver.save_screenshot('output.png')
  driver.quit()


  final_array = test.test_final_image_recursion(water_height, elevation_height, np.array([[x,y]]), EV_cells, increment_constant, rgb_values, dangerous_level)  # Replace this with your actual final_array

  image = mpimg.imread('output.png')

  grid = np.full((final_array.shape[0], final_array.shape[1], 3), 255, dtype=int)


  grid[final_array >= 0.5] = [255, 0, 255]  
  grid[(final_array < 0.5) & (final_array > 0)] = [0, 0, 255]  
  grid[final_array == 0] = [255, 255, 255]

  grid[x,y] = [0,0,0]

  fig, ax = plt.subplots()

  ax.imshow(image, extent=[west_longitude, east_longitude, south_latitude, north_latitude])

  extent = [west_longitude, east_longitude, south_latitude, north_latitude]
  ax.imshow(grid, extent=extent, alpha=0.2)

  ax.set_axis_off()
  plt.show()

button = tk.Button(root, text="Run Program", command=ask_for_input)
button.pack()

root.mainloop()