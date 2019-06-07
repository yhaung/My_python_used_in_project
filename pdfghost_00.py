# convert pdf to web pdf or optimized pdf with Ghostscript

'''
install ghostscript
get ghostscript installer from https://www.ghostscript.com/download/gsdnld.html

PDFSETTINGS:

    /screen selects low-resolution output similar to the Acrobat Distiller "Screen Optimized" setting.
    /ebook selects medium-resolution output similar to the Acrobat Distiller "eBook" setting.
    /printer selects output similar to the Acrobat Distiller "Print Optimized" setting.
    /prepress selects output similar to Acrobat Distiller "Prepress Optimized" setting.
    /default selects output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file.
'''

import subprocess
import os

# ghostscript exe path
gs_cmd = r"C:\Program Files\gs\gs9.27\bin\gswin64c.exe"

# folders
input_dir = r"D:\mgw_CFpermitsFD_OMM\cf_permits"
output_dir = r"D:\mgw_CFpermitsFD_OMM\cf_permits"

input_filename = r"nmt_001_Pi_Tauk_Ngoke_Ywar_Thit.pdf"

def pdf2pdf (input_pdf, suffix = "_mobile"):
    
    if input_pdf[-3:] == "pdf" or input_pdf[-3:] == "PDF":
     
        cmd_args = []
        
        if suffix: suffix = "_"+suffix
            
        output_pdf = input_pdf[:-4] + suffix + ".pdf"
        
        sub_cmds = "-sDEVICE=pdfwrite -dCompatibilityLevel=2 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile="
        input_pdf = input_dir+os.sep+input_pdf
        output_pdf = output_dir+os.sep+output_pdf
        #ghostscript -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
        
        #cmd_args += (gs_cmd, sub_cmds, output_pdf, input_pdf)
        cmds = (gs_cmd + " " + sub_cmds + output_pdf+" "+input_pdf)
        subprocess.run(cmds)
       
    else:
        print ("{} is not pdf format and skipped..".format(input_pdf))
    
    print ("\n"+input_filename+" reduced file size..")

    
pdf2pdf(input_filename)