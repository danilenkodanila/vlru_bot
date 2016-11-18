import config #импортирую файл конфиг из этой же папки
import pars #импортирую файл парс из этой же папки
import telebot #с помощью этой библиотеки строится бот
import test
import hotNews
import sendSpam
import pytz
import schedule
import time
import re
import sys
import lastNews

from grab import Grab #импортируем граб для работы с парсингом
from time import sleep
from multiprocessing import Process
from bs4 import BeautifulSoup
from urllib.request import urlopen
from apscheduler.schedulers.blocking import BlockingScheduler
from telebot import types
from datetime import datetime, date, time

spamId = []
spamUsers = []
cancel = []
number = [],[]
dictionary = {}
listLink = []

class A:
    def __call__(self, count=1, sleep_time=0.5):
        bot = telebot.TeleBot(config.token) #создаем бота
        answer = pars.mainString #это то, что будем посылать в ответ
        setNews = 0 #если посылали новости, то 1, если нет, то 0
# ______________________________________________________________________________________________________________________________
        # реакция на команду /news
        # сначала обновляем список новостей ( pars.update() )
        # потом прикрепляем кнопку с ссылкой на сайт
        @bot.message_handler(commands=['news', 'новости', 'Новости', 'НОВОСТИ']) #реакция на КОМАНДЫ 
        def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
            pars.update()
            answer = pars.mainString
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на newsvl.ru", url="http://www.newsvl.ru/")
            keyboard.add(url_button)
            setNews = 1
            bot.send_message(message.chat.id, answer, parse_mode='HTML', disable_web_page_preview = True, reply_markup=keyboard) #посылаем в ответ 
# ______________________________________________________________________________________________________________________________
        # реакция на команду /hotnews
        # сначала обновляем горячие новости ( updateHot() )
        # потом посылаем в ответ горячие новости
        @bot.message_handler(commands=['hotnews', 'HotNews', 'hot', 'горячиеНовости']) 
        def repeat_all_messages(message): 
            hotNews.updateHot()
            bot.send_message(message.chat.id, hotNews.finish[0], parse_mode='HTML', disable_web_page_preview = True)
# ______________________________________________________________________________________________________________________________
        # реакция на команду /lastNews
        @bot.message_handler(commands=['lastNews', 'LastNews', 'last', 'последниеНовости']) 
        def repeat_all_messages(message): 
            lastNews.last()
            bot.send_message(message.chat.id, lastNews.finish[0], parse_mode='HTML', disable_web_page_preview = True)
# ______________________________________________________________________________________________________________________________
        # реакция на команду /numberofnews
        # В ответ посылаем просто строку с объяснением, как работает команда
        @bot.message_handler(commands=['numberofnews'])
        def repeat(message): 
            bot.send_message(message.chat.id, "Чтобы я прислал вам текст новости из списка новостей отправте мне сообщение в таком формате: /1, /14") #посылаем в ответ ссылку 2 из массива ссылок в файле парс. 
# ______________________________________________________________________________________________________________________________
        # реакция на команду /start
        # В ответ посылаем просто строку приветствие и краткую справку по командам
        @bot.message_handler(commands=['start']) 
        def repeat_all_messages(message): 
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на newsvl.ru", url="http://www.newsvl.ru/")
            keyboard.add(url_button)
            f = open('allUsers.txt', 'a')
            f.write(str(message.chat.id) + '\n')
            f.close()
            bot.send_message(message.chat.id, "Привет, я неофициальный бот сайта newsvl.ru. \nЯ умею отправлять список новостей по команде /news \nПо команде /hot я отправляю 3 самые горячие новости. \nПо команде /last я отправлю список 6 последних новостей \nТак же я умею отправлять текст новости из списка /news по команде /1 .. /20", parse_mode='HTML', disable_web_page_preview = True, reply_markup=keyboard)
# ______________________________________________________________________________________________________________________________
        # реакция на команду /help
        # В ответ посылаем просто строку приветствие и краткую справку по командам
        @bot.message_handler(commands=['help']) 
        def repeat_all_messages(message): 
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на newsvl.ru", url="http://www.newsvl.ru/")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Привет, я неофициальный бот сайта newsvl.ru. \nЯ умею отправлять список новостей по команде /news \nПо команде /hot я отправляю 3 самые горячие новости. \nПо команде /last я отправлю список 6 последних новостей \nТак же я умею отправлять текст новости из списка /news по команде /1 .. /20", parse_mode='HTML', disable_web_page_preview = True, reply_markup=keyboard)
# ______________________________________________________________________________________________________________________________# ______________________________________________________________________________________________________________________________
        # отправляем спам
        # в файле users.txt лежит список пользователей, которые подписались на рассылку
        # сначала считываем файл в spamUsers. Потом пытаемся удалить оттуда id пользователя, который написал.
        # если получается удалить пользователя, то просто удаляем пользователя из spamUsers
        # если удаление кидает ValueError, то добавляем пользователя в spamUsers
        # после удаления/добавления стираем файл users.txt и записываем туда id пользователей из spamUsers
        @bot.message_handler(commands=['spam'])
        def repeat(message): 
            global spamUsers
            spamUsers = []
            f = open('users.txt', 'r')
            for line in f:
                spamUsers.append(line.replace("\n",""))
            f.close()
            try:
                spamUsers.pop(spamUsers.index(str(message.chat.id)))
                bot.send_message(message.chat.id, "Вы успешно отписались от рассылки")
            except ValueError:
                print('spamUsers в except: ', spamUsers)
                spamUsers.append(str(message.chat.id))
                bot.send_message(message.chat.id, "Вы успешно подписались на рассылку")
            f = open('users.txt', 'w')
            for element in spamUsers:
                f.write(str(element) + '\n')
            f.close()
# ______________________________________________________________________________________________________________________________
        # добавление клавиатуры
        markup = types.ReplyKeyboardMarkup()
        markup.row('/news', '/hot', '/last')
        markup.row('/1', '/2', '/3')

        @bot.message_handler(commands=['keyboard'])
        def repeat(message):  
            bot.send_message(message.chat.id, "Клавиатура добавлена", reply_markup=markup)
# ______________________________________________________________________________________________________________________________
        # обрабатываем команды /1 ... /20
        # в ответ на каждую команду посылаем номер линка, чтобы в ответ функция в test.py вернула текст новости
        if setNews == 0: 
             @bot.message_handler(commands=['1'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(0), disable_web_page_preview = True) #посылаем в ответ ссылку 2 из массива ссылок в файле парс. 
             @bot.message_handler(commands=['2'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(1), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['3'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(2), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['4'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(3), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['5'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(4), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['6'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(5), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['7'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(6), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['8'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(7), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['9'])
             def repeat(message):
                pars.update()
                bot.send_message(message.chat.id, test.funcText(8), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['10'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(9), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['11'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(10), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['12'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(11), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['13'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(12), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['14'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(13), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['15'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(14), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['16'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(15), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['17'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(16), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['18'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(17), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['19'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(18), disable_web_page_preview = True) #посылаем в ответ 
             @bot.message_handler(commands=['20'])
             def repeat(message): 
                pars.update()
                bot.send_message(message.chat.id, test.funcText(19), disable_web_page_preview = True) #посылаем в ответ 
        sleep(sleep_time)
        if __name__ == '__main__': #запускам бота
            bot.polling(none_stop=True)
# ______________________________________________________________________________________________________________________________

class B:
    def __call__(self, count=1, sleep_time=0.5):
        sleep(sleep_time)
        global number 
        global dictionary 
        cancel = []
# ______________________________________________________________________________________________________________________________
        # функция работает каждый час — ходит в news.vl.ru/rss и парсит новости
        # просто добавляет ссылки в listLink — ссылки уникальные
        def everyHour():
            print("work everyHour")
            global listLink
            s = pars.update()
            for element in s:
                try:
                    listLink.index(str(element)) # если ссылка уже есть в списке, то ничего не делаем
                except ValueError:
                    listLink.append(element) # если try кидает ValueError, значит ссылки нет в списке — добавляем ее
            return
# ______________________________________________________________________________________________________________________________
        # функция работает каждый день (раз в 24 часа)
        # отправляет рассылку пользователям
        # сначала пробегаем по всем ссылкам в listLink и добавляем их в number[1]
        # потом в number[0] добавляем колличество комментариев (0 если их нет)
        # индекс по х ссылки и ее комментария совпадает
        # потом сортируем комментарии по возрастанию 
        # 10 самых комментируемых новостей кидаем пользователям
        def everyDay():
            bot = telebot.TeleBot(config.token) #создаем бота 
            global cancel
            global getSpam
            global dictionary
            global number 
            global listLink
            dictionary = {}
            link = []
            number = [],[]

            print("work everyDay")
            print('everyDay listLink: ', listLink)

            log = open('log.txt', 'w')
            for element in listLink:
                log.write(str(element) + '\n')
            log.close()

            for element in listLink: # для каждой ссылки нужно найти колличество комментариев
                soup = BeautifulSoup(urlopen(element.replace("\n","").replace("\t","").replace("\t","")), "lxml")
                number[1].append(element.replace("\n","").replace("\t","").replace("\t",""))
                try:
                    if soup.find("a", class_="story__info-comments-count") != None: # better: if item is not None
                        data = soup.find("a", class_="story__info-comments-count")
                        for contents in data:
                            number[0].append(contents)
                    else:        
                        raise TypeError 
                except TypeError:
                    number[0].append('0') # если try вернул TypeError, значит блока на странице нет — просто ставим 0 в разделе комментарии
            i = 0
            for element in number[0]: #создаем словарь
                dictionary[int(number[0][i])] = number[1][i]
                i += 1

            l = dictionary.keys() # получаем ключи
            l = list(l) # превращаем его в обычный список
            l.sort() # сортируем список
            l.reverse() # разворачиваем, чтобы список шел по возрастанию
            f = 0 
            cancel = [] # сбрасываем прошлые 10 самых комментируемых новостей
            for i in l: # вывод элементов словаря (ключ - значение) по алфавиту
                if f < 10:
                    cancel.append(dictionary[i])
                f += 1
            global spamId
            spamId = []
            goSpam = 'Самые комментируем новости за день: \n'
            count = 1
            for element in cancel: # для каждой ссылки из списка 10 находим ее тайтл и формируем гиперссылку
                doc = element
                soup = BeautifulSoup(urlopen(doc), "lxml")
                for wrapper in soup.find_all("h1", class_="story__title"): 
                    goSpam = goSpam + (str(count) + ") " +  '<a href="' + element + '">' + wrapper.text + '</a>' + '\n')
                    count += 1
            f = open('users.txt', 'r')
            for line in f: 
                spamId.append(line.replace("\n","")) # считываем список пользователей, которые подписались на рассылку
            f.close()
            for element in spamId: 
                bot.send_message(element, goSpam, parse_mode='HTML', disable_web_page_preview = True) # отправляем рассылку
            cancel = []
            listLink = [] # очищаем лист ссылок, чтобы следующие 24 часа формировался новый лист ссылок
            return
# ______________________________________________________________________________________________________________________________
        # код внизу запускает функции с различным интервалом 
        scheduler = BlockingScheduler()
        scheduler.add_job(everyHour, 'interval', hours=1)
        scheduler.add_job(everyDay, 'interval', hours=24)
        scheduler.start()
# ______________________________________________________________________________________________________________________________

if __name__ == '__main__':
    a = A()
    b = B()

    p1 = Process(target=a, kwargs={'sleep_time': 0.7})
    p2 = Process(target=b, args=(12,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()