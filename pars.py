#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
from grab import Grab 

mainString = ''
s = []

# ______________________________________________________________________________________________________________________________
def update():
	global mainString
	global s
	url = 'http://www.newsvl.ru/rss'
	xpath = '//title'
	xpath1 = '//link'

	g = Grab()
	g.go(url)
	# считываем заголовки
	page = g.doc.select(xpath)
	# считываем ссылки
	page1 = g.doc.select(xpath1) 

	mainString = ''
	# "-1" — ибо первый заголовок и ссылка не нужны (это ссылка на rss и заголовок соответствующий)
	count = -1 
	s = [] # массив ссылок

	count = -2 

	for element in page1: #цикл считывающий линки
		count = count + 1
		if count > 0:
			s.append(element.html().replace("<link>","").replace("\n","").replace("\t",""))
			
	count = -1
	lol = 0

	for element in page: #цикл считывающий заголовки
		count = count + 1
		if count > 0: 
			mainString = mainString + (str(count) + ") " +  '<a href="' + s[lol] + '">' + element.html().replace("<title>","").replace("</title>","").replace("  ","").replace("\n","").replace("\s","").replace("\t","")  + '</a>' + '\n') #формирование номера новости
			lol += 1
	return s
# ______________________________________________________________________________________________________________________________

update()




