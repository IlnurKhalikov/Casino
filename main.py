@bot.message_handler(commands=['Casino', 'casino'])
def casino(message):
    splited = message.text.split()
    if len(splited) == 1:
        bot.send_message(message.chat.id, 'Введите /casino (число или цвет(ч или к)) (сумма игры)')
    elif len(splited) == 3 and splited[2].isdigit():
        try:
            if int(splited[1]) == random.randint(0, 36):
                bot.send_message(message.chat.id, f'Вы выиграли! Ваш выигрыш {int(splited[2]) * 35} MRK')
                Users.pay(message.chat.id, int(splited[2]) * 35)
            else:
                bot.send_message(message.chat.id, 'Вы проиграли( Повезёт в другой раз')
        except:
            number = random.randint(1, 36)
            if (number%2 == 0 and splited[1] == 'ч') or (number%2 == 1 and splited[1] == 'к'):
                bot.send_message(message.chat.id, f'Вы выиграли! Ваш выигрыш {int(splited[2]) * 2} MRK')
                Users.pay(message.chat.id, int(splited[2]) * 2)
            else: bot.send_message(message.chat.id, 'Вы проиграли( Повезёт в другой раз')
        Users.withdraw(message.chat.id, int(splited[2]))
    else:
        bot.send_message(message.chat.id, 'Введите /casino (число или цвет) (сумма игры)')
