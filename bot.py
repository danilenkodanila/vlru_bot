# -*- coding: utf-8 -*-
import config #импортирую файл конфиг из этой же папки
import pars #импортирую файл парс из этой же папки
import telebot #с помощью этой библиотеки строится бот
import test
import hotNews
#import parsLink

bot = telebot.TeleBot(config.token) #создаем бота
answer = pars.mainString #это то, что будем посылать в ответ
#lol = pars.stroka[1]
setNews = 0 #если посылали новости, то 1, если нет, то 0

@bot.message_handler(commands=['news', 'новости', 'Новости', 'НОВОСТИ']) #реакция на КОМАНДЫ 
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, answer, parse_mode='HTML') #посылаем в ответ 
    setNews = 1

@bot.message_handler(commands=['hotnews', 'HotNews', 'hot']) 
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, hotNews.finish[0], parse_mode='HTML' )


#обрабатываем команды 
#пока не уверен, но вроде то, что внизу ДАЖЕ не говнокод, а норм обработчик команд
if setNews == 0: #ВНИМАНИЕ, УСЛОВИЕ setNews == 1 ПОЧЕМУ-ТО НЕ РАБОТАЕТ (((((
     @bot.message_handler(commands=['1'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[1]) #посылаем в ответ ссылку 2 из массива ссылок в файле парс. 
     @bot.message_handler(commands=['2'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[2]) #посылаем в ответ 
     @bot.message_handler(commands=['3'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[3]) #посылаем в ответ 
     @bot.message_handler(commands=['4'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[4]) #посылаем в ответ 
     @bot.message_handler(commands=['5'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[5]) #посылаем в ответ 
     @bot.message_handler(commands=['6'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[6]) #посылаем в ответ 
     @bot.message_handler(commands=['7'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[7]) #посылаем в ответ 
     @bot.message_handler(commands=['8'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[8]) #посылаем в ответ 
     @bot.message_handler(commands=['9'])
     def repeat(message):
        bot.send_message(message.chat.id, pars.s[9]) #посылаем в ответ 
     @bot.message_handler(commands=['10'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[10]) #посылаем в ответ 
     @bot.message_handler(commands=['11'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[11]) #посылаем в ответ 
     @bot.message_handler(commands=['12'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[12]) #посылаем в ответ 
     @bot.message_handler(commands=['13'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[13]) #посылаем в ответ 
     @bot.message_handler(commands=['14'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[14]) #посылаем в ответ 
     @bot.message_handler(commands=['15'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[15]) #посылаем в ответ 
     @bot.message_handler(commands=['16'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[16]) #посылаем в ответ 
     @bot.message_handler(commands=['17'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[17]) #посылаем в ответ 
     @bot.message_handler(commands=['18'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[18]) #посылаем в ответ 
     @bot.message_handler(commands=['19'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[19]) #посылаем в ответ 
     @bot.message_handler(commands=['20'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[20]) #посылаем в ответ 



     @bot.message_handler(commands=['1text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(1)) #посылаем в ответ ссылку 2 из массива ссылок в файле парс. 
     @bot.message_handler(commands=['2text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(2)) #посылаем в ответ 
     @bot.message_handler(commands=['3text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(3)) #посылаем в ответ 
     @bot.message_handler(commands=['4text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(4)) #посылаем в ответ 
     @bot.message_handler(commands=['5text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(5)) #посылаем в ответ 
     @bot.message_handler(commands=['6text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(6)) #посылаем в ответ 
     @bot.message_handler(commands=['7text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(7)) #посылаем в ответ 
     @bot.message_handler(commands=['8text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(8)) #посылаем в ответ 
     @bot.message_handler(commands=['9text'])
     def repeat(message):
        bot.send_message(message.chat.id, test.funcText(9)) #посылаем в ответ 
     @bot.message_handler(commands=['10text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(10)) #посылаем в ответ 
     @bot.message_handler(commands=['11text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(11)) #посылаем в ответ 
     @bot.message_handler(commands=['12text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(12)) #посылаем в ответ 
     @bot.message_handler(commands=['13text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(13)) #посылаем в ответ 
     @bot.message_handler(commands=['14text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(14)) #посылаем в ответ 
     @bot.message_handler(commands=['15text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(15)) #посылаем в ответ 
     @bot.message_handler(commands=['16text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(16)) #посылаем в ответ 
     @bot.message_handler(commands=['17text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(17)) #посылаем в ответ 
     @bot.message_handler(commands=['18text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(18)) #посылаем в ответ 
     @bot.message_handler(commands=['19text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(19)) #посылаем в ответ 
     @bot.message_handler(commands=['20text'])
     def repeat(message): 
        bot.send_message(message.chat.id, test.funcText(20)) #посылаем в ответ 
    
if __name__ == '__main__': #запускам бота
      bot.polling(none_stop=True)