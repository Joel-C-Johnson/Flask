from xlwt import Workbook
import xlrd
#import pdb
wb=Workbook()
import polib
#pdb.set_trace()


book=xlrd.open_workbook('/home/joel/Documents/flask/xlwt.xls')
p=book.sheet_by_index(0)
n=p.nrows - 1
po = polib.POFile()
po.metadata = {
    'Project-Id-Version': '1.0',
    'Report-Msgid-Bugs-To': 'you@example.com',
    'POT-Creation-Date': '2007-10-18 14:00+0100',
    'PO-Revision-Date': '2007-10-18 14:00+0100',
    'Last-Translator': 'you <you@example.com>',
    'Language-Team': 'English <yourteam@example.com>',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
}


i=0
j=0
for i in range(1,n):
    xl = polib.POEntry(msgid=p.cell_value(i,j),msgstr=p.cell_value(i,j+1))
    po.append(xl)


po.save('/home/joel/Documents/flask/xlwtttt.po')
