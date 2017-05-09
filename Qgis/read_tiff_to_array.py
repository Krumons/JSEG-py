from osgeo import gdal
import numpy as np

def open_tiff(self, path):
        dataset = gdal.Open( path, GA_ReadOnly )
        print dataset.GetRasterCount()
