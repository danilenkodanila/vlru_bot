from grab import Grab
import logging

g = Grab()
g.go('https://news.yandex.ru/yandsearch?cl4url=izvestia.ru%2Fnews%2F624707')

print(g.xpath_text('//a[@class="link link_theme_normal i-bem link_js_inited"]')  #чтобы новый коммент грузануть напишу это