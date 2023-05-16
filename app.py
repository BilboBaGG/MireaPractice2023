from database.functions import ORM
from models.buttons import keyboard
from models.help import helpMenu

import telebot
import logging
import time


time.sleep(3)

db = ORM()
print("--> Seccessfully connected to database")

db.CreateTable()

token = '5524674402:AAHc131tO94lxIsL5tCcQcj7fDUM6EyDtXc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['my_group'])
def my_group(message):
    group = db.GetStudent(str(message.chat.id)).group
    bot.send_message(message.chat.id, "Your group is: " + group)


def process_group_selection(message):
    db.UpdateStudentGroup(str(message.chat.id), message.text)
    bot.send_message(message.chat.id, "Group updated")

@bot.message_handler(commands=['update_group'])
def update_group(message):
    buttonMessage = bot.send_message(message.chat.id, "Select group:\n", reply_markup=keyboard)
    bot.register_next_step_handler(buttonMessage, process_group_selection)

@bot.message_handler(commands=['start'])
def start(message):
    if db.IsStudentExists(str(message.id)):
        db.AddStudent(message.chat.id, "", True)
        buttonMessage = bot.send_message(message.chat.id, "Hello, new user!\n\nYou shold print your group to work with bot!", reply_markup=keyboard)
        bot.register_next_step_handler(buttonMessage, process_group_selection)
    else:   
        bot.send_message(message.chat.id, helpMenu)

    #bot.send_message(message.chat.id, "Hello, new user!\n\nYou shold print your group to work with bot!", reply_markup=keyboard)
    
        
if __name__ == "__main__":
    print("--> Bot secsessfully started")
    logging.info("hello")
    bot.infinity_polling()

