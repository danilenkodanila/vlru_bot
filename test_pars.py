#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
#reload(sys)
#sys.setdefaultencoding('cp866') # устанавливаем кодировку вывода консоли
from grab import Grab #импортируем граб для работы с парсингом

url = 'https://news.yandex.ru/index.rss'
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

mainString = "" 
count = -2
s = [] #массив ссылок, используем тип данных "список" (list)
i = 0 

for element in page: #цикл считывающий заголовки
	count = count + 1
	if count > 0: #ограничение по канту нужно, чтобы не считать первые ненужные заголовки НЕ НОВОСТЕЙ. С 3 тайтла идут те заголовки, что нам нужны
		mainString = mainString + str(count) + ") " + element.html() #формирование номера новости

for element in page1: #цикл считывающий линки
	count = count + 1
	if count > 0:
		s.append(element.html()) # list.append — добавляет элемент в конец списка

mainString = mainString.replace("<title>","").replace("</title>","").replace("  ","") #обрезаем говно

 #обрезаем тег <link> в каждом элементе списка и получаем на выход готовые линки
 #замечу, что линки в списке идут с позиции №2 — ибо первой ссылкой парсится ссылка на яндекс новости, а дальше уже ссылки на конкретные события
for element in s:
     s[i] = s[i].replace("<link>","")
     i = i + 1

#обрезаем все то, что идет до названия интернет источника
i = 0
for element in s:
     s[i] = s[i].replace("<link>","").replace("https://news.yandex.ru/yandsearch?cl4url=", "")
     i = i + 1

#обрезаем все то, что идет после интернет-источника
i = 0
find = 0
linkString = ""
for element in s:
     i = i + 1
     if i > 1 and i < 17:
     		linkString = s[i]
     		find = linkString.find('.ru')
     		linkString = linkString[0:find+3]
     		s[i] = linkString

url2 = s[2]

#все переменные без приставки "1" нужны для считывания тайтлов
g2 = Grab()
g2.go(s[2])

#g2.search(u'яндекс')
#print(s)




