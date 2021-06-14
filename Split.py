import xlrd

data = xlrd.open_workbook('./1.xls')

print data.sheet_names()

row = print table.row_values(1)
#print table.col_values(1)

table = data.sheet_by_index(0)

for i in range(row+1):
	print table.cell(i, 6).value