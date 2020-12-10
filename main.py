import telebot

api = '1491500064:AAEfEeK7DrTcsTXA4Yty1t-ykNawcJHD6uo'
bot = telebot.TeleBot(token=api, parse_mode=None)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'hai!')


@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    bot.reply_to(message, 'Maaf aku gak bisa bantu!')


bot.polling()
