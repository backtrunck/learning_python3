import numpy as np
import pandas as pd

#tipos = {0:str,1:str, 'C':str, 'D':str, 'E':str, 'F':str, 'G':str, 'H':str, 'I':str, 'J':str, 'K':str, 'L':str, 'M':str, 'N':str, 'O':str, 'P':str, #'Q':str, 'R':str, 'S':str, 'T':str, 'U':str, 'V':str, 'W':str, 'X':str, 'Y':str, 'Z':str, 'AA':str, 'AB':str, 'AC':str, 'AD':str, 'AE':str, 'AF':str, #'AG':str, 'AH':str, 'AI':str, 'AJ':str, 'AK':str, 'AL':str} 

#file = 'ConsultaPagamentoRelsao.felix_02.xls'
#x1 = pd.ExcelFile(file)
#df1 = x1.parse('ConsultaPagamentoRel')
#planilha = pd.read_excel(x1,'ConsultaPagamentoRel',usecols=[0, 1,2, 3,5,6],converters = tipos)

#print(planilha.values)

from xlrd import open_workbook,cellname

workbook = open_workbook('ConsultaPagamentoRelsao.felix_02.xls')
sheet = workbook.sheet_by_index(0)

for row_index in range(sheet.nrows):       
    for col_index in range(sheet.ncols):    

        print(cellname(row_index,col_index),'-',  sheet.cell_value(row_index,col_index))



