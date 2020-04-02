# Name: Clip_Example2.py
# Description: Clip major roads that fall within the study area. 

# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "D:/OSM_Comparison/OSM Yangon/OSM_2017/Metadata_Geofabrick/20171213_Myanmar/Yangon"

# Set local variables
#in_features = "majorrds.shp"

clip_features = "D:/OSM_Comparison/Ygn_OSM_Comparison(17&18)/Summarize dbf/Yangon_polygon.shp"

out_feature_class = "C:/output/studyarea.shp"
xy_tolerance = ""

# Execute Clip
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)
print("successflly clipped)
