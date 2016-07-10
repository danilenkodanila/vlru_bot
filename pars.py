#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('cp866') # устанавливаем кодировку вывода консоли
from grab import Grab #импортируем граб для работы с парсингом

url = 'https://news.yandex.ru/index.rss'
xpath = '//title'

g = Grab()
g.go(url)
page = g.doc.select(xpath)

mainString = ""
count = -2

for element in page:
	count = count + 1
	if count > 0:
		mainString = mainString + str(count) + ") " + element.html()


mainString = mainString.replace("<title>","").replace("</title>","").replace("  ","")