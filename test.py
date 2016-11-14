#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import pars
from bs4 import BeautifulSoup
from urllib.request import urlopen



text = []

# soup = BeautifulSoup(urlopen(doc))
# print(soup.text)
 
# mydivs = soup.find_all("div", class_="story__text")

# mainString = mainString.replace("<title>","").replace("</title>","").replace("  ","") #обрезаем говно

# print(mydivs.get_text())

# for el in soup.find_all('div', attrs={'class': 'story__text'}):
#         s = s + el.get_text()

# print(s)
def funcText(number):
	pars.update()
	print('NUMBER         ', number)
	doc = pars.s[number]
	s = pars.s[number]
	soup = BeautifulSoup(urlopen(doc))
	print(doc)
	for el in soup.find_all('div', attrs={'class': 'story__text'}):
		s = s + el.get_text()
	return s

# for i in range(1,20):
# 	doc = pars.s[i]
# 	print(doc)
# 	soup = BeautifulSoup(urlopen(doc))
# 	for el in soup.find_all('div', attrs={'class': 'story__text'}):
# 		text.append(el.get_text())

# print(text[1])