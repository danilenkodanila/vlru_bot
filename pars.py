#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
from grab import Grab #импортируем граб для работы с парсингом

url = 'https://news.yandex.ru/index.rss'
xpath = '//title'

g = Grab()
g.go(url)
page = g.doc.select(xpath)

s = ""
for element in page:
    s = s + element.html()
s = s.replace("<title>","").replace("</title>","")

