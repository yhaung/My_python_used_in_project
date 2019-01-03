#https://stackoverflow.com/questions/40828450/python-copy-folder-structure-under-another-directory

import os

inputpath = r'Y:\\SurveyDepartment_TNTexports_TGO\\'
outputpath = 'D:\\Temp1\\'

for dirpath, dirnames, filenames in os.walk(inputpath):
    structure = os.path.join(outputpath, dirpath[len(inputpath):])
    if not os.path.isdir(structure):
        os.mkdir(structure)
    else:
        print("Folder does already exits!")
