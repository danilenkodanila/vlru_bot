#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import pars
from bs4 import BeautifulSoup
from urllib.request import urlopen


s = ""
s2 = ""
text = []


def funcText(number):
	global s
	global s2
	pars.update()
	# print('NUMBER         ', number)
	doc = pars.s[number]
	s2 = ""
	s3 = ""
	s = pars.s[number]
	soup = BeautifulSoup(urlopen(doc), "lxml")
	# print(doc)
	for el in soup.find_all('div', attrs={'class': 'story__text'}):
		s = s + el.get_text()
	if len(s) > 4096:
		s3 = s
		s2 = s[0:4096]
		s = s[4096:len(s)]
		s3 = s
		s = s2
		s2 = s3

	print("s", s)
	print("s2", s2)
	return s
