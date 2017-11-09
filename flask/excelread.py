# import xlsxwriter
# a = ['January\n','February\n','March\n','April\n','May\n','June\n']
# xbook = xlsxwriter.Workbook('Test.xlsx')
# xsheet = xbook.add_worksheet('Test')
# j = 0
# i = 1
# for e in a:
#     xsheet.write(i,j,e)
#     i = i + 1
# xbook.close()



# len(p.col_values(1))   # -----------find the values in a specified column
# cell = p.cell(0,1)      # --- to find the cell value
# print cell.value
# p.col(1,1) (c,r)



from xlrd import open_workbook
import xlrd
import json, ast
book = open_workbook('/home/joel/Documents/flask/xlwt.xls')
p=book.sheet_by_index(0)
count = 0
for c in range(p.nrows):                                   #| to find a cell is empty
    cell = p.cell(c,1).value                                 #|
    if cell:
        count = count + 1
if count > 1:
    token_c = (token_c.value for token_c in p.col(0,1))
    tran = (tran.value for tran in p.col(1,1))
    data = dict(zip(token_c, tran))
    m = ast.literal_eval(json.dumps(data))     #------ remove unicode (u'joel)
    print m
else:
    print "no transltion to Upload"

# token_c = (token_c.value for token_c in p.col(0,1))
# tran = (tran.value for tran in p.col(1,1))
# data = dict(zip(token_c, tran))
# m = ast.literal_eval(json.dumps(data))     #------ remove unicode (u'joel)
# print m
# print "nothing"

#
# token_c = (token_c.value for token_c in range(1,p.col(0)))
# tran = (tran.value for tran in range(1,p.col(1)))
# data = dict(zip(token_c, tran))
# dic = ast.literal_eval(json.dumps(data))
#





# import xlrd
# from xlrd import open_workbook
# import arcpy
#
# wb = open_workbook('/home/joel/Documents/flask/xlwt.xls')
# sheet = wb.sheet_by_index(0)
# sheetdict = {}
# for rownum in range(sheet.nrows):
#     sheetdict[sheet.cell(rownum,1)] = [sheet.cell(rownum,15),sheet.cell(rownum,16)]




# import xlrd
# workbook = xlrd.open_workbook('/home/joel/Documents/flask/xlwt.xls')
# workbook = xlrd.open_workbook('/home/joel/Documents/flask/xlwt.xls', on_demand = True)
# worksheet = workbook.sheet_by_index(0)
# first_row = [] # Header
# for col in range(worksheet.ncols):
#     first_row.append( worksheet.cell_value(0,col) )
# # tronsform the workbook to a list of dictionnaries
# data =[]
# for row in range(1, worksheet.nrows):
#     elm = {}
#     for col in range(worksheet.ncols):
#         elm[first_row[col]]=worksheet.cell_value(row,col)
#     data.append(elm)
# print data




# n=p.nrows - 1
# for i in range(1,n):
#     msgid=p.cell_value(i,j),msgstr=p.cell_value(i,j+1))
#     po.append(xl)
# po.save('/home/joel/Documents/flask/xlwtttt.po')


# from pandas import *
# xls = ExcelFile('/home/joel/Documents/flask/xlwt.xls')
# df = xls.parse(xls.sheet_names[0])
# print str(df.to_dict())



# import pandas as pd
# my_dic = pd.read_excel('/home/joel/Documents/flask/xlwt.xls', index_col=0).to_dict()
# print my_dic
