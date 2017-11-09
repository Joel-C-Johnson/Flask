from xlwt import Workbook
wb = Workbook()
sheet1=wb.add_sheet('sheet1',cell_overwrite_ok=True)
sheet1.write(0,0,"S_N")
sheet1.write(0,1,"TOKENS")
sheet1.write(0,2,"REFERENCE")
i=1
j=1
data = ['This', 'another', 'is', 'line', 'test']
for entry in data:
    if entry:
		sheet1.write(i,j,entry)
		i +=1

	#	if(j==1):
	#	   	sheet1.write(i,j,entry)
	#	   	j = 0
#    i = i+1

wb.save('xlwt.xls')
