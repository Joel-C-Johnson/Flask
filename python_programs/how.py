# import xlsxwriter
#
# workbook = xlsxwriter.Workbook('hello.xlsx')
# worksheet = workbook.add_worksheet()
#
# worksheet.write('A1', 'Hello world')
#
# workbook.close()
import io
from django.http.response import HttpResponse
from xlsxwriter.workbook import Workbook

def your_view(request):
    output = io.BytesIO()
    workbook = Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'Hello, world!')
    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=test.xlsx"
    return response
