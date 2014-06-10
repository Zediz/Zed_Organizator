#! /usr/bin/python
# -*- coding: utf-8 -*-


from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

today = date.today()
year = rrule(YEARLY,bymonth=8,bymonthday=16,byweekday=FR)[0].year
rdelta = relativedelta(easter(year), today)

fechacreada=date(2014,06,1)
now = date.today()
relaitive =str(relativedelta(now, fechacreada,))

pasado_manyana = str(fechacreada)

def weeks_between(start,end):
	weeks = rrule(WEEKLY,dtstart=start,until=end)
	return weeks.count()


print "Hoy es:", today
print "El próximo año en que el 13 de agosto es viernes es el :", year
print "Faltan %s días para el Día de Pascua." %(rdelta)
print "Pascua de ese año es el %s." %(today+rdelta)
print fechacreada
print relaitive
print weeks_between(fechacreada,now)
print pasado_manyana
print "********************"
print pasado_manyana[5:7] #Mes
print pasado_manyana[0:4] #año
print pasado_manyana[8:10]