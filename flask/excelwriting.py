from xlwt import Workbook
import xlwt
wb=Workbook()
style_string = "font: bold on; borders: bottom dashed"
style = xlwt.easyxf(style_string)
l = ["joel","manu","arun","jobin"]
sheet1=wb.add_sheet('sheet1',cell_overwrite_ok=True)
sheet1.write(0,0,"token",style=style)
sheet1.write(0,1,"translation",style=style)
j = 0
i = 1
for e in l:
    sheet1.write(i,j,e)
    i = i + 1
wb.save('xlwt.xls')
