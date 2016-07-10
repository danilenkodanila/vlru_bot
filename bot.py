# -*- coding: utf-8 -*-
import config #импортирую файл конфиг из этой же папки
import pars #импортирую файл парс из этой же папки
import telebot #с помощью этой библиотеки строится бот

bot = telebot.TeleBot(config.token) #создаем бота
answer = pars.s #это то, что будем посылать в ответ

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, answer) #посылаем в ответ 

if __name__ == '__main__': #запускам бота
     bot.polling(none_stop=True)