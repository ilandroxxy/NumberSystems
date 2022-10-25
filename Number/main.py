# region API KEY
import telebot
from telebot import types
import time


bot = telebot.TeleBot('5791614763:AAH2G2i8tccHGsw9PvVuwD-EdNKroYy_2Hk')
# real 5791614763:AAH2G2i8tccHGsw9PvVuwD-EdNKroYy_2Hk
# test 5734914555:AAEPdNUsCpv4n49jie8C9P7TojK_McPkCIU
# endregion API KEY

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️
Alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# region команда HI
@bot.message_handler(commands=['hi'])
def hi(message):
    if message.chat.id == 1891281816:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Уведомлен ✅')
        markup.add(btn1)
        bot.send_message(1208542295, 'Привет, Саша. Я работаю над проектом!', reply_markup=markup)

    elif message.chat.id == 1208542295:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Уведомлен ✅')
        markup.add(btn1)
        bot.send_message(1891281816, 'Привет, Илья. Я работаю над проектом!', reply_markup=markup)
# endregion команда HI

# region Команда START
@bot.message_handler(commands=['start'])
def start(message):
    ID = message.chat.id
    bot.send_message(message.chat.id, f'Ваш user ID: `{ID}`', parse_mode='Markdown')

    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    message_text = f'Привет *{first_name}*! Как у тебя дела? Твоя фамилия _{last_name}_?\n\n' \
                   f'Чтобы найти автора, воспользуйтесь [ссылкой](https://t.me/ilandroxy).'


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Перевод из 10-ной в N-ную')
    btn2 = types.KeyboardButton('Перевод из N-ной в 10-ную')
    btn3 = types.KeyboardButton('Перевод из N-ной в K-тую')
    markup.add(btn1, btn2, btn3)


    bot.send_message(message.chat.id, message_text, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)
# endregion Команда START

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()


    # region Перевод из 10-ной в N-ную
    if get_message_bot == "Перевод из 10-ной в N-ную":
        bot.send_message(message.chat.id, 'Введите два числа через пробел:\n'
                                          '*[10-ное число] [n-ную систему счисления]*', parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            try:
                text_message = message.text
                M = [int(i) for i in text_message.split()]
                if len(M) == 2:
                    x = M[0]  # число которое будем переводить в систему счисления n
                    n = M[1]  # система счисления
                    RES = []
                    while x > 0:
                        RES.append(Alphabet[x % n])
                        x //= n
                    RES.reverse()
                    res_string = "".join(RES)

                    message_text = f"Перевели число {M[0]} *из 10-ной* в *{n}-ую систему*\n\nРезультат вычислений: *{res_string}* в {n}-ной системе счисления."
                    bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, "Введите два числа, через пробел!")
            except IndexError:
                bot.send_message(message.chat.id, "Введите два числа, через пробел!")
            except ZeroDivisionError:
                bot.send_message(message.chat.id, "На нуль делить нельзя, плюс нуль всегда является нулем!")
        bot.register_next_step_handler(message, message_input)
    # endregion Перевод из 10-ной в N-ную

    # region Перевод из N-ной в 10-ную
    elif get_message_bot == "Перевод из N-ной в 10-ную":
        bot.send_message(message.chat.id, 'Введите два числа через пробел:\n'
                                          '*[N-ное число] [n-ную систему счисления]*', parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            try:
                text_message = message.text
                M = [i for i in text_message.split()]
                if len(M) == 2:
                    x = M[0]  # число которое будем переводить в систему счисления n
                    n = int(M[1])  # система счисления

                    r = int(x, n)

                    message_text = f"Перевели число {M[0]} *из N-ной* в *{10}-ую систему*\n\nРезультат вычислений: *{r}* в {10}-ной системе счисления."
                    bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, "Введите два числа, через пробел!")
            except IndexError:
                bot.send_message(message.chat.id, "Введите два числа, через пробел!")
            except ZeroDivisionError:
                bot.send_message(message.chat.id, "На нуль делить нельзя, плюс нуль всегда является нулем!")

        bot.register_next_step_handler(message, message_input)
    # endregion Перевод из N-ной в 10-ную


    elif get_message_bot == "Перевод из N-ной в K-тую":
        bot.send_message(message.chat.id, 'Пока что разрабатываем!')
    # Кнопки для перевода в системы -------------------------------------------------------------------------------------

    # Кнопка Уведомлен --------------------------------------------------------------------------------------------------
    elif get_message_bot == "Уведомлен ✅":
        if message.chat.id == 1891281816:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton('Перевод из 10-ной в N-ную')
            btn2 = types.KeyboardButton('Перевод из N-ной в 10-ную')
            btn3 = types.KeyboardButton('Перевод из N-ной в K-тую')
            markup.add(btn1, btn2, btn3)
            bot.send_dice(1891281816, reply_markup=markup)
            bot.send_message(1208542295, 'Ваш коллега, принял уведомление!')

        elif message.chat.id == 1208542295:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton('Перевод из 10-ной в N-ную')
            btn2 = types.KeyboardButton('Перевод из N-ной в 10-ную')
            btn3 = types.KeyboardButton('Перевод из N-ной в K-тую')
            markup.add(btn1, btn2, btn3)
            bot.send_dice(1208542295, reply_markup=markup)
            bot.send_message(1891281816, 'Ваш коллега, принял уведомление!')
    # Кнопка Уведомлен --------------------------------------------------------------------------------------------------




'''
@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    if call.data == 'КлючСобытия':
        pass

@bot.message_handler(commands=['voice'])
def voice(message):

    @bot.message_handler(content_types=['text'])
    def message_input(message):
        text_message = message.text
        bot.send_message(message.chat.id, text_message)

    bot.register_next_step_handler(message, message_input)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == "Репетитор":
        pass
'''

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)





