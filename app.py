from database.functions import ORM
import telebot
import time

time.sleep(3)

print("--> Seccessfully connected to database")

db = ORM()

token = '5524674402:AAHc131tO94lxIsL5tCcQcj7fDUM6EyDtXc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def tomorrow_lessons(message):
    output = "Hello world"
    bot.send_message(message.chat.id, output)
    print("Good connection from " + str(message.chat.id))
        
if __name__ == "__main__":
    print("--> Bot secsessfully started")
    bot.infinity_polling()

