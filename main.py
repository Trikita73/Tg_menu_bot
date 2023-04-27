import telebot
from telebot import types

bot=telebot.TeleBot('token')

@bot.message_handler(commands=['start'])

    
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Ганстер', callback_data='delete'))
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://trikita73.github.io/High-Wave/'))
    

    bot.send_photo(message.chat.id, open('img/izy_i_2.jpg', 'rb'))
    bot.send_message(message.chat.id, '<b>Hello!!!</b><b>Hello!!!</b><b>Hello!!!</b>', parse_mode='html', reply_markup=markup)



bot.polling(none_stop=True)