import telebot
from telebot import types


bot = telebot.TeleBot('5791614763:AAH2G2i8tccHGsw9PvVuwD-EdNKroYy_2Hk')
# real 5791614763:AAH2G2i8tccHGsw9PvVuwD-EdNKroYy_2Hk
# test 5734914555:AAEPdNUsCpv4n49jie8C9P7TojK_McPkCIU


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


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == "Перевод из 10-ной в N-ную":
        bot.send_message(message.chat.id, 'Введите число и систему в определенном порядке:\n'
                                          '*[10-ное число] [В какую систему счисления]*', parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            try:
                text_message = message.text
                M = [int(i) for i in text_message.split()]
                x = M[0]
                n = M[1]
                print(x, n)
                N = []
                while x > 0:
                    N.append(str(x % n))
                    x //= n
                N.reverse()
                print(N)
                res_string = "".join(N)
                print(res_string)

                message_text = f"Перевели число {M[0]} из 10-ной в {n}-ую систему\nРезультат вычисление: {res_string}_{n}"
                bot.send_message(message.chat.id, message_text)
            except IndexError:
                bot.send_message(message.chat.id, "Введите два числа, через пробел!")
            except ZeroDivisionError:
                bot.send_message(message.chat.id, "На нуль делить нельзя, плюс нуль всегда является нулем!")
        bot.register_next_step_handler(message, message_input)

    if get_message_bot == "Перевод из N-ной в 10-ную":
        bot.send_message(message.chat.id, 'Пока что разрабатываем!')

    if get_message_bot == "Перевод из N-ной в K-тую":
        bot.send_message(message.chat.id, 'Пока что разрабатываем!')




'''
@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    if call.data == 'КлючСобытия':
        pass

@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Репетитор')
    markup1.add(btn1)
    send_mess = f'👋 Доброго времени суток, *{message.from_user.first_name}*!'
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup1)

    markup2 = types.InlineKeyboardMarkup(row_width=1)
    markup2.add(types.InlineKeyboardButton("Кнопка", callback_data="КлючСобытия"))
    pic_1 = open("hello.jpeg", 'rb')
    bot.send_photo(message.chat.id, pic_1, reply_markup=markup2)

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

bot.polling(none_stop=True)





