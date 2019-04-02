# Extract featues base on attribute and saved as new files. Attribute is used for file name.
# Written by Kyaw Naing Win, GIS Program Manger, OneMap Technical Unit
# date: 2019 -04 -01
# project: DoP inter census

import arcpy
arcpy.env.workspace = r"D:\OMM_GIS\Projects\DoP_InterCensus_2019\01_EA\EA_copiled"
src = r"NPT_EA_116(export).shp"
outDir = r"C:\TempGIS\DOP\export"
srcField = "VTCODE"
preffix = "VT"
fcList = arcpy.ListFeatureClasses(src)
setAttr = []
row_count = 0
for fc in fcList:  
    
    with arcpy.da.SearchCursor(fc, [srcField]) as cursor:  
        for row in cursor:  
           setAttr.append(row[0])
           row_count += 1
setAttr = set(setAttr)
setAttr = list(setAttr)
print ('Number of row: {}'.format(row_count))
print ('Number of attribute: {}'.format(len(setAttr)))
print (setAttr)
# Set local variables

in_features = src
for each in setAttr:
    
    out_feature_class = outDir+"//"+ preffix + each + ".shp"
    #where_clause = '"VTCODE" = \'{}\''.format(each)
    where_clause = '"{}" = \'{}\''.format(srcField,each)
    arcpy.Select_analysis(in_features, out_feature_class, where_clause)
    print ("{}_{}{} is saved..".format(preffix, each, ".shp"))
