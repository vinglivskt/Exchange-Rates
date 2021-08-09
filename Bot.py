import json

import telebot
import update as update

import config
from telebot import types
# from Exchange_Rates import get_currency_price
from Exchange_Rates import sum
from Exchange_Rates import toFixed
from Exchange_Rates import get_currency_price

url_us = "http://www.floatrates.com/daily/usd.json"
url_eu = 'http://www.floatrates.com/daily/eur.json'
url_ua = 'http://www.floatrates.com/daily/uah.json'
url_ru = 'http://www.floatrates.com/daily/rub.json'
# Заголовки для передачи вместе с URL
bot = telebot.TeleBot(config.TOKEN)


def oops():
    return "Ой, вы походу ошиблись при вводе, попрошу вводить числа 😊\n\nПопробуйте еще раз выбрать нужную кнопку и указать корректную сумму для перевода"


def start_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Актуальный курс🤑")
    item2 = types.KeyboardButton("Перевод валют💱")
    markup.add(item1, item2)
    return markup


def learn_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Узнать курс💵")
    item2 = types.KeyboardButton("Узнать курс🇺🇦")
    item3 = types.KeyboardButton("Узнать курс💶")
    item4 = types.KeyboardButton("More")
    Back = types.KeyboardButton("Назад 🚪")
    markup.add(item1, item2, item3, item4, Back)
    return markup


def transfer_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    us_ru = types.KeyboardButton("US ➡ RU")
    us_ua = types.KeyboardButton("US ➡ UA")
    us_eu = types.KeyboardButton("US ➡ EU")

    ru_us = types.KeyboardButton("RU ➡ US")
    ru_ua = types.KeyboardButton("RU ➡ UA")
    ru_eu = types.KeyboardButton("RU ➡ EU")

    ua_us = types.KeyboardButton("UA ➡ US")
    ua_ru = types.KeyboardButton("UA ➡ RU")
    ua_eu = types.KeyboardButton("UA ➡ EU")

    eu_us = types.KeyboardButton("EU ➡ US")
    eu_ru = types.KeyboardButton("EU ➡ RU")
    eu_ua = types.KeyboardButton("EU ➡ UA")
    Back = types.KeyboardButton("Назад 🚪")
    markup.add(us_ru, us_ua, us_eu, ru_us, ru_ua, ru_eu, ua_ru, ua_us, ua_eu, eu_us, eu_ru, eu_ua, Back)
    return markup


@bot.message_handler(commands=['insta'])
def Instagram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com/vinglivskt/?r=nametag"))
    sti = open('static/Putin6.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже для перехода в мой Instagram", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['start'])
def Welcome(message):
    sti = open('static/Putin.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, "
                     "бот, который ""умеет отслеживать актуальный курс валют. "
                     "\nДоступные команды:\n""/start - запуск бота\n"
                     "/vk - моя страница ВКонтакте\n"
                     "/insta - моя страница в Instagram".format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=start_menu())


@bot.message_handler(commands=['vk'])
def vk(message):
    markup = types.InlineKeyboardMarkup()
    sti = open('static/Putin5.png', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup.add(types.InlineKeyboardButton("Посетить мою страницу в вк", url="https://vk.com/vinglivskt"))
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже для перехода", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['oll'])
def oll_transfer(message):
    sti = open('static/Putin7.png', 'rb')
    bot.send_sticker(message.chat.id, sti)
    send = bot.send_message(message.chat.id,
                            "Введите валюты заглавными буквами, следующим образом: ВАЛЮТА_ВАЛЮТА\nПример: USD_UAH")
    bot.register_next_step_handler(send, oll)


@bot.message_handler(content_types=['text'])
def Menu_Change(message):
    if message.chat.type == 'private':

        if message.text == 'Актуальный курс🤑':
            sti = open('static/Putin2.jpg', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id,
                             "В данной категории вам предоставленная быстрая информация о курсе валют в рублях,\n\n Так же возможность перевода\n любой валюты 1 к 1".format(
                                 message.from_user, bot.get_me()), parse_mode='html', reply_markup=learn_menu())
        elif message.text == 'Узнать курс💵':
            bot.send_message(message.chat.id, toFixed(float(get_currency_price('USD_RUB')), 2))
        elif message.text == 'Узнать курс🇺🇦':
            bot.send_message(message.chat.id, toFixed(float(get_currency_price('UAH_RUB')), 2))
        elif message.text == 'Узнать курс💶':
            bot.send_message(message.chat.id, toFixed(float(get_currency_price('EUR_RUB')), 2))
        elif message.text == 'More':
            sti = open('static/Putin7.png', 'rb')
            bot.send_sticker(message.chat.id, sti)
            send = bot.send_message(message.chat.id,
                                    "Введите валюты заглавными буквами, как в примере. Пример: USD_UAH")
            bot.register_next_step_handler(send, oll)
        elif message.text == 'Назад 🚪':
            bot.send_message(message.chat.id,
                             "Вы вернулись на начальную страницу. Не звбывайте проверять актуальный курс валют 😊".format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=start_menu())
        elif message.text == 'Перевод валют💱':
            sti = open('static/Putin4.png', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id,
                             "Здесь вы можете выбрать нужную вам валюту,"
                             "которая будет служить для перевода 😊".format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=transfer_menu())
        # Перевод Долларов в Рубли
        elif message.text == 'US ➡ RU':
            send_ru = bot.send_message(message.chat.id, "Введите сумму для перевода долларов в рубли")
            bot.register_next_step_handler(send_ru, usd_ru)

        # Перевод Долларов в Гривны
        elif message.text == 'US ➡ UA':
            send_ua = bot.send_message(message.chat.id, "Введите сумму для перевода долларов в гривны")
            bot.register_next_step_handler(send_ua, usd_ua)

        # Перевод Долларов в Евро
        elif message.text == 'US ➡ EU':
            send_usd_eur = bot.send_message(message.chat.id, "Введите сумму для перевода долларов в евро")
            bot.register_next_step_handler(send_usd_eur, usd_eur)

        #  Перевод Рублей в Гривню
        elif message.text == 'RU ➡ UA':
            send_ru_ua = bot.send_message(message.chat.id, "Введите сумму для перевода рублей в гривны")
            bot.register_next_step_handler(send_ru_ua, ru_ua)

            # Перевод Рублей в Доллар
        elif message.text == 'RU ➡ US':
            send_ru_usd = bot.send_message(message.chat.id, "Введите сумму для перевода рублей в доллары")
            bot.register_next_step_handler(send_ru_usd, ru_usd)
            # Перевод Рублей в Евро

        elif message.text == 'RU ➡ EU':
            send_ru_eur = bot.send_message(message.chat.id, "Введите сумму для перевода рублей в евро")
            bot.register_next_step_handler(send_ru_eur, ru_eur)

        # Перевод Гривны в Рубли
        elif message.text == 'UA ➡ RU':
            send_ua_ru = bot.send_message(message.chat.id, "Введите сумму для перевода гривны в рубли")
            bot.register_next_step_handler(send_ua_ru, ua_ru)

        # Перевод Гривни в Доллар
        elif message.text == 'UA ➡ US':
            send_ua_usd = bot.send_message(message.chat.id, "Введите сумму для перевода гривны в доллары")
            bot.register_next_step_handler(send_ua_usd, ua_usd)

            # Перевод Гривни в Евро
        elif message.text == 'UA ➡ EU':
            send_ua_eur = bot.send_message(message.chat.id, "Введите сумму для перевода гривны в евро")
            bot.register_next_step_handler(send_ua_eur, ua_eur)

        # Перевод Евро в Доллар
        elif message.text == 'EU ➡ US':
            send_eur_usd = bot.send_message(message.chat.id, "Введите сумму для перевода евро в доллары")
            bot.register_next_step_handler(send_eur_usd, eur_usd)

            # Перевод Евро в Рубли
        elif message.text == 'EU ➡ RU':
            send_eur_ru = bot.send_message(message.chat.id, "Введите сумму для перевода евро в рубли")
            bot.register_next_step_handler(send_eur_ru, eur_ru)

            # Перевод Евро в Гривню
        elif message.text == 'EU ➡ UA':
            send_eur_ua = bot.send_message(message.chat.id, "Введите сумму для перевода евро в гривны")
            bot.register_next_step_handler(send_eur_ua, eur_ua)



def usd_ru(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в рублях = " + sum(float(last), get_currency_price('USD_RUB')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def eur_ru(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в рублях = " + sum(float(last), get_currency_price('EUR_RUB')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def usd_eur(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в евро = " + sum(float(last), get_currency_price('USD_EUR')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def ru_usd(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в долларах = " + sum(float(last), get_currency_price('RUB_USD')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def eur_usd(message):
    try:

        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в долларах = " + sum(float(last), get_currency_price('EUR_USD')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def ru_eur(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в евро = " + sum(float(last), get_currency_price('RUB_EUR')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def ua_ru(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в рублях = " + sum(float(last), get_currency_price('UAH_RUB')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def ru_ua(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в гривнах = " + sum(float(last), get_currency_price('RUB_UAH')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def eur_ua(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в гривнах = " + sum(float(last), get_currency_price('EUR_UAH')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def usd_ua(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в гривнах = " + sum(float(last), get_currency_price('USD_UAH')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def ua_usd(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в долларах = " + sum(float(last), get_currency_price('UAH_USD')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def ua_eur(message):
    try:
        last = message.text.split()[0]
        bot.send_message(message.chat.id,
                         "Полученная сумма в евро = " + sum(float(last), get_currency_price('UAH_EUR')))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)


def error(message):
    sti = open('static/Putin3.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, oops())


def oll(message):
    try:
        last = str(message.text.split()[0])
        bot.send_message(message.chat.id,
                                   "Полученная сумма перевода " + last + " = " + toFixed(float(get_currency_price(last)), 2))
    except ValueError:
        error(message)
    except AttributeError:
        error(message)
    except KeyError:
        error(message)

# #
# def oll_exit(message):
#     try:
#         last = message.text.split()[0]
#         bot.send_message(message.chat.id,
#                          "Полученная сумма в евро = " + last)
#     except ValueError:
#         error(message)
#     except AttributeError:
#         error(message)


# RUN
bot.polling(none_stop=True)
