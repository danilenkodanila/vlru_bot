# -*- coding: utf-8 -*-
import schedule
import time
from grab import Grab #импортируем граб для работы с парсингом
import re
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pars 

from apscheduler.schedulers.blocking import BlockingScheduler

listLink = []
s = []
number = [],[]
dictionary = {}
cancel = []

def everyHour():
	print("work everyHour")
	s = pars.update()
	link = []
	for element in s:
		try:
			listLink.remove(element)
		except ValueError:
			listLink.append(element)
	for element in listLink:
		soup = BeautifulSoup(urlopen(element.replace("\n","").replace("\t","").replace("\t","")))
		number[1].append(element.replace("\n","").replace("\t","").replace("\t",""))
		try:
			if soup.find("a", class_="story__info-comments-count") != None: # better: if item is not None
				data = soup.find("a", class_="story__info-comments-count")
				for contents in data:
					number[0].append(contents)
			else:        
				raise TypeError 
		except TypeError:
			number[0].append('0')
	i = 0
	for element in number[0]:
		dictionary[int(number[0][i])] = number[1][i]
		i += 1

	l = dictionary.keys() # получаем ключи
	l = list(l) # превращаем его в обычный список
	l.sort() # сортируем список
	l.reverse()
	f = 0
	global cancel
	cancel = []
	for i in l: # вывод элементов словаря (ключ - значение) по алфавиту
		if f < 10:
			cancel.append(dictionary[i])
		f += 1

def everyDay():
	global cancel
	print("work everyDay")
	# print(cancel)
	cancel = []



# count:  [<a class="story__info-comments-count" data-notation="Количество комментариев" href="#comments">8</a>]

scheduler = BlockingScheduler()
scheduler.add_job(everyHour, 'interval', hours=0.001)
scheduler.add_job(everyDay, 'interval', hours=0.01)
scheduler.start()


