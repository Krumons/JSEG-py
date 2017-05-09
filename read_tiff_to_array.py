from env import *
def open_tiff(path):
        dataset = gdal.Open(path, GA_ReadOnly )
        return dataset
