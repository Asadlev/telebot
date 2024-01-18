import telebot
from config import keys, TOKEN
from utils import ConvertionExcetion, CryptoConverter

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):  # "message: telebot.types.Message" - РќРЈ Р±СѓРєРІР°Р»СЊРЅРѕ РѕР·РЅРѕС‡Р°РµС‚ - Р»СЋР±РѕРµ СЃРѕРѕР±С‰РµРЅРёРµ (С‡С‚Рѕ-Р»Рё ?)
    text = 'Р§С‚РѕР±С‹ РЅР°С‡Р°С‚СЊ СЂР°Р±РѕС‚Сѓ РІРІРµРґРёС‚Рµ РєРѕРјР°РЅРґСѓ Р±РѕС‚Сѓ \nРІ СЃР»РµРґСѓСЋС‰РµРј С„РѕСЂРјР°С‚Рµ:\n<РёРјСЏ РІР°Р»СЋС‚С‹>\n<РІ РєР°РєСѓСЋ РІР°Р»СЋС‚Сѓ РїРµСЂРµРІРµСЃС‚Рё>\n<РєРѕР»-РІРѕ РїРµСЂРµРІРѕРґРёРјРѕР№ РІР°Р»СЋС‚С‹> \
            \nРЈРІРёРґРµС‚СЊ СЃРїРёСЃРѕРє РІСЃРµС… РґРѕСЃС‚СѓРїРЅС‹С… РІР°Р»СЋС‚(РїРѕ РєРѕРјР°РЅРґРµ): /values'

    bot.reply_to(message, text)



"""РќР°РїРёСЃР°РЅРёРµ Р±РѕС‚Р°. Р—РЅР°РєРѕРјСЃС‚РІРѕ СЃ API, РїРёС€РµРј РіР»Р°РІРЅС‹Р№ РѕР±СЂР°Р±РѕС‚С‡РёРє"""
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):  # "message: telebot.types.Message" - РќРЈ Р±СѓРєРІР°Р»СЊРЅРѕ РѕР·РЅРѕС‡Р°РµС‚ - Р»СЋР±РѕРµ СЃРѕРѕР±С‰РµРЅРёРµ (С‡С‚Рѕ-Р»Рё ?)
    text = 'Р”РѕРїСѓСЃС‚РёРјС‹Рµ РІР°Р»СЋС‚С‹:'
    for key in keys.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])  # "content_types" - СЌС‚Рѕ, С‚РёРї РІРІРµРґРµРЅРёРµ, РЅР°РїСЂРёРјРµСЂ, "voice" - РіРѕР»РѕСЃРѕРІРѕРµ СЃРѕРѕР±С‰РµРЅРёРµ, "photo" - С„РѕС‚Рѕ
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        # РќР°РїРёСЃР°РЅРёРµ Р±РѕС‚Р°. РћР±СЂР°Р±Р°С‚С‹РІР°РµРј РѕС€РёР±РєРё
        if len(values) != 3:
            raise ConvertionExcetion('РЎР»РёС€РєРѕРј РјРЅРѕРіРѕ РїР°СЂР°РјРµС‚СЂРѕРІ')
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionExcetion as e:
        bot.reply_to(message, f'РћС€РёР±РєР° РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ\b{e}')
    except Exception as e:
        bot.reply_to(message, f'РќРµ СѓРґР°Р»РѕСЃСЊ РѕР±СЂР°Р±РѕС‚Р°С‚СЊ РєРѕРјР°РЅРґСѓ{e}')

    else:
        text = f'Р¦РµРЅР° {amount} {quote} РІ {base} - {total_base}'
        bot.send_message(message.chat.id, text)



bot.infinity_polling()