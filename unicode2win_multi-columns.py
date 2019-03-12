# ---------------------------------------------------------------------------
# unicode2win_multi-columns.py
# Create by: Kyaw Naing Win
# Created on: 2019-03-10
#   
# Description: The script will convert unicode to WinInnwa font in an excel file
# it can process multiple columns
# for DoP inter census GIS tasks
# ---------------------------------------------------------------------------
# required: python-myanmar, pandas and os modules

from myanmar.converter import convert as mc
import pandas as pd
import os

# excel file parameters
excel = r"D:\Programming\Python_Summary_for_OMM\unicode2win_multi-columns\Random_unicode.xls" # excel file path and name
sheet = "Sheet1" # target sheet for conversion
uni_cols = ['col1', 'col2' , 'col3'] # target columns with unicode texts as list of colum names ['col1','col2','col3']


df = pd.read_excel(excel, sheet_name=sheet)
print ("Processing starts...\nignore some alerts from pandas module")
for col in uni_cols:
    win_col = 'WIN_' + col
    print (col + " column is being processed..")
    df[win_col] = ''
    for i in df.index:
        unicode = df.loc[i][col]
        if (unicode!=''):
            wincode = mc(unicode, 'unicode', 'wininnwa')
            df.at[i, win_col] = wincode


folder, file = os.path.split(excel)
ext = file.find(".") - len(file)
file = file[:ext]+ "_winInnwa.xls"

df.to_excel(folder + "\\" + file, index = False)

print ("\nUnicode to WinInnwa conversion finished. New file " + file + " is generated under same folder")