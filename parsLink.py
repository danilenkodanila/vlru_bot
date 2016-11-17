import re
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

# print(doc)

cancel = ['http://www.newsvl.ru/accidents/2016/11/16/153571/', 'http://www.newsvl.ru/vlad/2016/11/16/153565/', 'http://www.newsvl.ru/vlad/2016/11/16/153583/', 'http://www.newsvl.ru/vlad/2016/11/16/153574/', 'http://www.newsvl.ru/vlad/2016/11/16/153570/', 'http://www.newsvl.ru/vlad/2016/11/16/153573/', 'http://www.newsvl.ru/vlad/2016/11/16/153568/', 'http://www.newsvl.ru/photos/2016/11/16/153578/', 'http://www.newsvl.ru/vlad/2016/11/16/153590/', 'http://www.newsvl.ru/society/2016/11/16/153592/']

count = 1
goSpam = ''

for element in cancel:
	doc = element
	soup = BeautifulSoup(urlopen(doc), "lxml")
	for wrapper in soup.find_all("h1", class_="story__title"):
		goSpam = goSpam + (str(count) + ") " +  '<a href="' + element + '">' + wrapper.text + '</a>' + '\n')
		count += 1
