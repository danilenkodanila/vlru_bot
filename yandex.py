from grab import Grab 

g = Grab()
url = 'https://news.yandex.ru/index.rss'
g.go(url)

print (g.doc.text_search(u'Яндекс'.encode('utf-8'), byte=True))