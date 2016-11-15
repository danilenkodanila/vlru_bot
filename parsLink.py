#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import pars

from grab import Grab #импортируем граб для работы с парсингом

url = pars.s.pop()

#url = 'http://www.newsvl.ru/society/2016/11/06/153268/'

xpath = ('//div[@class="story__text"]')

# print(url)

g = Grab()
g.go(url)

try:
     # print(g.doc.select(xpath).text())
except IndexError:
     # print('not found')

