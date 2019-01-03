import arcpy,csv,os 

mydir = r'Y:\\SurveyDepartment_TNTexports_TGO\\'
file = r'D:\\test\\sd_layers.txt'
outfile = file 

# listing all files in subdirectoires
def list_files(dir): 
    r = [] 
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs: 
        files = os.walk(subdir).next()[2] 
        if (len(files) > 0): 
            for file in files: 
                r.append(subdir+ '\\' + file) 
    return r
print("just 1")
# #--loop through subdirectories and all files endin in .shp, list fields in a new row
with open(outfile,'w+') as f:
    w = csv.writer(f)	
    for file in list_files(mydir):
        if file.endswith(".shp"):
            desc = arcpy.Describe(file)
            geomtype = ([desc.shapeType])
            file_type = ([mydir])
            file_type.extend([file])
            file_type.extend(geomtype)
            w.writerow(file_type)
f.close
print("successfully complete")