#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
#reload(sys)
#sys.setdefaultencoding('cp866') # устанавливаем кодировку вывода консоли
from grab import Grab #импортируем граб для работы с парсингом


url = 'http://www.newsvl.ru/rss'
xpath = '//title'
xpath1 = '//link'

#все переменные без приставки "1" нужны для считывания тайтлов
g = Grab()
g.go(url)
page = g.doc.select(xpath)

#все переменные с приставкой "1" нужны для считывания линков
g1 = Grab()
g1.go(url)
page1 = g1.doc.select(xpath1)


stroka = []

mainString = ''
count = -1
s = [] #массив ссылок, используем тип данных "список" (list)
i = 0 

count = -2 

for element in page1: #цикл считывающий линки
	count = count + 1
	if count > 0:
		s.append(element.html()) # list.append — добавляет элемент в конец списка

for element in s:
     s[i] = s[i].replace("<link>","")
     i = i + 1

count = -1
lol = 0
for element in page: #цикл считывающий заголовки
	count = count + 1
	if count > 0: #ограничение по канту нужно, чтобы не считать первые ненужные заголовки НЕ НОВОСТЕЙ. С 3 тайтла идут те заголовки, что нам нужны
		mainString = mainString + (str(count) + ") " +  '<a href="' + s[lol].replace("\n","").replace("\s","").replace("\t","") + '">' + element.html().replace("<title>","").replace("</title>","").replace("  ","").replace("\n","").replace("\s","").replace("\t","")  + '</a>' + '\n') #формирование номера новости
		lol += 1

print(mainString)




# + element.html().replace("<title>","").replace("</title>","").replace("  ","") 
# mainString = mainString.replace("<title>","").replace("</title>","").replace("  ","") #обрезаем говно

 #обрезаем тег <link> в каждом элементе списка и получаем на выход готовые линки
 #замечу, что линки в списке идут с позиции №2 — ибо первой ссылкой парсится ссылка на яндекс новости, а дальше уже ссылки на конкретные события









