from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters

bot = Bot(token='TOKEN')
updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher


def finder(update, context):
    text = update.message.text
    answer = ' '.join([x for x in text.split() if 'абв' not in x])
    context.bot.send_message(update.effective_chat.id, answer)


find_handler = MessageHandler(Filters.text, finder)

dispatcher.add_handler(find_handler)

updater.start_polling()
updater.idle()