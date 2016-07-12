from grab import Grab
import logging

g = Grab()
g.go('https://news.yandex.ru/yandsearch?cl4url=regnum.ru%2Fnews%2Fpolit%2F2156222.html&lr=75&lang=ru&rubric=index')

print(g.xpath_text('//a[@class="link link_theme_normal i-bem link_js_inited"]') 