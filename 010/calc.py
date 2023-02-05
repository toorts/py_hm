from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import logging


bot = Bot(token='TOKEN')

updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='010/bot.log')
STATES = (0, 1)

logging.info('start bot')


def start(update, context):
    name = update.effective_chat.first_name
    context.bot.send_message(update.effective_chat.id, f"<b>Привет, {name}</b>!\nЭто - калькулятор рациональных чисел.\n"
                             "Введите выражение типа:\n<b>12 + 3*3 - 20/5</b>"
                             "\nИ дождитесь результата.", parse_mode='html')


def calc(update, context):
    example = update.message.text
    parse = example.replace(
        '*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ').split()
    while '*' in parse or '/' in parse:
        for i in range(1, len(parse) - 1):
            if parse[i] == '*':
                oper1 = float(parse.pop(i - 1))
                oper2 = float(parse.pop(i))
                parse[i-1] = oper1 * oper2
                break
            elif parse[i] == '/':
                oper1 = float(parse.pop(i - 1))
                oper2 = float(parse.pop(i))
                parse[i-1] = oper1 / oper2
                break
    while '+' in parse or '-' in parse:
        for i in range(1, len(parse) - 1):
            if parse[i] == '+':
                oper1 = float(parse.pop(i - 1))
                oper2 = float(parse.pop(i))
                parse[i-1] = oper1 + oper2
                break
            elif parse[i] == '-':
                oper1 = float(parse.pop(i - 1))
                oper2 = float(parse.pop(i))
                parse[i-1] = oper1 - oper2
                break
    context.bot.send_message(
        update.effective_chat.id, f"Результат: {''.join(str(x) for x in parse)}")
    menu(update, context)


def menu(update, context):
    context.bot.send_message(update.effective_chat.id, "Для выхода клинки сюда 👉 /bye")


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "До новых встреч)")
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
calc_handler = MessageHandler(Filters.text, calc)
menu_handler = MessageHandler(Filters.text, menu)
cancel_handler = CommandHandler('bye', cancel)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(calc_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(cancel_handler)

updater.start_polling()
updater.idle()