#!C:/python366
# cut out Grid convergence area portion of utm map and save
from PIL import Image, ImageFilter
import sys, os
dst = r'D:\YeHtet_Works\utm_gc'
src = r'Y:\mm_topo50kUTM_SD_OMM\sourcedata\ScanOriginal'
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

my_files = list_files(src,"jpg")
if len(my_files):
    for file in my_files:
        try:
            img = Image.open(file)
    
        except IOError:
            print("Unable to load image")
            sys.exit(1)
        
        width, height = img.size
    
        x0 = int(width * 0.68) # left margin
        y0 = int(height * 0.88) # upper margin
        x1 = x0 + int(width * 0.15) # right margin 
        y1 = y0 + int(height * 0.10) # lower margin
        
        #The crop() method takes a 4-tuple defining the left, upper, right, and lower pixel coordinates. 
        img_crop = img.crop((x0,y0,x1,y1))
    
        img_crop.save(dst + "\\" + os.path.split(file)[1])
        img.close() # closing file will free up the memory
        print ( dst + "\\" + os.path.split(file)[1] + ' has been exported.')
else:
    print ("no file found in source directory and subdirectories....!")