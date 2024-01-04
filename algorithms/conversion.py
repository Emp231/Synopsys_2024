import numpy as np

input_asc = "" # PATH TO INPUT .asc (to read)
with open(input_asc, 'r') as file:
    for _ in range(6):
        content = file.readline()
        print(content)

    data = np.loadtxt(file)

print(data)
# Example usage


