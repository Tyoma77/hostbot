import telebot
from telebot import apihelper

apihelper.proxy = {
    'http': 'socks5://127.0.0.1:9150',
    'https': 'socks5://127.0.0.1:9150'
}

bot = telebot.TeleBot('711272556:AAEXxkMl2YEMWpCc49nKmixgqEBTaHwPIAc')

CHANNEL_NAME = "-1001383299074"


@bot.message_handler(content_types=["text", "photo", "sticker"])
def repeat_messages(message):
    if message.content_type == 'text':
        bot.send_message(CHANNEL_NAME, message.text)
    elif message.content_type == 'sticker':
        bot.send_sticker(CHANNEL_NAME, message.sticker.file_id)
    else:
        bot.send_photo(CHANNEL_NAME, message.photo[len(message.photo) - 1].file_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
