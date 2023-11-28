import telebot

bot = telebot.TeleBot('6607216259:AAFFo9XtZcRYu-iru9OuK9E34n3_pJtevTA')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! Я могу поддержать тебя небольшими напоминаниями!! \nПросто воспользуйся этими командами: \n /compliment - Узнай, кто ты на самом деле \n /support - Узнай, что ты можешь на самом деле \n /mainreminder - Что Вселенная скрывает от тебя?')


@bot.message_handler(commands=['compliment'])
def main(message):
    bot.send_message(message.chat.id, '*Ты лучший!!!* Даже Вселенная восхищена твоей красотой и силой!!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['support'])
def main(message):
    bot.send_message(message.chat.id, '*Ты* со всем справишься!!! Просто не опускай руки и иди вперёд!!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['mainreminder'])
def main(message):
    bot.send_message(message.chat.id,
                     'Вау! *Ты* ведь тот самый человек, который всего добьётся! Вселенная никогда не врёт. Будь счастлив, приятель!!!',
                     parse_mode='Markdown')


bot.infinity_polling()