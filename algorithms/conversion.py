import numpy as np

input_tif = "C:/Users/saman/OneDrive/Documents/GitHub/Synopsys_2024/algorithms/spacereserve.asc"
with open(input_tif, 'r') as file:
    for _ in range(6):
        content = file.readline()
        print(content)

    data = np.loadtxt(file)

print(data)
# Example usage


