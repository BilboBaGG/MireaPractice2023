from database.functions import ORM
from models.buttons import keyboard
from models.helpers import *
import telebot
import time

# Waiting for database
time.sleep(3)
db = ORM()
#db.CreateTable()
token = '5524674402:AAHc131tO94lxIsL5tCcQcj7fDUM6EyDtXc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['today'])
def today(message):
    group = db.GetStudent(str(message.chat.id)).group
    day, week = curent_day()
    text = create_output(group, day, week)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['my_group'])
def my_group(message):
    group = db.GetStudent(str(message.chat.id)).group
    bot.send_message(message.chat.id, "Your group is: " + group)

@bot.callback_query_handler(func=lambda call:True) # Buttons
def callback_query(call):
    
    db.UpdateStudentGroup(str(call.message.chat.id), call.data)
    bot.send_message(call.message.chat.id, "Group updated! Now it is :" + call.data)

@bot.message_handler(commands=['update_group'])
def update_group(message):
    bot.send_message(message.chat.id, "Select group:\n", reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    if not db.IsStudentExists(str(message.chat.id)):
        db.AddStudent(telegram_id_=str(message.chat.id), group_="")
        db.IsStudentExists(str(message.chat.id))
        bot.send_message(message.chat.id, "Hello, new user!\n\nYou should select your group to work with bot!" + str(message.chat.id), reply_markup=keyboard)
    else:   
        bot.send_message(message.chat.id, helpMenu)
        
if __name__ == "__main__":
    bot.infinity_polling()


