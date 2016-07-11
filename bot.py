# -*- coding: utf-8 -*-
import config #импортирую файл конфиг из этой же папки
import pars #импортирую файл парс из этой же папки
import telebot #с помощью этой библиотеки строится бот

bot = telebot.TeleBot(config.token) #создаем бота
answer = pars.mainString #это то, что будем посылать в ответ
setNews = 0 #если посылали новости, то 1, если нет, то 0

@bot.message_handler(commands=['news', 'новости', 'Новости', 'НОВОСТИ']) #реакция на КОМАНДЫ 
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, answer) #посылаем в ответ 
    setNews = 1


#Ты можешь спросить, если посмотришь на код ниже, почему мы берем ссылки на +1?????!??!?!. Так ответ таков:
#Первая ссылка, которая парсится — просто ссылка на яндекс новости, поэтому мы ее пропускаем )))))
#Да, можно было сделать, как у тебя при парсинге заголовков — ввести иф и счетчик, но какая разница? 
#По объему памяти выходит одинаково ( наверное)))) )

#обрабатываем команды 
#пока не уверен, но вроде то, что внизу ДАЖЕ не говнокод, а норм обработчик команд
if setNews == 0: #ВНИМАНИЕ, УСЛОВИЕ setNews == 1 ПОЧЕМУ-ТО НЕ РАБОТАЕТ (((((
     @bot.message_handler(commands=['1'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[2]) #посылаем в ответ ссылку 2 из массива ссылок в файле парс. 
     @bot.message_handler(commands=['2'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[3]) #посылаем в ответ 
     @bot.message_handler(commands=['3'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[4]) #посылаем в ответ 
     @bot.message_handler(commands=['4'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[5]) #посылаем в ответ 
     @bot.message_handler(commands=['5'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[6]) #посылаем в ответ 
     @bot.message_handler(commands=['6'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[7]) #посылаем в ответ 
     @bot.message_handler(commands=['7'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[8]) #посылаем в ответ 
     @bot.message_handler(commands=['8'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[9]) #посылаем в ответ 
     @bot.message_handler(commands=['9'])
     def repeat(message):
        bot.send_message(message.chat.id, pars.s[10]) #посылаем в ответ 
     @bot.message_handler(commands=['10'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[11]) #посылаем в ответ 
     @bot.message_handler(commands=['11'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[12]) #посылаем в ответ 
     @bot.message_handler(commands=['12'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[13]) #посылаем в ответ 
     @bot.message_handler(commands=['13'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[14]) #посылаем в ответ 
     @bot.message_handler(commands=['14'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[15]) #посылаем в ответ 
     @bot.message_handler(commands=['15'])
     def repeat(message): 
        bot.send_message(message.chat.id, pars.s[16]) #посылаем в ответ 

    
if __name__ == '__main__': #запускам бота
      bot.polling(none_stop=True)