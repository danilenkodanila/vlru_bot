#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import pars
from bs4 import BeautifulSoup
from urllib.request import urlopen

text = []

def funcText(number):
	pars.update()
	doc = pars.s[number]
	s = pars.s[number]
	soup = BeautifulSoup(urlopen(doc), "lxml")
	for el in soup.find_all('div', attrs={'class': 'story__text'}):
		s = s + el.get_text()
	return s
