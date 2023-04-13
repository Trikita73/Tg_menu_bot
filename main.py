import telebot

bot=telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '<b>Hello!!!</b>', parse_mode='html')


bot.polling(none_stop=True)