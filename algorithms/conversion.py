import subprocess

def tif_to_asc(input_tif, output_asc):
    # Run gdal_translate command
    gdal_translate_path = "" #Path to gdal_translate
    command = [gdal_translate_path, '-of', 'AAIGrid', input_tif, output_asc]
    subprocess.run(command)

    print("Conversion completed.")

# Example usage
input_tif = "" # Directory of TIF file you want to convert
output_asc = "" # Directory of ASC file you want to store data in
tif_to_asc(input_tif, output_asc)

