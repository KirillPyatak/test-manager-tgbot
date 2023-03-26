import telebot

TOKEN = '5877590294:AAHP1lANVCByyY7HGXwvCEoXA3DH6YowYRg'
CHAT_ID = '-100691258066'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я твой помощник на этом сайте.')

@bot.message_handler(content_types=['text'])
def send_message(message):
    bot.send_message(CHAT_ID, message.text)

bot.polling(none_stop=True)