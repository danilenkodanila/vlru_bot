#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import pars
from bs4 import BeautifulSoup
from urllib.request import urlopen


finish = []

text = []

def last():
	link = []
	title = []
	time = []
	global finish
	finish = []

	linkList = pars.update()
	soup = BeautifulSoup(urlopen(linkList[0].replace("\n","").replace("\t","").replace("\t","")), "lxml")
	data = soup.find_all("div", class_="last-stories")
	for div in data:
		links = div.findAll('a')
		for a in links:
			link.append("http://www.newsvl.ru" + a['href']) 

	for div in data:
		links = div.find_all('span', class_="last-stories__item-date")
		for span in links:
			# print(span.get_text())
			# title.append(span['last-stories__item-title'])
			time.append( span.get_text() )
	for div in data:
		links = div.find_all('span', class_="last-stories__item-title")
		for span in links:
			# print(span.get_text())
			title.append( span.get_text() )
			# time.append(span.get_text())))

	finish.append('Последние новости: \n' +  time[0] + ' <a href="' + link[0] + '">' + title[0] + '</a>' + '\n' +
										     time[1] + ' <a href="' + link[1] + '">' + title[1] + '</a>' + '\n' +
										     time[2] + ' <a href="' + link[2] + '">' + title[2] + '</a>' + '\n' +
										     time[3] + ' <a href="' + link[3] + '">' + title[3] + '</a>' + '\n' +
										     time[4] + ' <a href="' + link[4] + '">' + title[4] + '</a>' + '\n' +
										     time[5] + ' <a href="' + link[5] + '">' + title[5] + '</a>') 
	# print(finish)

	return finish