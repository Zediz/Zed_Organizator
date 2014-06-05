import ttk
import xlrd
from Tkinter import *

import xlrd
book = xlrd.open_workbook("hello.xlsx")
print "The number of worksheets is", book.nsheets
print "Worksheet name(s):", book.sheet_names()
sh = book.sheet_by_index(0)
print sh.name, sh.nrows, sh.ncols
print "Cell (2,0) is: ", sh.cell_value(colx =1, rowx=1)