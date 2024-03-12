import numpy as np
import json

with open('plesstreets.json', 'r') as file:
    data = json.load(file)

all_coordinates = []
for element in data["elements"]:
    for geometry in element["geometry"]:
        lat = geometry["lat"]
        lon = geometry["lon"]
        all_coordinates.append((lat, lon))

min_lat = min(coord[0] for coord in all_coordinates) if all_coordinates else 0
max_lat = max(coord[0] for coord in all_coordinates) if all_coordinates else 0
min_lon = min(coord[1] for coord in all_coordinates) if all_coordinates else 0
max_lon = max(coord[1] for coord in all_coordinates) if all_coordinates else 0

def scale_coord(coord, min_val, max_val, new_min, new_max):
    return (coord - min_val) / (max_val - min_val) * (new_max - new_min) + new_min

lat_dim = int((max_lat - min_lat) * 100000) + 1
lon_dim = int((max_lon - min_lon) * 100000) + 1
area_array = np.zeros((lat_dim, lon_dim))

for lat, lon in all_coordinates:
    lat_index = int(scale_coord(lat, min_lat, max_lat, 0, lat_dim - 1))
    lon_index = int(scale_coord(lon, min_lon, max_lon, 0, lon_dim - 1))
    area_array[lat_index, lon_index] = 1

np.savetxt('street_map.txt', area_array, fmt='%d')