import re
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

finish = []

def updateHot():
	global finish
	doc = 'http://www.newsvl.ru/'

	link = []
	title = []
	finish = []

	soup = BeautifulSoup(urlopen(doc), "lxml")

	data = soup.find_all("div", class_="inset__content inset__content_hot")
	for div in data:
	    links = div.findAll('a')
	    for a in links:
	        link.append("http://www.newsvl.ru" + a['href']) # считываем ссылки горячих новостей
	        title.append(a['title']) # считываем заголовки горячих новостей

	finish.append('Горячие новости: \n1) ' + '<a href="' + link[0] + '">' + title[0]+ '</a>' + '\n'+ '2) ' + '<a href="' + link[1] + '">' +title[1]  + '</a>' + '\n' + '3) ' + '<a href="' + link[2] + '">' + title[2] + '</a>') 
	return(1)

