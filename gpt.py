def gpt(ask):  
    import requests
    url = "https://reverse.mubi.tech/v1/chat/completions"


    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "user", "content": ask}
        ]
    }

    response = requests.post(url, json=data)
    content = response.json().get("choices")[0].get("message").get("content")

    return(content)
import telebot

# Создаем экземпляр бота с вашим токеном
bot = telebot.TeleBot("6854145735:AAFlvvGdn1WuLBQKJpmZhV9RlKvEjyhUuII")

# Обрабатываем команды /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Спроси что-нибуть?")

# Обрабатываем обычные сообщения (эхо)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, gpt(message.text))

# Запускаем бота
bot.polling()
