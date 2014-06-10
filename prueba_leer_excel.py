#! /usr/bin/python
# -*- coding: utf-8 -*

import xlrd

book = xlrd.open_workbook("data_new.xls")
print "The number of worksheets is", book.nsheets
print "Worksheet name(s):", book.sheet_names()
sh = book.sheet_by_index(0)
print sh.name, sh.nrows, sh.ncols
print "Cell (2,0) is: ", sh.cell_value(rowx=17, colx=21)

