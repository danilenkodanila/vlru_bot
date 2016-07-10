from grab import Grab #импортируем граб для работы с парсингом

url = 'https://news.yandex.ru/index.rss'
xpath = '//description'

g = Grab()
g.go(url)
page = g.doc.select(xpath)

for element in page:
    s = element.html()
