import telebot

bot=telebot.TeleBot('6145733943:AAGMhy0O5bxlluF4tsC-9ktvTODiQpRsxUA')

@bot.message_handler(commands=['start'])

    
def start_message(message):
    bot.send_photo(message.chat.id, open('img/izy_i.jpg', 'rb'))
    bot.send_message(message.chat.id, '<b>Hello!!!</b>', parse_mode='html')
    

bot.polling(none_stop=True)