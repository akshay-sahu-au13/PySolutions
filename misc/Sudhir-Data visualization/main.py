# import xlsxwriter
# workbook = xlsxwriter.Workbook('c:\\temp\\Welocme.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.write('A1', 'Name')
# worksheet.write('B1', 'Department')
 
# row = 1
# col = 0
 
# data = ( 
#     ['Rajendra', 'IT'], 
#     ['Kashish','Physiotherapist'], 
#     ['Arun', 'Student'], 
#     ['Rohan','Bank Manager'], 
#     ['Akshay','Bank Officer']
# ) 
 
# for name, score in (data): 
#     worksheet.write(row, col, name) 
#     worksheet.write(row, col + 1, score) 
#     row += 1
# workbook.close()

#############################################################################
from threading import Timer

import xlsxwriter
workbook = xlsxwriter.Workbook('c:\\temp\\Welocme.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Department')
 
row = 1
col = 0
 
data = ( 
    ['Rajendra', 'IT'], 
    ['Kashish','Physiotherapist'], 
    ['Arun', 'Student'], 
    ['Rohan','Bank Manager'], 
    ['Akshay','Bank Officer']
) 


 
for name, score in (data): 
    worksheet.write(row, col, name)
    r = Timer(1.0, worksheet.write, (row, col, name) ) 
    r.start()

    worksheet.write(row, col + 1, score)
    s = Timer(1.0, worksheet.write, (row, col + 1, score) )
    s.start()
    row += 1
workbook.close()