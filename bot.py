# -*- coding: utf-8 -*-
import config #импортирую файл конфиг из этой же папки
import pars #импортирую файл парс из этой же папки
import telebot #с помощью этой библиотеки строится бот
import test
import hotNews
import sendSpam
import pytz
import schedule
import time
from grab import Grab #импортируем граб для работы с парсингом
import re
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pars 

from apscheduler.schedulers.blocking import BlockingScheduler
from telebot import types
from datetime import datetime, date, time

bot = telebot.TeleBot(config.token) #создаем бота
# pars.update()
answer = pars.mainString #это то, что будем посылать в ответ
#lol = pars.stroka[1]
setNews = 0 #если посылали новости, то 1, если нет, то 0



@bot.message_handler(commands=['news', 'новости', 'Новости', 'НОВОСТИ']) #реакция на КОМАНДЫ 
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    pars.update()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на newsvl.ru", url="http://www.newsvl.ru/")
    keyboard.add(url_button)
    setNews = 1
    bot.send_message(message.chat.id, answer, parse_mode='HTML', disable_web_page_preview = True, reply_markup=keyboard) #посылаем в ответ 

@bot.message_handler(commands=['hotnews', 'HotNews', 'hot', 'горячиеНовости']) 
def repeat_all_messages(message): 
    hotNews.updateHot()
    bot.send_message(message.chat.id, hotNews.finish[0], parse_mode='HTML', disable_web_page_preview = True)

@bot.message_handler(commands=['numberofnews'])
def repeat(message): 
    bot.send_message(message.chat.id, "Чтобы я прислал вам текст новости из списка новостей отправте мне сообщение в таком формате: /1, /14") #посылаем в ответ ссылку 2 из массива ссылок в файле парс. 

@bot.message_handler(commands=['start', 'help']) 
def repeat_all_messages(message): 
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на newsvl.ru", url="http://www.newsvl.ru/")
    keyboard.add(url_button)
    try:
        sendSpam.listUsers.pop(sendSpam.listUsers.index(message.chat.id))
        sendSpam.listUsers.append(message.chat.id)
    except ValueError:
        sendSpam.listUsers.append(message.chat.id)
        f = open('users.txt', 'a')
        f.write(str(message.chat.id) + '\n')
        f.close()
    print(sendSpam.listUsers)
    bot.send_message(message.chat.id, "Привет, я неофициальный бот сайта newsvl.ru. \n Я умею отправлять список новостей по команде /news, по команде /hot я отправляю 3 самые горячие новости. \n Так же я умею отправлять текст новости из списка /news по команда /1 .. /20", parse_mode='HTML', disable_web_page_preview = True, reply_markup=keyboard)
    
# number = 0

# tzvl = pytz.timezone('Asia/Vladivostok')
# now = datetime.now(tzvl)

# if (now.hour == 23) and (now.minute == 4):  
#     def repeat_all_messages(message):
#         bot.send_message(sendSpam.listId.pop(0), hotNews.finish[0], parse_mode='HTML', disable_web_page_preview = True)


@bot.message_handler(commands=['spam'])
def repeat(message): 
    print(message.chat.id)
    try:
        sendSpam.listUsers.pop(sendSpam.listUsers.index(message.chat.id))
        bot.send_message(message.chat.id, "Вы успешно отписались от рассылки")
    except ValueError:
        sendSpam.addUser(message.chat.id)
        bot.send_message(message.chat.id, "Вы успешно подписались на рассылку")


markup = types.ReplyKeyboardMarkup()
markup.row('/news', '/hot')
markup.row('/1', '/2', '/3')

@bot.message_handler(commands=['keyboard'])
def repeat(message):  
    bot.send_message(message.chat.id, "Клавиатура добавлена", reply_markup=markup)


#обрабатываем команды 
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
    return

def everyDay():
    global cancel
    print("work everyDay")
    print(cancel)
    lol = str(cancel)
    for element in sendSpam.listUsers: 
        print('USER ID при отправке ', element)
        bot.send_message(element, lol, disable_web_page_preview = True)
    cancel = []
    return



# count:  [<a class="story__info-comments-count" data-notation="Количество комментариев" href="#comments">8</a>]

scheduler = BlockingScheduler()
scheduler.add_job(everyHour, 'interval', hours=1)
scheduler.add_job(everyDay, 'interval', hours=5)
scheduler.start()



if __name__ == '__main__': #запускам бота
      bot.polling(none_stop=True)