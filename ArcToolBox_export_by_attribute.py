# Extract featues base on attribute and saved as new files. Attribute is used for file name.
# Written by Kyaw Naing Win, GIS Program Manger, OneMap Technical Unit
# date: 2019 -04 -01
# project: DoP inter census
import os, sys
import arcpy

src = arcpy.GetParameterAsText(0)# r"D:\OMM_GIS\Projects\DoP_InterCensus_2019\01_EA\EA_copiled"NPT_EA_116(export).shp"
srcField = arcpy.GetParameterAsText(1) # Field to get attribute value eg. "VTCODE"
outDir = arcpy.GetParameterAsText(2) # output directory to save new files eg. r"C:\TempGIS\DOP\export"
preffix = arcpy.GetParameterAsText(3) # option for prefix for new file name. if not provided, field name will be use.
if not preffix:
	preffix = srcField
preffix = preffix + "_"
#fcList = arcpy.ListFeatureClasses(src)
setAttr = []
row_count = 0

# verify field type as string or integer for where clause construction
fields = arcpy.ListFields(src)
for field in fields:
	if field.name == srcField:
		if field.type == "String":
			where_clause_template = '"{}" = \'{}\''
		elif field.type=="Integer":
			where_clause_template = '"{}" = {}'
		else:
			print ("You have differnt data type other than \"string & numeric\" data types. \nScript stopped" )
			sys.exit()

# fetch field value and make unique list
with arcpy.da.SearchCursor(src,[srcField]) as cursor:
	for row in cursor:
		setAttr.append(row[0])
		row_count += 1
setAttr = list(set(setAttr))

print ('Number of row to process: {}'.format(row_count))
print ('Number of attribute to process: {}'.format(len(setAttr)))
print (setAttr)

# extract features as separate feature class export

in_features = src
for each in setAttr:    
    out_feature_class = outDir+"//"+ preffix + str(each) + ".shp"
    #where_clause = '"VTCODE" = \'{}\''.format(each)
    where_clause = where_clause_template.format(srcField,each)
    arcpy.Select_analysis(in_features, out_feature_class, where_clause)
    print ("{}_{}{} is saved..".format(preffix, each, ".shp"))
