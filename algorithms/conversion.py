from osgeo import gdal

def tif_to_asc(input_tif, output_asc):
    ds = gdal.Open(input_tif)
    band = ds.GetRasterBand(1)
    data = band.ReadAsArray()
    geotransform = ds.GetGeoTransform()
    projection = ds.GetProjection()

    with open(output_asc, 'w') as asc_file:
        asc_file.write("NCOLS {}\n".format(ds.RasterXSize))
        asc_file.write("NROWS {}\n".format(ds.RasterYSize))
        asc_file.write("XLLCORNER {}\n".format(geotransform[0]))
        asc_file.write("YLLCORNER {}\n".format(geotransform[3] + ds.RasterYSize * geotransform[5]))
        asc_file.write("CELLSIZE {}\n".format(abs(geotransform[1])))
        asc_file.write("NODATA_VALUE -9999\n")

        # Write the raster data
        for row in data:
            for value in row:
                asc_file.write("{} ".format(value))
            asc_file.write("\n")


    print("Conversion completed.")

input_tif = "" # Add directory of TIF file
output_asc = "file.asc" # Add directory where you want to store ASC file
tif_to_asc(input_tif, output_asc)

