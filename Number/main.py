# region API KEY
import telebot
from telebot import types
import time
import random


bot = telebot.TeleBot('5791614763:AAH2G2i8tccHGsw9PvVuwD-EdNKroYy_2Hk')
# real 5791614763:AAH2G2i8tccHGsw9PvVuwD-EdNKroYy_2Hk
# test 5734914555:AAEPdNUsCpv4n49jie8C9P7TojK_McPkCIU
# endregion API KEY

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️
Alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
GOOD_ANSWERS = (f'Поздравляю, ответ верный!\nВернуться в меню тренажера 👉 /game', f'Ответ верный!\nВернуться в меню тренажера 👉 /game', f'Отлично! Двигаемся дальше ☺\nВернуться в меню тренажера 👉 /game', f'У тебя получилось! Молодец!\nВернуться в меню тренажера 👉 /game')
BAD_ANSWERS = (f'Ответ неверный😭 Попробуй ещё раз!', 'Ответ неверный. Получить еще один пример\nВернуться в меню тренажера 👉 /game', "По-моему, Вы ошиблись.", "Мне кажется, это неправильно🤔")

@bot.callback_query_handler(func=lambda call: True)
def step(call):

    if call.data == 'lvl_1':
        M = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
        n = random.choice(M)
        a = random.randint(20, 1000)
        bot.send_message(call.message.chat.id, f'*Отправляю пример:*\nПереведите *{a}* из *10-ной* в *{n}-ную* систему счисления'
                                               f'\n\nОтвет введите в виде целочисленного, *без указания на систему счисления*.', parse_mode='Markdown')

        M = []
        while a > 0:
            M.append(str(a % n))
            a //= n
        M.reverse()
        r = ''.join(M)


        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = message.text

            if x == r:
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton('Получить еще один пример', callback_data='lvl_1')
                markup.add(btn1)
                bot.send_message(call.message.chat.id, random.choice(GOOD_ANSWERS), reply_markup=markup)
            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton('Повторить попытку с новым примером', callback_data='lvl_1')
                markup.add(btn1)
                bot.send_message(call.message.chat.id, random.choice(BAD_ANSWERS), reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'lvl_2':
        M = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
        letters = ''
        n = random.choice(M)
        a = random.randint(2, 10)
        for _ in range (a):
            letters += random.choice(Alphabet[:n])
        bot.send_message(call.message.chat.id,
                         f'*Отправляю пример:*\nПереведите *{letters}* из *{n}-ной* в *10-ную* систему счисления'
                         f'\n\nОтвет введите в виде целочисленного, *без указания на систему счисления*.',
                         parse_mode='Markdown')

        r = int(letters, n)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = message.text

            if x == str(r):
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton('Получить еще один пример', callback_data='lvl_2')
                markup.add(btn1)
                bot.send_message(call.message.chat.id, random.choice(GOOD_ANSWERS))

            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton('Повторить попытку с новым примером', callback_data='lvl_2')
                markup.add(btn1)
                bot.send_message(call.message.chat.id, random.choice(BAD_ANSWERS),
                                 reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)


    elif call.data == 'lvl_3':
        pass


# region Команда GAME
@bot.message_handler(commands=['game'])
def game(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('Получить пример из 10-ной в n-ную', callback_data='lvl_1')
    btn2 = types.InlineKeyboardButton('Получить пример из n-ной в 10-ную', callback_data='lvl_2')
    btn3 = types.InlineKeyboardButton('Получить пример из k-ой в n-ную', callback_data='lvl_3')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, f'Добро пожаловать в нашу игру:\n*Тренажер счет систем счислений*', parse_mode='Markdown', reply_markup=markup)




# endregion Команда GAME

# region Команда CREATORS
@bot.message_handler(commands=['creators'])
def creators(message):
    bot.send_message(message.chat.id, f'Я Александра, а это мой Telegram Bot по системам счисления, который я разработала со своим репетитором Ильёй @ilandroxy.  '
                                      f'\n\nЯ ученица 8 класса и очень стремлюсь к новым знаниям. И в принципе хочу связать свою жизнь с IT-сферой. '
                                      f'В данный момент я обучаюсь на онлайн курсе "Код будущего" на направлении "Разработка на Pyton" в университете Синергия.  '
                                      f'А также с Ильёй мы делаем интересные проекты, не входящие в программу курса. Илья - профессиональный репетитор. '
                                      f'Он закончил СибГУТИ по специальности "Информатика и Вычеслительная техника". '
                                      f'На данный момент Илья проходит обучение в НГПУ, по направлению: _«Педагогическое образование для специалистов с высшим непедагогическим образованием»_.', parse_mode='Markdown')

# endregion Команда CREATORS

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


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)





