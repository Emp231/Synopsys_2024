import subprocess
import numpy as np

def tif_to_asc(input_tif, output_asc):
    gdal_translate_path = "" # Path to gdal_translate
    command = [gdal_translate_path, '-of', 'AAIGrid', input_tif, output_asc]
    subprocess.run(command)

    print("Conversion completed.")

    return asc_to_numpy(output_asc)


def asc_to_numpy(input_asc):
    with open(input_asc, 'r') as asc_file:
        for _ in range(6):
            asc_file.readline()

        data = np.loadtxt(asc_file)
    
    return data

input_tif = "" # Directory of TIF file you want to convert
output_asc = "" # Directory of ASC file you want to store data in
data_np = tif_to_asc(input_tif, output_asc)
print(data_np)

