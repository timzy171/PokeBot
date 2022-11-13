import telebot
from Pokemon import Pokemon
import re
from myToken import token

token = token
bot = telebot.TeleBot(token)
html = parse_mode = 'html'


@bot.message_handler(commands=['start'])
def send_echo(message):
    bot.send_message(message.chat.id,
                     "<b>Привет , </b>" + message.from_user.username + " 👋" + "\nДанный бот расскажет тебе "
                                                                              "обо всех покемонах, "
                                                                              "просто введи "
                                                                              "его имя 👇", html)

@bot.message_handler(func=lambda m: True)
def bot_answer(message):
    try:
        pokemon = Pokemon(message.text)

        bot.send_photo(message.chat.id, pokemon.get_photo())
        bot.send_message(message.chat.id,
                         '<b>' + pokemon.get_name().upper() + '</b>' +
                         "\nВес = " +
                         str(pokemon.get_weight()) + " кг" +
                         "\nРост = " + str(pokemon.get_height()) + " см" +
                         "\nID в Pokedex'e : " + str(pokemon.get_ID()) +
                         "\nТип покемона : [" + ', '.join(pokemon.get_types()).upper() + "]" +
                         '<b>' + "\nХАРАКТЕРИСТИКИ :" + '</b>' +
                         "\nHP = " + str(pokemon.get_HP()) + " ❤" +
                         "\nATTACK = " + str(pokemon.get_attack()) + " 👊" +
                         "\nDEFENSE = " + str(pokemon.get_defence()) + " 🛡️" +
                         "\nSUPER ATTACK = " + str(pokemon.get_special_attack()) + " 💣" +
                         "\nSUPER DEFENSE = " + str(pokemon.get_special_defence()) + " 🦾" +
                         "\nSPEED = " + str(pokemon.get_speed()) + " 🏃" +
                         '<b>' + "\nСПОСОБНОСТИ ПОКЕМОНА" + '</b>' + " : [" + ', '.join(
                             pokemon.get_moves()).upper() + "]", html)


    except Exception:
        if re.search("[а-яА-Я]", message.text):
            bot.send_message(message.chat.id, "Название покемона должно быть написано " + "<b>на английском языке!</b>",
                             html)
        else:
            bot.send_message(message.chat.id, "Я не знаю такого покемона :(")


bot.infinity_polling()
