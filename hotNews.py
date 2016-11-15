import re
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

doc = 'http://www.newsvl.ru/'
# print(doc)

link = []
title = []
finish = []

soup = BeautifulSoup(urlopen(doc))

data = soup.find_all("div", class_="inset__content inset__content_hot")
for div in data:
    links = div.findAll('a')
    for a in links:
        link.append("http://www.newsvl.ru" + a['href'])



data = soup.find_all("div", class_="inset__content inset__content_hot")
for div in data:
    links = div.findAll('a')
    for a in links:
        title.append(a['title'])


print(link)
print(title)

finish.append('1) ' + '<a href="' + link[0] + '">' + title[0]+ '</a>' + '\n'+ '2) ' + '<a href="' + link[1] + '">' +title[1]  + '</a>' + '\n' + '3) ' + '<a href="' + link[2] + '">' + title[2] + '</a>') 
print(finish)

def updateHot():
	doc = 'http://www.newsvl.ru/'
	print(doc)

	link = []
	title = []
	finish = []

	soup = BeautifulSoup(urlopen(doc))

	data = soup.find_all("div", class_="inset__content inset__content_hot")
	for div in data:
		links = div.findAll('a')
		for a in links:
			link.append("http://www.newsvl.ru" + a['href'])



	data = soup.find_all("div", class_="inset__content inset__content_hot")
	for div in data:
		links = div.findAll('a')
		for a in links:
			title.append(a['title'])


	# print(link)
	# print(title)

	finish.append('1) ' + '<a href="' + link[0] + '">' + title[0]+ '</a>' + '\n'+ '2) ' + '<a href="' + link[1] + '">' +title[1]  + '</a>' + '\n' + '3) ' + '<a href="' + link[2] + '">' + title[2] + '</a>') 
	# print(finish)
	return(1)

# finish.append('1) ' + '<a href="https://news.yandex.ru/yandsearch?cl4url=regnum.ru/news/society/2202110.html&lang=ru&from=main_portal&lr=75">Госорганы РФ не смогут требовать от граждан 85 видов справок</a>' + '\n'+ '2) ' + '<a href="https://news.yandex.ru/yandsearch?cl4url=www.kommersant.ru/doc/3135777&lang=ru&from=main_portal&lr=75">Украина предоставит коридор для российских войск в Приднестровье</a>' + '\n' + '3) ' + '<a href="https://news.yandex.ru/yandsearch?cl4url=www.rbc.ru/politics/07/11/2016/58205a429a79479cbd632f95&lang=ru&from=main_portal&lr=75">Саакашвили объявил об уходе в отставку</a>') 




