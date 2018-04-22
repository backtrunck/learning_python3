#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      luiscar
#
# Created:     05/03/2018
# Copyright:   (c) luiscar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import PyPDF2
    f = open('sefip.pdf','rb')
    pdf = PyPDF2.PdfFileReader(f)
    fields = pdf.getFields()

    for key,field in fields:
        print("keys %s values %s") % (key,field)


    print(pdf.getNumPages())

if __name__ == '__main__':
    main()
