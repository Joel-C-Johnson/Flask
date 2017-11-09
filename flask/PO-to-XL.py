import polib
#import pdb

from xlwt import Workbook
wb=Workbook()
#pdb.set_trace()

po=polib.pofile('/home/joel/Documents/bha.po')
sheet1=wb.add_sheet('sheet1',cell_overwrite_ok=True)
sheet1.write(0,0,"msgid")
sheet1.write(0,1,"msgstr")
i=1
j=0
for entry in po:
    if (j==0):
		sheet1.write(i,j,entry.msgid)
		j +=1
		if(j==1):
		   	sheet1.write(i,j,entry.msgstr)
		   	j = 0
    i = i+1

wb.save('xlwt.xls')
