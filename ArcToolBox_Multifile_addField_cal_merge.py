# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Model_Multifile_addField_cal_merge.py
# Create by: Kyaw Naing Win
# Created on: 2019-03-07 00:34:33.00000
#   
# Description: The script will add BLD_CODE column and add IDs into each building shapefiel
# finally all will be mearged into single file
# for DoP inter census GIS tasks
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy, os


# Local variables:
src_dir = arcpy.GetParameterAsText(0) # get folder from dialogbox
#src_dir = r"C:\TempGIS\DOP\15010110_Test"

dst_dir = src_dir
fld = src_dir.split("\\")[-1:] # extract main folder name for using in merge file name
Field_Name = "BLD_CODE"
bld_merge_shp = dst_dir + "\\" + fld[0] +"_bld_merged.shp"

def list_files(pdir, file_type = ""):                                                                                                  
    r = []                                           
    subdirs = [x[0] for x in os.walk(pdir)]
    for subdir in subdirs:              
        files = next(os.walk(subdir))[2]                  
        if (len(files) > 0):                                                        
            for file in files:
                if (len(file_type)):
                    file_ext = "." + file_type
                    if file.endswith(file_ext.lower()) or file.endswith(file_ext.upper())  :            
                        r.append(subdir+ '\\' + file)
                else:
                    r.append(subdir+ '\\' + file)
                    
    return r

my_files = list_files(src_dir,"shp")
print ("Building codes are being added to below files..")
for shp in my_files:

    # Process: Add Field
    arcpy.AddField_management(shp, Field_Name, "SHORT", "", "", "", "", "NULLABLE", "REQUIRED", "")

    # Process: Calculate Field
    arcpy.CalculateField_management(shp, "BLD_CODE", "[FID] + 1", "VB", "")
  
    print ("  "+shp + " ... ")
print ("building codes added")
# Process: Merge
arcpy.Merge_management(my_files, bld_merge_shp)
print ("All building with codes merged as " + bld_merge_shp)
print ("Processing finished")