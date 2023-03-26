from flask import Flask, render_template, request
import telebot
app = Flask(__name__)
TOKEN = '5877590294:AAHP1lANVCByyY7HGXwvCEoXA3DH6YowYRg'
CHAT_ID = '-1001923842541'

bot = telebot.TeleBot(TOKEN)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=["POST"])
def send_message():
    # chat_id = request.form.get("chat_id")
    text = request.form.get("text")
    if text.lower() == 'да':
        bot.send_message(CHAT_ID,text='Lox')
    else:
        bot.send_message(CHAT_ID, text)
    return "Message sent"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я чат-менеджер на сайте. Как я могу тебе помочь?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    app.run()