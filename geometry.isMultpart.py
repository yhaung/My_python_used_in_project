 arcpy.env.workspace = r"C:\Users\Dell\Desktop\Temp_KHA\Temp_Test.gdb"
 
 fcList = arcpy.ListFeatureClasses("multipart")
 arcpy.AddField_management("multipart", "isMulti", "TEXT")
 for fc in fcList:
 
     with arcpy.da.UpdateCursor(fc, ["SHAPE@", "vill_name", "isMulti"]) as cursor:
         for row in cursor:
 
             geometry = row[0]
 
             if geometry.isMultipart == True:
                 print
                 "{0} is Multipart".format(row[1])
                 row[2] = "yes"
                 cursor.updateRow(row)