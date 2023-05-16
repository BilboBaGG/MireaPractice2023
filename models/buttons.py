from telebot import types

button1 = types.InlineKeyboardButton('BISO-01-22', callback_data='BISO-01-22')
button2 = types.InlineKeyboardButton('BISO-02-22', callback_data='BISO-02-22')
button3 = types.InlineKeyboardButton('BISO-03-22', callback_data='BISO-03-22')

keyboard = types.InlineKeyboardMarkup()
keyboard.add(button1)
keyboard.add(button2)
keyboard.add(button3)
