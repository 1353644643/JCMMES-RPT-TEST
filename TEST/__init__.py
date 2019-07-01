# -*- coding : utf-8 -*-
import xlwt  # 写xls
import xlrd  # 读xls
from xlutils.copy import copy

file_tb1 = xlwt.Workbook()  # 创建工作簿
sheet1 = file_tb1.add_sheet(u'test1', cell_overwrite_ok=True)
sheet2 = file_tb1.add_sheet(u'test2', cell_overwrite_ok=True)

row = 0
temp = [u'学校', u'学院', u'专业', u'学号', '姓名', '总成绩']
for v_pos, v in enumerate(temp):  # enumerate枚举一个可遍历的数据对象,返回序号和对象
    sheet1.write(row, v_pos, v)
row += 1
sheet1.write(row, 0, u'华南理工大学')  # 在Excel中用row,col定位表格
sheet1.write(row, 1, '计算机学院')
sheet1.write(row, 2, u'计算机科学与技术')
sheet1.write(row, 3, u'3548241456')
sheet1.write(row, 4, u'路人甲')
sheet1.write(row, 5, u'413')

# 向工作表单元格写入公式
sheet1.write_formula(0, 0, '=B3 + B4')
sheet1.write_formula('A7', '{=SUM(A1:B1*A2:B2)}')
sheet1.write(5, 0, u'总分统计')

sheet2.write_merge(1, 2, 3, 4, u'合并文本')  # 合并单元格
# write_merge(x, x + h, y,  y + w, string, sytle)
file_tb1.save('F://temp_data/xlwt_tutorial_9.xls')

file_tb1 = xlrd.open_workbook(r'F://temp_data/xlwt_tutorial_9.xls')
print(file_tb1.sheet_names())  # 然后输出所有sheet名

for i in range(len(file_tb1.sheet_names())):  # 得到表格里的所有的sheet
    sheet_n = file_tb1.sheet_by_index(i)

sheet1 = file_tb1.sheet_by_index(0)  # 打开第一个sheet
sheet2 = file_tb1.sheet_by_name(u'test2')  # 打开名字为 test2 的sheet

# 输出sheet的名称,行数,列数
print(sheet1.name, sheet1.nrows, sheet1.ncols)
print(sheet2.name, sheet2.nrows, sheet2.ncols)

# 获取单元格内容
print(sheet1.cell(1, 0).value)

# 获取单元格内容的数据类型
print(sheet1.cell(1, 1).ctype)
# ctype : 0 empty, 1 string, 2 number, 3 date, 4 boolean, 5 error

# 如果想对原有的Excel文件的基础上进行编辑，就要用到xlutils包了，因为xlwt,xlrd是只写和只读
# 用xlrd打开一个文档，后采用xlutils中copy功能把文档拷贝，然后进行编辑保存即可
file_tb1 = xlrd.open_workbook(r'F://temp_data/xlwt_tutorial.xls')
file_tb2 = copy(file_tb1)  # 将 file_tb1 拷贝到 file_tb2

sheet1 = file_tb2.get_sheet(0)  # 打开sheet1
print(sheet1.name)
sheet1.write(6, 6, 'change')  # 更改(7,7)单元格数据(原先有数据则会覆盖)

file_tb2.save('F://temp_data/xlwt_tutorial_copy.xls')  # 保存为xls文件(不能是xlsx)

wd.quit()


















