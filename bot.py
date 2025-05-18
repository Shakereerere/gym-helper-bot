
import os
import telebot

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет! Я помогу тебе с выбором упражнений для зала.
"
                     "Напиши свою цель (например: масса, сушка, выносливость), максимальный вес и сколько подходов ты обычно делаешь.")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    chat_id = message.chat.id
    text = message.text.lower()

    if "спина" in text:
        reply = "Для спины подойдёт: подтягивания, тяга штанги в наклоне, гиперэкстензия."
    elif "грудь" in text:
        reply = "Для груди: жим лёжа, разводка гантелей, отжимания на брусьях."
    elif "ноги" in text:
        reply = "Для ног: приседания, выпады, жим ногами."
    elif "руки" in text or "бицепс" in text or "трицепс" in text:
        reply = "Для рук: подъём штанги на бицепс, французский жим, отжимания узким хватом."
    elif "плечи" in text:
        reply = "Для плеч: жим штанги над головой, махи гантелями, армейский жим."
    else:
        reply = "Напиши, какую часть тела хочешь потренировать: спина, грудь, ноги, руки, плечи."

    bot.send_message(chat_id, reply)

bot.polling()
