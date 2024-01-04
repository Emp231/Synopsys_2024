from osgeo import gdal

def tif_to_asc_with_headers_and_data(input_tif, output_asc):
    # Open the input GeoTIFF file
    ds = gdal.Open(input_tif)

    # Get necessary information from the dataset
    geotransform = ds.GetGeoTransform()

    # Read the raster band
    band = ds.GetRasterBand(1)
    data = band.ReadAsArray()

    # Write to the ASCII file with GeoTIFF metadata and elevation data
    with open(output_asc, 'w') as asc_file:
        asc_file.write("NCOLS {}\n".format(ds.RasterXSize))
        asc_file.write("NROWS {}\n".format(ds.RasterYSize))
        asc_file.write("XLLCORNER {}\n".format(geotransform[0]))
        asc_file.write("YLLCORNER {}\n".format(geotransform[3] + ds.RasterYSize * geotransform[5]))
        asc_file.write("CELLSIZE {}\n".format(abs(geotransform[1])))
        asc_file.write("NODATA_VALUE {}\n".format(band.GetNoDataValue() if band.GetNoDataValue() is not None else -9999))

        # Write the elevation data
        for row in data:
            for value in row:
                asc_file.write("{} ".format(value))
            asc_file.write("\n")

    # Close the dataset
    ds = None

    print("Conversion completed.")

# Example usage
input_tif = "C:/Users/saman/OneDrive/Documents/GitHub/Synopsys_2024/LF2020_Elev_220_CONUS/LC20_Elev_220.tif"
output_asc = "C:/Users/saman/OneDrive/Documents/GitHub/Synopsys_2024/algorithms/file.asc"
tif_to_asc_with_headers_and_data(input_tif, output_asc)