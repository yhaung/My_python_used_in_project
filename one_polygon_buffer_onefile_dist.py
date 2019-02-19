#cvs import into geopandas
# e.g center points of drone pictures
# source code ref: https://gist.github.com/nygeog/2731427a74ed66ca0e420eaa7bcd0d2b

import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame as geodf
#from shapely.geometry import Point
#import fiona
#import matplotlib.pyplot as plt


poly_shp = r'D:\MIMU\myanmar_district_boundaries\myanmar_district_boundaries.shp'
poly_geodf = gpd.read_file(poly_shp)



# https://gis.stackexchange.com/questions/279670/geopandas-equivalent-to-select-by-location

# If poly is a GeoDataFrame with a single geometry, extract this:


for kwin in poly_geodf['DT']:
    polygon = poly_geodf.loc[poly_geodf['DT']==kwin]
    #polygon = polygon.geometry[polygon.index.min()] # index is required to get geometry
    #polygon['geometry'] = polygon.geometry.buffer(0.0005)
    shp_name = "DT_" + kwin + "test.shp"
    polygon.to_file(driver='ESRI Shapefile', filename=r'D:\\MIMU\\test_dt\\'+ shp_name)
    print (shp_name, " exported")
