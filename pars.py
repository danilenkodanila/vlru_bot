from grab import Grab #импортируем граб для работы с парсингом

url = 'https://www.yandex.ru/'
xpath = '//div[@id="tabnews_newsc"]'

g = Grab()
g.go(url)
page = g.doc.select(xpath)

for element in page:
    s = element.html()
